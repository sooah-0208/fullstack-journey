# kafka 만들기

 ```bash
docker run -d --name kafka --network my-net -p 9092:9092 -e KAFKA_CLUSTER_ID=kraft-cluster-1 -e KAFKA_NODE_ID=1 -e KAFKA_PROCESS_ROLES=broker,controller -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092 -e KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@kafka:9093 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -e KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=1 -e KAFKA_TRANSACTION_STATE_LOG_MIN_ISR=1 -e KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS=0 -e KAFKA_NUM_PARTITIONS=3 apache/kafka:4.0.1

 ```

 ```bash
 docker network inspect bridge
```
- Network IP : 172.17.0.2 **kafka**

## 1. App1 설정

 ```bash
 uv init. 
uv add fastapi --extra standard
uv add kafka-python
 ```

 ## UV 이미지 생성 `dokcerfile`

 ```bash
 FROM python:3.13.11

 RUN apt-get update
 RUN apt-get upgrade -y
 RUN curl -LsSf https://astral.sh/uv/install.sh | sh
 RUN pip install uv

 WORKDIR /workspace

 EXPOSE 8000
 ```

 ```bash
 docker build -t uv:1
 ```

 ## APP1 Container 생성

```bash
docker run -d -it -p 8001:8000 -v ./:/workspace --network=my-net --name app1 uv:1
```

- Network IP : 172.17.0.3 **app1**