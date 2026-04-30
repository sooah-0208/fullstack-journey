0423(목)
# 로직설계

로직 담당을 어케 나눌지는 비즈니스 로직 설계 후 결정

## 회원가입(하면 바로 로그인) *Only ESG 담당자 가입루트*
- input 값 DB 저장
    순서대로 USER T, COMPANY T, USER_ROLE T, FILE T(임의지정) => apis/auth.py
- 이메일 / 사업자번호 중복확인
    인증버튼 클릭시, 이메일 - USER T, 사업자번호 - COMPANY T
- 로그인 함수 실행


## 로그인
공통
- email, pwd 값 있는지 검증(USER T)
- 토큰 발행(값은 하위에 따로 분류)
    1) Refresh Token 만료 검증(TOKEN T - user_id)
    2) Access Token 발행
    3) Redis에 DB0 = {key: uuid, value: access token}, DB1 = {key: uuid, value: USER_ROLE 컨설턴트가 셀렉한 회사 but 일반 유저도 USER_ROLE 저장} 저장 
    4) 로그인 성공 응답
        {status: True, data: {uuid:"", datas}}
        data: 논의 후 결정 @x2bjvhmmwg-gif 

### 최종결정
Req
Res

## 초대받고 첫 로그인(회원가입)
- 메일 발송 시 
1. INVITE T - * 저장
2. Redis에 issuepull권한, role_id 저장
2. 링크 토큰에 INVITE T - id 정보 저장하여 발송

- 임시 비밀번호로 로그인
- input 값(이름, 비번) + 토큰에서 읽은 값 DB 저장
    순서대로 USER T, USER_ROLE T => apis/auth.py
- 공통
- 회원정보 수정


**수정사항**
4) 이전 key: uuid 쿠키 발행 로직 삭제
: 로그인 상태확인용인데 http only: true 하면 front에서 쿠키 존재를 모름 -> 발행 필요성 X -> 상호 합의 후 성공 응답에 uuid 주는 방향으로 결정

+) 추후 보안성 업그레이드 요소: 디도스 방어 -> 블랙리스트 작성

쿠키 백에서 생성시
장 - front에서 uuid 보관 안 해도 됨, 상태값만 가지면 됨
단 - 유효기간이 access token이랑 다름 -> refresh token이랑 같은 유효기간 설정 issue
   - access token 발급시마다(로그인시) 수정 필요함 -> 토큰 관리가 번거로움 

프론트에서 생성시(header에 보냄)
장 - 관리 측면에서 간단함
단 - 크게 없음


## 회원 정보 관리
수정 창 진입
- Redis에서 uuid 검증
- Data 전달
    USER T - * 
    담당자면 COMPANY T - * 추가 전달

수정 버튼 클릭
- input data DB 저장
    USER T 
    담당자면 COMPANY T

탈퇴
- Redis에서 uuid 검증
- delete_yn 1

- 비밀번호 2차 확인
    수정창 진입시 or 탈퇴시 (front와 논의 필요: @)

## 비번 찾기

## 초대

## ACCESS TOKEN에 넣을 정보
- 권한식별 USER_ROLE T 의 company_id, role_id
- 사용자 정보 

## Access Token 만료 로직

---

## 로그 생성 규칙
Gateway에서 생성
request_id => 브라우저마다 고정해야함(ip)

"timestamp": datetime.utcnow().isoformat(),
            "level": level,
            "request_id": request_id,
            "user_id": request.state.user_uuid,
            "endpoint": request.url.path,
            "method": request.method,
            "message": "Request processed",
            "error": None,
            "status_code": response.status_code,
            "client_ip": request.client.host,
            "latency": latency

----

# 공통 Response 구조
✅ 성공 응답
{
 "status": true,
 "data": {},
 "message": null,
}
❌ 실패 응답
{
 "status": false,
 "code": "AUTH_001",
 "message": "Invalid access token",
}

응답에서 request_id가 필요가 없음
=> front에서 respones가 와서 back에서 로그에 쌓아야 함

----------

### 0424

# GateWay 할
java로 결정
## G.W Trouble shooting
각 팀 개별로 관리할 경우 같은 코드가 4번 들어감 -> 공통으로 하나로 묶을 경우 로그 관리가 쉬워짐 + 공통부분 제작 후 리뷰 작업 진행하기 때문에 각 팀에서 하는 것과 같음 => 최종으로 java G.W로 픽스함

# 협력사 가입
초대장 발송(초대 보낸 기업 키가 필요) -> 회원가입창으로 보냄 이때 회원가입창에는 depts, 초대회사, 받는회사 필요(front)
## 자동화 실패 Trouble shooting
휴먼에러 - 해당 링크로 들어왔는데 어? 복잡하네 나중에 할래 -> url로 따로 접속하면 위의 정보가 없음.
=> 자동 불가.
초대 로그기록에서 체결 승인/거절 가능은 함.
초대 보낼 때 기업대표메일로 보내지 않을 경우 입력창을 다시 관리해야함.

협력사를 가입시키는 것
-> 플랫폼에서 관리하지 않을 부분이라 생각
가입시키고 메일 공유는 회사간에서 해결.
이후 가입한 메일에 초대 하면 이부분은 메일발송(only승락해달라는 알람만) or 알림창에 띄워줌.

----

# 0428

## TrobleShooting

1) 주석
```
# --------------------------
# 컨슈머 시작
# --------------------------
def startConsumer():
    """컨슈머 시작 함수"""
    emailThread = threading.Thread(target=runEmailConsumer, daemon=True)
    emailThread.start() # 추가주석 있을 시
```
- 가독성을 위하여 주석 ---로 구분
- utils에서 함수 추출사용시 함수 설명 확인 위해 """컨슈머 시작 함수""" 포함

----

- savefile
회원가입시 // 사업자등록증 front에서 물고있다가 가입할 때 저장이 안됨 지금
OCR을 백에서 해야해서
그럼 redis에 임시저장을 할지, db에 임시저장 테이블을 파고 삭제하는 로직을 짤지
=> 임시저장 x, file에 무조건 저장, 삭제 안 함 -> 
**Troble Shooting**
- OCR 로직이 front 담당에서 back으로 넘어옴 -> 파일을 저장해야만 OCR이 가능 -> DB에 임시저장 테이블을 만들지 저장하고 삭제할지, 쭉 쌓을지 논의 -> 사용자 정보는 최대한 미삭제하는 쪽으로 협의, 쭉 쌓는 방향으로 fix함 ->
COMPANY T에 회원가입 될 테니 그걸로 조회하면 됨
(미사용 파일을 스케줄돌려서 특정 기간 지나면 지우는 로직 세울수 있고, 아니면 압축해서 백업할 수 있음)
이 부분은 추후 고도화를 할지, 바로 실행할지 고려사항

---

- token 생성시 
uuid를 내부에 생성함 -> uuid를 accesse token생성시 생성 -> redis key로 사용 -> db에 redis uuid 저장 => access_token만들때마다 uuid 업데이트 하기로함 그럼 db에 어케 저장? -> redis에 access_token, uuid 저장
**Troble Shooting**
JWE, 알고리즘: AES256-GCM(A256GCM)
2. 왜 AES-GCM을 사용할까? (발표용 핵심 이유)
기밀성과 무결성 동시 보장: 데이터를 숨기는 것(Encryption)뿐만 아니라, 누군가 데이터를 미세하게 수정했는지(Integrity)를 암호학적으로 즉시 판별할 수 있습니다.

표준 보안: Google, Cloudflare 등 글로벌 기술 기업들이 표준으로 사용하는 가장 안전하고 빠른 대칭키 암호화 방식입니다.
효율성: 하드웨어 가속 기능을 활용할 수 있어, 암/복호화 과정에서 서버 부하가 매우 적습니다.

---

- db.py에 
1. findOne, findAll, save, saveMany, add_key, exists, 페이지네이션 이렇게 있는데 더 필요한게 있는지?
2. 테스트 sql문 예시로 내가 써둬야하는지
**Troble Shooting**
1. url연결방식(mariadb.connect(settings.maria_db_url))은 mariadb에서 읽지 못하여 기존방식(conn_parmas)선정
2. with 사용시 블록 끝나면 바로 세션 종료가 됨 -> 현재는 각 함수에서 conn연결을 하지 않고 함수화하였기때문에 getConn()에서 with 사용하지 않기로 함

---

- redis
1. redis에 담을 key value fix
2. token만들건지, 받을건지
만약 만든다면 BaseModel fix
3. redis 사용을 어디어디 할지

---

- kafka
email 쓸 때 uuid 생성을 해야하는지, redis&token 
메일 4가지 fastapi로 보내는거 config 이 폴더에 둘건지 나눌지
kafka 순서: pd, cs // redis저장이 우선, redis uuid 읽어옴 
cs 요청 들어올 경우 redis key: uuid 읽어서 email보낸다?

---
---

# 0429
**Troble shooting**
- `models/auth.py`, `apis/auth.py` 로직 확정안
1) `models/auth.py` return 값을 only boolen만 주는 경우  
2) `models/auth.py`에 모든 생성로직을 넣고 `apis/auth.py`에는 결과값만 반환
1안을 선택할 경우  
sql문이 들어가는 로직 -> models/  
그 외의 생성로직 -> apis/  
2안을 선택할 경우 
모든 생성로직, DB 찍고오는 로직 -> models/
models/에서 만든 함수만 작성 -> apis/

- router list 추가 자동화로직 추가
현재 apis/에 py가 여러개있는데 거기서 라우터를 생성할 때 마다 수동으로 list에 include.router를 해줘야함  
이걸 자동화하는 로직 생성  
파일위치: `backend/src/apis/fastset.py`의 for문으로 생성함.  

- 로그인 로직 순서 변경
원래 redis 저장->front전달->db저장 순이었음  
이 로직을 쓸 경우 redis에는 저장되었으나 db저장시 오류가 나는 경우 생길 수 있음  
=> db저장 후 redis -> front로 전달하는 순서로 변경함
+) 추가적인 수정사항  
try문 사용하여 둘중에 하나만 저장될 경우를 막음. 둘중에 하나라도 실패하면 다 실패응답주도록 + 트랜젝션 롤백처리

- 공통 Response 구조 수정
Discussion # 29 참고  
1. request_id 삭제
응답에서 request_id가 필요가 없음    
=> front에서 respones가 와서 back에서 로그에 쌓아야 함  
2. 실패응답 status만 전달  
로그에 찍히는 code가 실패응답과는 관련이 없어 단순 성공/실패 여부만 전달함  

- token claim 규정
현재 커스텀으로 iss, sub 없이 하고있었음  
규정 확인 후 iss는 생략한 특별한 이유가 없기에 `withProject`로 추가하기로 함.
규정은 
- `iss` (Issuer): 토큰 발급자
- `sub` (Subject): 토큰 제목 (사용자 ID 등)
- `aud` (Audience): 토큰 대상자
- `exp` (Expiration): 토큰 만료 시간
- `iat` (Issued At): 토큰 발급 시간
가 기본적으로 들어가야함
왜 커스텀했는지? => aud는 이용자가 권한이 바뀔 수 있어서 값을 정하지 않음 -> WHY? accessToken이 있는 와중에 권한 변경이 일어나면 권한 변경점이 저장이 안됨  

## FRONT 로그인 요청사항

로그인하면 회사선택페이지로 이동(이부분을 프론트에서 체크) -> 온보딩에서 권한 체크

첫 로그인할때 front에서 필요한 정보

uuid
COMPANY T company_name
USER T email
USER_ROLE role_id

+ 회사 선택시마다 API 요청 필요
내가 가진 권한 체크해줘야함(USER_ROLE 전체)

---
# 0430

**Troble Shooting**
- 비밀번호 찾기 인증절차(미확정입니다ㅜㅜ)  
pass와 같은 공인인증이 불가하기 때문에 단순히 메일을 입력하여 임시비번 발급 -> DB password Update    
이 경우 이메일을 아는 타인이 비밀번호 찾기를 신청할 경우 기존 사용자가 본인의 계정으로 로그인 할 수 없는 경우 발생    
-> redis에 임시비밀번호를 저장, 유효기간 1시간 -> 회원 수정에서 비번 교체할 경우에만 Update 되도록 함

- 2차인증
회원정보 수정등의 상황에 보안 상향을 위하여 2차인증 기능을 추가함  
auth.py중 /patch: 비밀번호 확인 EndPoint 추가

- OCR
pororo : 설치 과정중 오류
paddle : 설치 과정중 오류
surya : 설치 과정중 오류
Doctr : 한글을 인식 못하고 깨짐
EasyOcr: 한글을 인식 하지만 정확도가 낮음
Tesseract :  exe파일을 설치해야함
google-vision-cloud : 외부 api인데 추가 설치가 필요함, api-key 파일을 요구함. 한달에 1천건 무료
tesseract : exe파일 설치 요구
유료 버전들 (일정 건수만 무료제공) 아니면 대부분 설치중 오류 혹은 한글 인식률이 떨어짐
NAVER OCR : api url, secretkey 발급필요, 한달에 300건 무료 

원인 분석

pororo : 계속 추가 라이브러리 설치를 요구 + 파이썬 버전과 연동이 안됨
paddle : 계속 추가 라이브러리 설치를 요구 + 파이썬 버전과 연동이 안됨
surya : 설치를 해도 인식을 못함 
Doctr: 분석언어에 영어만 있어서 한글을 인식 못함
tesseract : 다른 컴퓨터 마다 exe 파일을 깃허브에서 컴퓨터 마다 받아야함
google-vision-cloud : 라이브러리 설치, api-url, api-key 등 공식사이트에서 발급받아야 함
NaverOCR : 라이브러리 설치, api-url, api-key 등 공식사이트에서 발급받아야 함


해결 단계
1.pororo: 설치를 하여도 계속 오류 발생으로 사용 안하기로 결정
2. paddle : 설치를 하여도 계속 오류 발생으로 사용 안하기로 결정
3. surya : 설치를 하여도 계속 오류 발생으로 사용 안하기로 결정
4. Doctr : 인식언어에 한글추가, 하지만 인식을 못하고 언어가 깨짐
5. tesseract : exe파일을 사용하는 컴퓨터 마다 받아야 하니 사용 안하기로 결정
6. google-vision-cloud : 라이브러리 설치, api-url, api-key 등 공식사이트에서 발급받은뒤 필요한 부분에 추가 완료
7. NaverOCR : api-url, api-key 등 공식사이트에서 발급받은뒤 필요한 부분에 추가 완료


## 일정픽스
4/30
- 회원정보관리
- 회원가입
- OCR 파싱
- 비밀번호 찾기 메일 발송

5/1
- 로그확인 페이지 연결
- 초대 로직(권한설정, 초대 취소 등)

5/4
- 메인게시판

**0504**
- 페이지별 엔드포인트 작성
  - [ ] 대시보드
  - [ ] 데이터입력(온보딩)

5/6
- 알람기능

5/7
- front 연결까지 최종확인
