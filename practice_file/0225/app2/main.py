from fastapi import FastAPI, Request, Response, Cookie
from settings import settings
from authlib.integrations.starlette_client import OAuth
from starlette.middleware.sessions import SessionMiddleware
import httpx
import redis
import uuid

oauth = OAuth()
oauth.register(
    # 접근할 때 사용하는 이름, 필수조항
  name='kakao',
  client_id=settings.client_id,
  client_secret=settings.client_secret,
  authorize_url="https://kauth.kakao.com/oauth/authorize",
      # 일정시간 이내 발송하지 않으면 사라짐
  access_token_url="https://kauth.kakao.com/oauth/token",
  api_base_url="https://kapi.kakao.com",
  client_kwargs={
    "scope": "profile_nickname profile_image",
    # 'token_endpoint_auth_method': 'client_secret_basic',
    # 'token_placement': 'header',
                 }
)

client1 = redis.Redis(host="redis", port=6379, db=0,decode_responses=True ) # access_token용 redis
client2 = redis.Redis(host="redis", port=6379, db=1,decode_responses=True) # refresh_token용 redis

app = FastAPI(title=settings.title, root_path=settings.root_path)
app.add_middleware(
  SessionMiddleware,
  secret_key="your-secret-key-here"
)

async def getToken(client, code: str):
  return await client.post(
     "https://kauth.kakao.com/oauth/token",
    data={
      "grant_type": "authorization_code",
      "client_id": settings.client_id,
      "redirect_uri": settings.redirect_uri,
      "code": code,
      "client_secret": settings.client_secret,
    },
    headers={"Content-Type": "application/x-www-form-urlencoded"}
  )

async def getUserInfo(client, access_token: str):
  return await client.post(
    "https://kapi.kakao.com/v2/user/me",
    headers={"Authorization": f"Bearer {access_token}"}
  )


async def setUserLogout(client, access_token: str):
  return await client.get(
    "https://kapi.kakao.com/v1/user/logout",
    headers={"Authorization": f"Bearer {access_token}"}
  )


@app.get("/")
def read_root():
  return {"service": "App2"}

@app.get("/login/kakao")
async def kakaoLogin(request: Request):
  redirect_uri = settings.redirect_uri
  return await oauth.kakao.authorize_redirect(request, redirect_uri)

@app.get("/oauth/callback/kakao")
async def kakaoCallback(code: str, response:Response):
  async with httpx.AsyncClient() as client:
    tokenResponse = await getToken(client, code)
    tokens = tokenResponse.json()

    access_token = tokens.get("access_token")
    expires_in = tokens.get("expires_in")
    refresh_token = tokens.get("refresh_token")
    refresh_token_expires_in = tokens.get("refresh_token_expires_in")
    
    id=uuid.uuid4().hex
    client1.setex(id, int(refresh_token_expires_in), access_token)
    client2.setex(id, int(refresh_token_expires_in), refresh_token)
    
    response.set_cookie(
    key="accept",      # 쿠키 이름
    value=id,      # 저장할 값
    httponly=True,           # JavaScript에서 접근 불가 (보안)
    max_age=int(expires_in),            # 쿠키 유지 시간 (초 단위, 3600 = 1시간)
    expires=int(expires_in),            # 만료 시간 (max_age와 유사)
    path="/",                # 쿠키가 유효한 경로
    domain=settings.dns,             # 특정 도메인에서만 유효하게 설정 시 사용
    secure=False,            # True 설정 시 HTTPS에서만 전송
    samesite="lax"           # CSRF 공격 방지 설정 ("lax", "strict", "none")
)

    # 보안상의 이유로 토큰은 redis로 관리함
    # response.set_cookie(
    #     key="access_token",      # 쿠키 이름
    #     value=access_token,      # 저장할 값
    #     httponly=True,           # JavaScript에서 접근 불가 (보안)
    #     max_age=int(expires_in),            # 쿠키 유지 시간 (초 단위, 3600 = 1시간)
    #     expires=int(expires_in),            # 만료 시간 (max_age와 유사)
    #     path="/",                # 쿠키가 유효한 경로
    #     domain="aiedu.tplinkdns.com",             # 특정 도메인에서만 유효하게 설정 시 사용
    #     secure=False,            # True 설정 시 HTTPS에서만 전송
    #     samesite="lax"           # CSRF 공격 방지 설정 ("lax", "strict", "none")
    # )

    # response.set_cookie(
    #     key="refresh_token",
    #     value=refresh_token,
    #     httponly=True,
    #     max_age=int(refresh_token_expires_in),
    #     expires=int(refresh_token_expires_in),
    #     path="/",
    #     domain="aiedu.tplinkdns.com",
    #     secure=False,
    #     samesite="lax"
    # )
    return {"status":True, "token":tokenResponse.json()}
  return {"status": False}
  # kakao = oauth.create_client('kakao')
  # access_token = await oauth.kakao.authorize_access_token(request)
  # return{"access_token":access_token}

@app.get('/me')
async def me(accept: str = Cookie(default=None)):
  if accept:
    access_token = client1.get(accept)
    async with httpx.AsyncClient() as client:
      userResponse = await getUserInfo(client, access_token)
      userInfo = userResponse.json()

      if userResponse.status_code == 200:
        user = {
          "id":userInfo.get("id"),
          "nickname":userInfo.get("properties")["nickname"],
          "profile_image":userInfo.get("properties")["profile_image"],
        }
        return {"status":True, "userInfo": user}
  return {"status":False}

@app.get("/logout")
async def logout(response : Response, request:Request,accept: str = Cookie(default=None)):
    if accept:
      access_token = client1.get(accept)
      async with httpx.AsyncClient() as client:
        logoutResponse = await setUserLogout(client, access_token)
        if logoutResponse.status_code == 200:
          client1.delete(accept)
          client2.delete(accept)
          for cookieName in request.cookies.keys():
            response.delete_cookie(
              key=cookieName,
              path="/",
              domain=settings.dns,
              httponly=False,
              samesite="lax"
            )
          return{"status":True}
    return {"status":False}