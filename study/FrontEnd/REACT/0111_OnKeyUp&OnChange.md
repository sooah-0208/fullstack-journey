# onKeyUp과 onChange 차이

## ✔ onKeyUp

- 키보드에서 키를 눌렀다가 **뗐을 때** 실행되는 이벤트
- **키보드로 입력한 순간만 감지**
- 마우스 붙여넣기, 자동완성, 음성인식 처리 불가
```
const onKeyUp = (e) => {
  setSearch(e.target.value);
};
```
👉이런 식으로 실시간 인식도 가능함

## 그럼 onKeyUp은 언제 쓰나요?
### 🔹 Enter 키 감지
- 검색창, 로그인, 전송 버튼 등 엔터 눌러야 값 보낼 때
```
onKeyUp={(e) => {
  if (e.key === "Enter") {
    searchSubmit();
  }
}}
```
### 🔹 단축키 만들기(특정 키 조합 처리)
```
onKeyUp={(e) => {
  if (e.ctrlKey && e.key === "s") {
    console.log("저장!");           //실제 파일에 저장하는 코드 넣어주면 됨
  }
}}
```

### onKey관련 매서드
키 누름 → onKeyDown
키 누르고 있음 → onKeyPress (요즘 잘 안 씀)
키 뗌 → onKeyUp ✅

### 자주 쓰는 값
- `e.key`: 실제 입력된 키 (Enter, a, 1 등)
- `e.code`: 키보드 위치 (KeyA, Enter) 👉 키보드 하드웨어(레이아웃)를 기준으로 브라우저가 정해둔 값


----

## ✔ onChange (React)

- 값이 바뀌면 무조건 실행
- 검색 필터링, 실시간 입력 처리엔 onChange가 더 적합
