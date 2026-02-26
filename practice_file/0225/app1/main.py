from fastapi import FastAPI, Request, Response, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import httpx 
from settings import settings

# 1. FastAPI 앱 초기화
# docs_url=None은 게이트웨이 자체의 Swagger 문서 노출을 막기 위함입니다.
app = FastAPI(title=settings.title, docs_url=None)

# 2. 서비스 맵 설정 (라우팅 테이블)
# 어떤 경로(/app1)로 들어왔을 때 어떤 서버(http://service-1)로 보낼지 결정합니다.
SERVICE_MAP = {
    settings.app1_path: settings.app1_url,
    settings.app2_path: settings.app2_url,
}

# 3. 비동기 HTTP 클라이언트 생성
# 매 요청마다 클라이언트를 새로 만들면 성능이 떨어지므로, 전역적으로 하나를 생성해 재사용합니다.
# timeout=10.0은 대상 서버가 10초 동안 응답 없으면 연결을 끊겠다는 뜻입니다.
client = httpx.AsyncClient(timeout=10.0)

# 4. 리버스 프록시 미들웨어 정의
# 모든 HTTP 요청은 이 미들웨어를 통과하며 가공됩니다.
class ReverseProxyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path  # 클라이언트가 요청한 경로 (예: /app1/items)
        service_url = None

        # 5. 경로 매칭 (가장 긴 경로 우선 매칭)
        # 예: /app1/v2 와 /app1 이 있다면 더 구체적인 /app1/v2를 먼저 찾도록 정렬합니다.
        for prefix, url in sorted(SERVICE_MAP.items(), key=lambda x: -len(x[0])):
            if path.startswith(prefix):
                service_url = url
                # 접두사(prefix)를 떼어내고 실제 서비스가 받을 경로만 남깁니다.
                # 예: /app1/items -> /items
                path_suffix = path[len(prefix):] or "/"
                if not path_suffix.startswith("/"):
                    path_suffix = "/" + path_suffix
                break

        # 6. 매칭되는 서비스가 없을 경우
        # 게이트웨이가 처리할 경로가 아니면 다음 미들웨어나 일반 라우터로 넘깁니다.
        if not service_url:
            return await call_next(request)

        # 7. 홉 간(Hop-by-hop) 헤더 제거
        # HTTP 표준에 따라 프록시 서버가 다음 서버로 그대로 전달하면 안 되는 헤더들을 필터링합니다.
        excluded_headers = [
            "host", "connection", "keep-alive", "proxy-authenticate",
            "proxy-authorization", "te", "trailers", "transfer-encoding", "upgrade"
        ]
        headers = {k: v for k, v in request.headers.items() if k.lower() not in excluded_headers}

        # 8. 요청 바디 추출
        # POST, PUT 처럼 데이터가 포함된 요청의 경우 바디 내용을 읽어옵니다.
        body = await request.body() if request.method in ("POST", "PUT", "PATCH") else None

        # 9. 실제 마이크로서비스로 요청 전달 (Proxying)
        try:
            proxy_resp = await client.request(
            method=request.method,
            url=f"{service_url}{path_suffix}",
            headers=headers,
            content=body,
            params=request.query_params,
      )
            
            # 10. 대상 서버의 응답 헤더 재구성
            response_headers = [(k.encode("latin-1"), v.encode("latin-1")) for k, v in proxy_resp.headers.multi_items() if k.lower() not in excluded_headers]
            
            # 11. 최종 응답 생성
            # 마이크로서비스로부터 받은 결과(상태 코드, 내용, 헤더)를 클라이언트에게 그대로 돌려줍니다.
            response = Response(
                content=proxy_resp.content,
                status_code=proxy_resp.status_code,
                )
            response.raw_headers = response_headers
            return response
        except httpx.RequestError as exc:
            # 대상 서버가 죽어있거나 연결이 안 될 경우 502 에러를 던집니다.
            print(f"Proxy error: {exc}")
            raise HTTPException(status_code=502, detail="Bad Gateway")

# 12. 미들웨어 활성화
app.add_middleware(ReverseProxyMiddleware)