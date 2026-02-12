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
from db import findOne, findAll, save, add_key

# router = APIRouter(
#     prefix="/users",
#     tags=["Users"]
# )
app = FastAPI()

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
# 경로에 폴더가 있는지 판단해서 없으면 만들어줌 ()안의 내용 = 폴더가 있어도 오류 안나게 허용

def saveFile(file):
  checkDir()
  origin = file.filename
  ext = origin.split(".")[-1].lower()
  id = uuid.uuid4().hex
  newName = f'{uuid.uuid4().hex}.{ext}'
  # data = {"id":id, "origin": origin, "ext":ext, "newName":newName}
  # db.append(data)
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
  # shutil.copyfileobj(원본, 복제할 대상), 이미 있는 거 또 넣어도 오류 안 남

@app.get("/")
def root():
  return {"status": True}
# get은 오직! 문자열만 param으로 보낼 수 있음
# post put fetch는 파일 업로드에 쓸 수 있음

@app.post("/upload")
def file_upload(files: List[UploadFile] = File(None), txt:str =Form('')):
# front에서 보낼 때 "name"에 든 이름으로 변수를 지정해줘야함 프론트파일에서 확인
# file: UploadFile 파일을 업로드 한다는 뜻, =File()파일 형식으로 받겠다. 파일 주고받을거면 얘 내용은 고정
  arr = []
  for file in files:
    arr.append(saveFile(file))
  return {"status": True, "result":arr}

# class fileItem(BaseModel):
#   filename: str
  # content_type:str
  # content_base64:str

class fileModel(BaseModel):
  txt: str
  files: List[str]

@app.post('/upload2')
def upload(model:fileModel):
  print(model)
  return{"status":True}

# @app.get('/images')
# def images():
#   return {"status":True, "result": db}

@app.get('/download')
def download(id:str):
  # for row in db:
  #   if row['id'] == id:
  #     origin = row['origin']
  #     newName = row['newName']
  #     break
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