# 😯 코드가 너무 길어서 한 눈에 보기가 어려워요!
복잡한 구조일수록 코드가 길어져서 한번에 판독하기 어려움  
-> style만 따로 때어내서 `(파일명).css`로 새 파일을 파냄  
원본 파일에 `<link rel="stylesheet" href="index.css">`을 추가해줌  
f12 -> network를 열어 연결이 잘 되었는지 확인해줌

### 💦오류가 나요!!
css파일 url이 잘못되었을 경우 css가 불러와지지 않습니다.  
-> 폴더 위치가 올바른지 확인
-> 서로 다른 폴더에 위치해있다면 ../(폴더명)/index.css 처럼 위치를 잡아주어야함

### 💦바로바로 변경이 안돼요!
f12 누른 후 새로고침에 왼쪽클릭 -> 캐시 비우기 실행


# 연습할 때 ui짜기 귀찮아요!
bootstrap.com-> product example에서 틀 가져온 다음 원하는 대로 수정하면 됨

# 부트스트랩
미리 만들어진 ui 세트
class=""로 지정함

# 유틸리티 클래스
### 1️⃣ 여백 (Spacing)
기본 공식: (속성)(방향)-(숫자:0~5)
🔹 속성
m → margin  
p → padding  
🔹 방향
t → top  
b → bottom  
s → start (left)  
e → end (right)  
x → 좌우  
y → 상하  
**mx-auto** 가운데정렬(x좌우의 m마진을 auto자동으로 조절하겠음 이라서 가운데로 옴)
#### 예시
```
<div class="mt-3">위 여백</div>
<div class="mb-4">아래 여백</div>
<div class="px-2">좌우 패딩</div>
<div class="mx-auto">가운데 정렬</div>
```
### 2️⃣ Display
```
<div class="d-none">숨김</div>
<div class="d-block">블록</div>
<div class="d-inline">인라인</div>
<div class="d-flex">flex</div>
```
**반응형**
`<div class="d-none d-md-block">`

### 3️⃣ Flex 정렬 (진짜 많이 씀)
`justify-content-start`: 가로 시작  
`justify-content-center`: 가로 중앙  
`justify-content-between`: 양끝  
`align-items-center`: 세로 중앙  
```
<div class="d-flex justify-content-center align-items-center">
```
### 4️⃣ Width / Height
```
<div class="w-100">100%</div>
<div class="w-50">50%</div>
<div class="h-100">높이 100%</div>
```

### 5️⃣ Text
```<p class="text-center">가운데</p>
<p class="text-end">오른쪽</p>
<p class="fw-bold">굵게</p>
<p class="text-muted">연한 글자</p>
```

### 6️⃣ 색상
```
<div class="bg-primary text-white">Primary</div>
<div class="bg-danger">Danger</div>
<div class="text-success">Success</div>
```

### 7️⃣ Button
```
<button class="btn btn-primary">확인</button>
<button class="btn btn-outline-secondary">취소</button>
<button class="btn btn-sm btn-danger">삭제</button>
```

### 8️⃣ Form
```
<input class="form-control">
<select class="form-select"></select>
```

