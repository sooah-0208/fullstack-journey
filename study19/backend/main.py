from fastapi import FastAPI, Header, Depends, Request, Response, Cookie
from fastapi.middleware.cors import CORSMiddleware 
# 포트다른 사이트가 접근하게 만드는 부분, CORS 검색해보면 코드 나옴
from pydantic import BaseModel, Field
# post 사용할 때는 BaseModel이 필수임. 세트라고 생각하면 됨
from datetime import datetime, timedelta, timezone
# 시간 관련 함수들
from jose import jwt, JWTError
# jwt 암호화하기위해 임폿해옴. 이게 있어야 encode, decode가능
from settings import settings
# 환경변수 매번 바꾸기 힘드니까 pydantic_settings로 기본세팅해주기. env만 바꿔주면 db접근가능
from db import findOne, findAll, save
import mariadb
import uuid

SECRET_KEY = "your-extremely-secure-random-secret-key"
# 서명하는 비밀키
ALGORITHM = "HS256"
# 서명방식, JWT 홈페이지 Libraries 가보면 python 전용 알고리즘이 있음 걔가 hs256
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# 토큰 유지시간(분)


## 토큰 어떻게 생성할지 정하는 함수
def set_token(no: int, name: str):
  try:
    iat = datetime.now(timezone.utc) + (timedelta(hours=7))
    # 발행시간. timezone이 세계시간 보통 유럽 기준이라 utc로 써줌
    # timedelta는 시간 전/후 관리할 수 있게 해주는 시간계산도구
    exp = iat + (timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    # 만료시간
    data = {
      "name": name,
      "iss": "EDU", 
      "sub": str(no), 
      "iat": iat,
      "exp": exp
    }
    # data는 무조건 객체형이고 전부 "문자열"로 받아와야함
    id = uuid.uuid4().hex
    token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    sql = f"INSERT INTO edu.`login` (`id`, `userNo`, `token`) VALUE ('{id}', {no}, '{token}')"
    if save(sql): return id
  except JWTError as e:
    print(f"JWT ERROR : {e}")
  return None

def get_user(user: str = Cookie(None)):
  if user:
    sql = f"select * from edu.`login` where `id` = '{user}'"
    result = findOne(sql)
    if result:
      return jwt.decode(result["token"], SECRET_KEY, algorithms=ALGORITHM)
  return None

origins = [ settings.react_url ]

class LoginModel(BaseModel):
  email: str = Field(..., title="이메일 주소", description="로그인를 위한 이메일 주소 입니다.")
  # Field는 docs하단부에 설명 달아주는 아이라 없어도 됨
  pwd: str = Field(..., title="비밀번호", description="로그인를 위한 비밀번호 입니다.")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 포트가 다른 양쪽이 서로 접근할 수 있게 해주는 코드.

@app.get("/")
def read_root():
  return {"status": True, "msg": "공유해 드림"}

@app.post("/login")
def login(model : LoginModel, response : Response):
  sql = settings.login_sql.replace("{email}", model.email).replace("{pwd}", model.pwd)
  data = findOne(sql)
  if data:
    access_token = set_token(data["no"], data["name"])
    print(access_token)
    response.set_cookie(
        key="user",
        value=access_token,
        max_age=60 * 60,        # 1시간 (초)
        expires=60 * 60,        # max_age와 유사 (초)
        path="/",
        domain="localhost",
        secure=True,            # HTTPS에서만 전송
        httponly=True,          # JS 접근 차단 (⭐ 보안 중요)
        samesite="lax",         # 'lax' | 'strict' | 'none'
      )
    return {"status": True}
  else:
    return {"status": False}

@app.get("/me")
def me(payload = Depends(get_user)):
  if payload:
    return {"status": True, "me": payload["name"]}
  else:
    return {"status": False}

@app.post("/logout")
def logout(response: Response):
  response.delete_cookie(key="user")
  return {"status": True}
