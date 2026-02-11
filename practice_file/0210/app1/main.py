from fastapi import FastAPI
from kafka import KafkaProducer
from pydantic import EmailStr, BaseModel
import json

app = FastAPI()

kafka_server='kafka:9092'
kafka_topic='test'

pd = KafkaProducer(
    bootstrap_servers=kafka_server,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.get('/')
def get():
    return{"status":True}


@app.post("/msg")
def producer(msg: str):
  pd.send(kafka_topic, {"msg": msg})
  pd.flush()
  return {"status": True}