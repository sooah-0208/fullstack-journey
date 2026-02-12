# Apache Kafka
**대량의 데이터**를 **실시간으로** 안전하게 전달·저장하는 중간 허브
메세징프로그램(공유해야하는 데이터 싱크, 이메일, 알림설정 등등 실행가능)  

## 🤔 왜 카프카를 쓰나요?
producer A -> cunsumer A  
producer A -> cunsumer b  
producer A -> cunsumer c   
이런 시스템일 경우 producer A가 터지면 모든 컨슈머가 서비스를 이용할 수 없게 됨  
서비스 A → Kafka → B  
                → C  
                → D  
A는 책임 질게 없어짐  

## 흐름도
![alt text](image-2.png)
producer가 broker에 메세지 전달
이 Broker가 kafka, pd&cs가 개발자가 만든 것들
컨슈머가 메세지 하나를 읽음 -> 처리 완료되면 브로커가 삭제함

## CMD에서 kafka 실행하기

**Kafka Port: 9092**

kafka 명령어는 window에서 바로 실행할 수 없음
-> 환경변수 설정
-> 시스템 변수의 Path 
-> 편집 눌러서 새로 만들기
-> 내가 kafka Binary 다운로드한 경로 그대로 복붙해서 생성
-> cmd에 들어가서 kafka 명령어 실행하면 실행 됨!

1. Kafka 이미지 받기
```
docker pull apache/kafka:4.0.1
```

2. docker container 접속하기
```
docker exec -it kafka /bin/bash
```

3. kafka 파일 위치로 접근하기
```
cd /opt/kafka/bin
```

4. 토픽 만들기
```
./kafka-topics.sh --bootstrap-server localhost:9092 --create --topic my-topic
```

5. 토픽 목록 보기
```
./kafka-topics.sh --bootstrap-server localhost:9092 --list
```

6. 토픽 목록 삭제하기
```
./kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic my-topic
```

7. 토픽에 내용물 넣기
```
./kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test
```
- producer로 들어가면 보내짐
```
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
```
- consumer로 들어가면 보낸 내용 받을 수 있고 뒤에 --from-beginning이 있으면 첫 내용부터, 없으면 접속 시점부터 보여짐


## python에서 kafka 실행하기
```main.py
from kafka import KafkaProducer

pd = KafkaProducer(bootstrap_servers="localhost:9092")

pd.send('test',b'loveyou')
#('토픽이름', b'메세지')
# producer&consumer의 토픽 이름이 같아야 확인이 가능함
pd.flush()
# 보낸다는 함수
```
```받을쪽.py
from kafka import KafkaConsumer

cs=KafkaConsumer('test',bootstrap_servers=["localhost:9092"])

for msg in cs:
    print(msg.value)
```

그리고 각각 터미널 열어 각 파일 실행해주기 => main.py의 메세지 바꿔서 실행할 때 마다 consumer 터미널에 내용이 찍힘

[Kafka Tutorial PDF](./Kafka%20Python%20Tutorial.pdf)

# Kafka
apache/kafka

모든 ip에서 열기
```
docker run -d --name kafka -e KAFKA_NODE_ID=1 -e KAFKA_PROCESS_ROLES=broker,controller -e KAFKA_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 -e KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@localhost:9093 -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 -e KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR=1 -e KAFKA_TRANSACTION_STATE_LOG_MIN_ISR=1 -e KAFKA_GROUP_INITIAL_REBALANCE_DELAY_MS=0 -e KAFKA_NUM_PARTITIONS=3 apache/kafka:4.0.1
```



kafka ip: 172.17.0.2

1. app1 설정
```
uv init . 
uv add fastapi --extra standard
uv add kafka-python
```

## uv 이미지 생성 (docker file) 
도커파일
```
FROM python:3.13.11

RUN apt-get update
RUN apt-get upgrade -y
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN pip install uv

WORKDIR /workspace

EXPOSE 8000
```

```
docker build -t uv:1
```

## app1 container 생성
```
docker run -d -it -p 8001:8001 -v ./app1:/workspace --name app1 uv:1
```
-d는 서비스가 돌고있는게 있어야 켜짐
없으면 -it까지 넣어서 접속해서 사용하겠다고 선언해주기

app1 ip 확인
- docker에서 Inspect - network로 확인
- 
`172.17.0.3`



## Fastapi로 Mail서버 실행하기

[fastapi Mail사이트](https://sabuhish.github.io/fastapi-mail/example/)