from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from db import getConn, findOne, findAll, save
import uuid

app = FastAPI()

SECRET_KEY ='your-extremely-secure-random-secret-key'
# 서명하는 비밀키
ALGORITHM='HS256'
# 서명방식, JWT 홈페이지 Libraries 가보면 python 전용 알고리즘이 있음 걔가 hs256
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# 토큰 유지시간(분)

origins = [
  "http://localhost:5173"
  # 프론트 url
] #을 origins로 관리함 링크 매번 넣기 귀찮으니까

class loginModel(BaseModel):
  email: str
  pwd: str
# post하려면 BaseModel이 필수로 지정되어야함

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 다른 포트가 서로 접속할 수 있게 열어주는 코드


@app.get("/")
def read_root():
  return {"status": True, "result": ["공유는 해드림"]}

@app.post('/key')
def key(model: loginModel):
  #        키 : 벨류 설정해줌
  sql = f"""select * from team2.user
        where `email` = '{model.email}'
        and `password` = '{model.pwd}'  
        """
  # DB에서 데이터 가져오는 sql문
  data = findOne(sql)
  # 맞는 하나만 찾아옴
  print(data)
  # 이건 데이터 확인 차 나오는지 찍어보는 용. 실제론 없어야함
  if data:
    id = uuid.uuid4().hex
    # 랜덤 문자열을 만들어주는 코드
    # uuid1은 Mac주소로 제작해서 노출 위험 있음, 2는 python에서 안 씀, 3은 이름기반 해시, 4번이 완전 랜덤이라 보통 4를 씀
    # hex는 `-`를 빼고 16진수 문자열로 만들어주는 메소드
    token = set_token(data['no'],data['email'])
    # token에 뭐 넣을지 지정
    sql = f'insert into team2.`login` (`id`,`userNo`,`token`) value("{id}","{data['no']}", "{token}")'
    # 로그인 할 때 마다 db에 토큰 저장해줌()
    if save(sql):
      return{'status': True, 'access_token': id}
  return {'status':False}


@app.post('/login')
def get(loginmodel: loginModel):
  sql = f'''
        select * from team2.user
        where `email` = '{loginmodel.email}'
        and `password` = '{loginmodel.pwd}'  
        '''
  data = findAll(sql)
  if data:
    access_token = set_token(data[0]['no'], data[0]['email'])
    return{'status':True, 'loginmodel':loginmodel, 'access_token': access_token}
  else: pass
  

def set_token(num, email):
  try:
    iat = datetime.now(timezone.utc) + (timedelta(hours=7))
    exp = iat + (timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    data = { 'email': email,
            'iss': 'edu',
            'sub': str(num), 
            'iat': iat,
            'exp': exp}
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
  except JWTError as e:
    print(f"'JWTError: ' {e}'")
  return{'status': False}


@app.post('/token')
def token():
  result = set_token(1)
  return {'status': True, 'token': result}
  # try:
  #   iat = datetime.now(timezone.utc) + (timedelta(hours=7))
  #   exp = iat + (timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
  #   # 현재시간 기준 30분(위에 30으로 했음)뒤에 만료시키겠다
  #   # timedelta = 시간 길이를 나타내는 타입
  #   data = {'iss': '수아',
  #            'sub': str(1), 
  #            'iat': iat,
  #            'exp': exp}
  #   # 이 데이터를 JWT Patload의 '클레임'이라고 부름
  #   # iss = 발급자 
  #   # sub = 제목/사용자ID 등 식별자 : 얘는 꼭 문자열로 받아야해서 str로 바꿔줌
  #   # iat = 발급시간 timezone은 전세계시간, 보통 유럽 기준이라 utc 선택해옴
  #   # exp = 만료시간
  #   result = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
  #   #토큰 만드는 방법 encode(안에 데이터, 키, 알고리즘)
  #   #jwt=JSON Web Token
  #   #쿠키는 프론트에서 생기는 인증수단
  #   #jwt는 백에서 생기는 인증수단
  #   # 인증 받았으면 인가를 해야겠져? 그건 이 이후에 추가됩니다
  #   return{'status': True, 'token': result}
  # except JWTError as e:
  #   print(f"'JWTError: ' {e}'")
  # return{'status': True}

# @app.post("/login")  #쿼리스티링형식으로 접근시키기, /login으로 접근한 요청을 아래 함수로 실행시켜줌
# def login(loginModel: LoginModel, response: Response):
#   response.set_cookie(
#     key="user",
#     value=loginModel.email,
#     max_age=60 * 60,        # 1시간 (초)
#     expires=60 * 60,        # max_age와 유사 (초)
#     path="/",
#     domain="localhost",
#     secure=True,            # HTTPS에서만 전송
#     httponly=True,          # JS 접근 차단 (⭐ 보안 중요)
#     samesite="lax",         # 'lax' | 'strict' | 'none'
#   )
#   return {"status": True, "model": loginModel}

# @app.post("/logout")
# def logout(response: Response):
#   response.delete_cookie(key="user")
#   return {"status": True}

# @app.get("/user")
# def user(request: Request):
#   email = request.cookies.get("user")
#   if email:
#     return {"status": True, "me": email}
#   else:
#     return {"status": False}
  

