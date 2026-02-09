from fastapi import FastAPI
from kafka import KafkaConsumer
from settings import settings
import threading

def consumer():
    cs = KafkaConsumer(settings.kafka_topic, bootstrap_servers=settings.kafka_sever)
    for msg in cs:
        print(msg.value.decode('utf-8')) #비즈니스 로직은 여기서 처리

def startCousumer():
    thread=threading.Thread(target=consumer, daemon=True)
    thread.start()

app=FastAPI()

@app.get("/")
def read_root():
    return{"msg":"Consumer"}

@app.get("/start")
def start():
    startCousumer()