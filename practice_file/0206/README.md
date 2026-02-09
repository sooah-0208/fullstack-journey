## Kafka 이미지 받기

```
docker pull apache/kafka:4.0.1
```

## docker container 접속하기
```
docker exec -it kafka /bin/bash
```

## kafka 파일 위치
```
/opt/kafka/bin
```

## 토픽 만들기
```
./kafka-topics.sh --bootstrap-server localhost:9092 --create --topic my-topic
```

## 토픽 목록 보기
```
./kafka-topics.sh --bootstrap-server localhost:9092 --list
```

## 토픽 목록 삭제하기
```
./kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic my-topic
```

## 토픽에 내용물 넣기
```
./kafka-console-producer.sh --bootstrap-server localhost:9092 --topic test
```
producer로 들어가면 보내짐
```
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning
```
consumer로 들어가면 보낸 내용 받을 수 있고 뒤에 --from-beginning이 있으면 첫 내용부터, 없으면 접속 시점부터 보여짐

## mail용 Fastapi
python 설치파일
```
"fastapi-mail>=1.6.1",
    "fastapi[standard]>=0.128.2",
    "pydantic-settings>=2.12.0",
```