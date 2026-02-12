from fastapi import FastAPI, Depends, HTTPException, status
from kafka import KafkaProducer
from settings import settings
from pydantic import EmailStr, BaseModel
import json
import redis
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError, ExpiredSignatureError
from db import findOne
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware

security = HTTPBearer()

class EmailModel(BaseModel):
  email: EmailStr

class CodeModel(BaseModel):
  id: str


def set_token(email: str):
  try:
    sql = f"SELECT `no`, `name` FROM test.user WHERE `email` = '{email}'"
    data = findOne(sql)
    if data:
      iat = datetime.now(timezone.utc)
      exp = iat + (timedelta(minutes=settings.access_token_expire_minutes))
      data = {
        "name": data["name"],
        "iss": "EDU",
        "sub": str(data["no"]),
        "iat": iat,
        "exp": exp
      }
      return jwt.encode(data, settings.secret_key, algorithm=settings.algorithm)
  except JWTError as e:
    print(f"JWT ERROR : {e}")
  return None

def get_payload(credentials: HTTPAuthorizationCredentials = Depends(security)):
  if credentials.scheme == "Bearer":
    try:
      payload = jwt.decode(credentials.credentials, settings.secret_key, algorithms=settings.algorithm)
      exp = payload.get("exp")

      now = datetime.now(timezone.utc).timestamp()
      minutes, remaining_seconds = divmod(int(exp - now), 60)
      return payload
    except ExpiredSignatureError as e:
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token expired",
      )
    except JWTError as e:
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
      )
  return None

app = FastAPI(title="Producer")

kafka_server=settings.kafka_server
kafka_topic=settings.kafka_topic

pd = KafkaProducer(
  bootstrap_servers=kafka_server,
  value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

client = redis.Redis(
  host=settings.redis_host,
  port=settings.redis_port,
  db=settings.redis_db,
  decode_responses=True
)

origins = [ settings.react_url ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
  return {"Hello": "World"}

@app.post("/login")
def producer(model: EmailModel):
  pd.send(settings.kafka_topic, dict(model))
  pd.flush()
  return {"status": True}

@app.post("/code")
def code(model: CodeModel):
  print(model.id)
  result = client.get(model.id)
  print(result)
  if result:
    access_token = set_token(result)
    if access_token:
      # model에 있는 데이터 삭제
      # client.delete(model.id)
      return {"status": True, "access_token": access_token}
  return {"status": False}

@app.post("/me")
def me(payload = Depends(get_payload)):
  if payload:
    print(payload)
    return {"status": True, "no": payload["sub"], "name": payload["name"]}
  return {"status": False}


## 위에가 로그인인증

## 아래가 파일업로드

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
from pathlib import Path
app = FastAPI()
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import shutil
import uuid
from settings import settings
from db import findOne, findAll, save, add_keyapp = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:5173","http://app2:5173", "http://app2", "http://localhost"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


UPLOAD_DIR = Path("uploads")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
MAX_FILE_SIZE = 10 * 1024

# db = []

def checkDir():
  UPLOAD_DIR.mkdir(exist_ok=True)


def saveFile(file):
  checkDir()
  origin = file.filename
  ext = origin.split(".")[-1].lower()
  id = uuid.uuid4().hex
  newName = f'{uuid.uuid4().hex}.{ext}'
  sql = f"""
  insert into edu.`file` (`origin`,`ext`,`fileName`,`contentType`) 
  value ('{origin}','{ext}', '{newName}','{file.content_type}')
  """
  result = add_key(sql)
  if result[0]:
    path = UPLOAD_DIR / newName
    with path.open("wb") as f:
      shutil.copyfileobj(file.file, f)
    return {result[1]}
  return 0

@app.get("/")
def root():
  return {"status": True}

@app.post("/upload")
def file_upload(files: List[UploadFile] = File(None), txt:str =Form('')):
  arr = []
  for file in files:
    arr.append(saveFile(file))
  return {"status": True, "result":arr}

class fileModel(BaseModel):
  txt: str
  files: List[str]

@app.post('/upload2')
def upload(model:fileModel):
  print(model)
  return{"status":True}

@app.get('/download')
def download(id:str):
  sql =f"""
  select `origin`, `fileName`
  from edu.`file`
  where `no`={id}
  """
  result = findOne(sql)
  if result:
    print(result)
    origin = result['origin']
    newName = result['fileName']
    path = UPLOAD_DIR / newName
    return FileResponse(path = path, filename = origin)
  return {"status":False}

