# from fastapi import FastAPI
# from kafka import KafkaConsumer, KafkaProducer
# from settings import settings
# import threading
# from typing import List
# from starlette.responses import JSONResponse
# from pydantic import EmailStr, BaseModel
# from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
# import asyncio
# import json
# from fastapi.middleware.cors import CORSMiddleware

# app=FastAPI()

# origins = [
#     "http://localhost:5173",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class EmailModel(BaseModel):
#     email: EmailStr
#     content: str
#     title: str

# conf = ConnectionConfig(
#     MAIL_USERNAME = settings.mail_username,
#     MAIL_PASSWORD = settings.mail_password,
#     MAIL_FROM = settings.mail_from,
#     MAIL_PORT = settings.mail_port,
#     MAIL_SERVER = settings.mail_server,
#     MAIL_FROM_NAME=settings.mail_from_name,
#     MAIL_STARTTLS = settings.mail_starttls,
#     MAIL_SSL_TLS = settings.mail_ssl_tls,
#     USE_CREDENTIALS = settings.use_credentials,
#     VALIDATE_CERTS = settings.validate_certs
# )


# @app.post("/email")
# async def simple_send(model: EmailModel) -> JSONResponse:
#     html = f"""<h1>{model.title}</h1>
# <p>{model.content}</p>
# """

#     message = MessageSchema(
#         subject=model.title,
#         recipients=[model.email],
#         body=html,
#         subtype=MessageType.html)

#     fm = FastMail(conf)
#     await fm.send_message(message)
#     return{"status":True, "data":model.title}

# # def consumer():
# #     cs = KafkaConsumer(settings.kafka_topic, bootstrap_servers=settings.kafka_server,enable_auto_commit=True,
# value_serializer=lambda v:json.load(v.decode("utf-8")
# #     for msg in cs:
# #         print(msg.value.decode('utf-8'))
# #         data = json.load(msg.value.decode("utf-8"))
# #         model = EmailModel(**data)
# #         asyncio.run(simple_send(model,))

# @app.on_event('startup')
# def start_consumer():
#     thread = threading.Thread(target=consumer, daemon=True)
#     thread.start()


# @app.get("/")
# def read_root():
#     return{"msg":"Consumer"}

# # @app.get("/start")
# # def start():
# #     startCousumer()

from fastapi import FastAPI
from kafka import KafkaConsumer
from settings import settings
import threading
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
import asyncio
import json
from pydantic import EmailStr, BaseModel

app = FastAPI()

conf = ConnectionConfig(
    MAIL_USERNAME = settings.mail_username,
    MAIL_PASSWORD = settings.mail_password,
    MAIL_FROM = settings.mail_from,
    MAIL_PORT = settings.mail_port,
    MAIL_SERVER = settings.mail_server,
    MAIL_FROM_NAME=settings.mail_from_name,
    MAIL_STARTTLS = settings.mail_starttls,
    MAIL_SSL_TLS = settings.mail_ssl_tls,
    USE_CREDENTIALS = settings.use_credentials,
    VALIDATE_CERTS = settings.validate_certs,
)

class EmailModel(BaseModel):
    email: EmailStr
    content: str
    title: str

async def simple_send(model:EmailModel):
    html = f"""<h1>{model['title']}</h1> 
                <p>{model['content']}<p>
    """

    message = MessageSchema(
        subject=model['title'],
        recipients=[model['email']],
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)

def consumer():
    cs = KafkaConsumer(
        settings.kafka_topic, 
        bootstrap_servers=settings.kafka_server, 
        # [수정] load -> loads (문자열을 파싱할 때는 s가 붙어야 함)
        value_deserializer=lambda v: json.loads(v.decode("utf-8"))
    )
    
    for msg in cs:
        # 이제 msg.value는 시리얼라이즈된 파이썬 dict 객체입니다.
        print(f"수신된 데이터: {msg.value}")
        data = {"email":msg.value['email'], 'title':msg.value['title'], "content":msg.value['content']}
        asyncio.run(simple_send(data))

@app.on_event("startup")
def startConsumer():
    thread = threading.Thread(target = consumer, daemon=True)
    thread.start()



@app.get('/')
def root():
    return {"안녕"}

@app.get("/start")
def start():
    startConsumer()