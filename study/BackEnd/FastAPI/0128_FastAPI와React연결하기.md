[코드 참조 -study18](https://github.com/ESG-EDU/STUDY_FILES/tree/fastapi)


## axios

한 프로젝트에 backend, frontend 제작

양쪽 모듈 설치 후 run dev -> 포트가 다른 두가지 확인하기

axios 설치(백과 프론트 합쳐주는 모듈)
`npm install axios`

```
const Home = () => {
  const btn1Event = () =>{
    console.log('btn1 호출')
    axios.get('http://localhose:8000/')// '/'만 쓰면 react포트로 연결해줌, 그래서 fastapi링크 작성
    .then(res => console.log(res))   // 필수. respone을 받아오고싶을때
    .catch(err=>console.log(err))    // 통신(네트워크) 에러 잡으면 실행하고싶을 때(데이터에러는 then에 옴) 
    .finally(()=>console.log('완료')) // 성공하든 실패하든 일단 실행시키고싶을때, 필수는 아님
  }
```

## origins, Middleware

포트를 동시에 두가지 열면 기본적으로 차단시켜버림(해킹 위험성이 있어서) -> 요청 받은 fastapi쪽에서 이 차단항목을 오픈해줘야함

[오픈관련링크](https://fastapi.tiangolo.com/tutorial/cors/?h=cors#use-corsmiddleware)

```
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:5173"] #프로젝트랑 관련한 링크만 열어줘야함. 아니면 해킹당해여~
app = FastAPI()
app.add_middleware(       #app에 이 설정을 추가해주겠다
    CORSMiddleware,         #보안설정
    allow_origins=origins,  #origins에 들어간 링크로 오는 요청만 허용
    allow_credentials=True,
    allow_methods=["*"],    # 모든 http 메소드 허용(get, post, delete, put 등. *대신 얘네 넣으면 넣은 것만 허용)
    allow_headers=["*"],    # 모든 헤더 허용, 개발중엔 보통 다 허용함 req,res에 딸려오는 모든 부가정보를 헤더라고 함
)
```
CORS Origin는 url이 아님. Origin만의 규칙을 따름
`scheme + host + port`만 포함
❌ 포함 안 되는 것:
- path (/, /api)
- query
- fragment

## 쿠키로 정보 받아오기
```Login.jsx
//“백엔드(FastAPI)랑 통신할 기본 세팅을 미리 만들어두는 axios 인스턴스
const api = axios.create({ //axios설정을 api라는 변수에 넣음 각 method마다 아래 내용 안 넣게 하기위해
  baseURL: "http://localhost:8000", //api.post에 일일히 넣지 않기 위해 base로 깔아둠
  withCredentials: true, //쿠키를 주고받을것이냐 True
  headers: {
    "Content-Type": "application/json",
  },
})
```
``` main.py
@app.post("/login")
def login(loginModel: LoginModel, response: Response):
  response.set_cookie(
    key="user",
    value=loginModel.email,
    max_age=60 * 60,        # 1시간 (초)
    expires=60 * 60,        # max_age와 유사 (초)
    path="/",
    domain="localhost",
    secure=True,            # HTTPS에서만 전송
    httponly=True,          # JS 접근 차단 (⭐ 보안 중요)
    samesite="lax",         # 'lax' | 'strict' | 'none'
  )
  return {"status": True, "model": loginModel}
```

http로 정보를 주고받으면 보안상 위험함. 정보가 암호화 되지 않아서 인터셉트 가능함
but! front에서는 httponly에 True넣어둬서 안 보임 -> False로 바꾸면 프론트에서도 보임
=> 이렇게 막아두면 정보를 백만 가지고있어서 매번 맥에서 확인해줘야함

## useContext

전체 전역변수
컴포넌트 최상위에 호출해서 필요한 위치마다 사용할 수 있게 해줌
props는 함수마다 넣어줘야하는데 그 번거로움을 줄여줌

```
import { createContext } from 'react';

export const AuthContext = createContext(null);
```

AuthContext라는 이름으로 전역변수를 설정해줌
`null`은 Context의 기본값 -> Provider를 못 찾으면 일단 아직 없다는 의미로 null을 넣어줌
기본값을 객체로 넣어두게되면 Provider가 없어도 에러가 안 나서 Provider 없는 경우의 버그를 읽어낼 수 없음

메인으로 쓰는 페이지에서
```
  return (
    <AuthContext.Provider value={{ isLogin, setIsLogin }}> 
    {/* 이 벨류가 전역변수 */}
      <Nav />
      <BrowserRouter>
        <Routes>
          { paths?.map((v, i) => <Route key={i} path={v.path} element={v.element} />) }
        </Routes>
      </BrowserRouter>
    </AuthContext.Provider> //전역변수 허용할 범위, 안 쓸 애들은 이 밖으로 빼주면 됨
  )
```

AuthContext.Provider로 묶어줘야만 전역변수를 사용할 수 있음
전역변수가 필요없는 항목은 밖에 빼줘도 괜찮음


## API로 파일 업로드/다운로드
업로드는 무조건 post
다운로드는 get 가능하나 로그인 해서 다운하는 경우 post사용(아무나 받아가면 안되니까)

