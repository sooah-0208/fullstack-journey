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