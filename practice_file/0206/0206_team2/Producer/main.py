# from fastapi import FastAPI
# from kafka import KafkaProducer
# from settings import settings
# from pydantic import EmailStr, BaseModel
# import json

# app=FastAPI()

# class EmailModel(BaseModel):
#     email: EmailStr
#     content: str
#     title: str

# @app.get("/")
# def read_root():
#     return{"msg":"Producer"}

# pd = KafkaProducer(bootstrap_servers=settings.kafka_server, value_serializer=lambda v: json.dumps(v).encode("utf-8"))

# @app.post("/pd")
# def producer(model:EmailModel):
#     pd.send(settings.kafka_topic, model.dict()))
#     pd.flush()
#     return{"status": True}



from fastapi import FastAPI, Body
from kafka import KafkaProducer
from settings import settings
import json
# from typing import List
from pydantic import EmailStr, BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailModel(BaseModel):
    # email: List[EmailStr]
    email: EmailStr
    content: str
    title: str


# 1. 시리얼라이저 등록 (모든 value는 여기서 자동으로 JSON/Byte 변환됨)
pd = KafkaProducer(
    bootstrap_servers=settings.kafka_server,
    value_serializer=lambda v: json.dumps(v, ensure_ascii=False).encode("utf-8")
)

@app.get('/')
def root():
    return {"message": "안녕하세요"}

@app.post('/pd')
def producer(model: EmailModel): # JSON Body로 문자열을 받음
    # [수정] 이미 pd 설정에서 인코딩을 해주므로, 여기선 문자열 그대로 보냅니다.
    # 만약 여기서 .encode()를 또 하면 시리얼라이저가 바이트를 다시 변환하려다 에러가 날 수 있습니다.
    pd.send(settings.kafka_topic, dict(model)) 
    pd.flush()
    return {"status": True}