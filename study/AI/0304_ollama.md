# OLLAMA
AI 모델 전용 플레이어(로컬 챗봇이라고 생각하면 됨)

## Ollama 알아보기 : `LLM 서버`

- [앱 다운받기](https://ollama.com/download)
- [LLM 모델 검색](https://ollama.com/search)

### PC 설정
- 다운로드 후 Ollama 버젼 확인
```bash
ollama --version
```

- `GPT-OSS:20b` 모델 받기
```bash
ollama pull gpt-oss:20b
```

- 환경 변수 추가 : `외부 접속 허용`
```bash
OLLAMA_HOST=0.0.0.0

로컬 pc는
OLLAMA_HOST=http://서버IP:11434
```

- 방화벽 포트 허용(이라고 찾기에 검색하면 나옴) : `인바운드 규칙` 추가
```bash
이름 : OLLAMA
프로토콜 : TCP
포트 : 11434
```

- CLI 방식으로 서버 실행 : `log` 확인 가능
```bash
ollama serve
```

- 모델 확인 `get` 요청
```bash
curl http://localhost:11434/api/tags
```

- 프롬프트 `post` 요청
```bash
curl -X POST http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3:8b",
    "prompt": "Ollma에 대해 간단하게 설명해주세요.",
    "stream": false
  }'
```