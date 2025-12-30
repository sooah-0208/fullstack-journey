# 🔗 GitHub ↔ VS Code 연결하기

## 1️⃣ GitHub에서 할 일

### 📁 1. Repository 생성
- GitHub에서 새로운 **Repository** 제작

### 🐞 2. Issue 생성
- 해당 Repository에서 **Issues** 생성

### 🌱 3. Issue에서 브랜치 생성
- Issue 화면의 **Development** 영역
- `Create branch` 클릭
- 👉 생성된 브랜치는 **해당 Issue와 자동 연결됨**

---

## 2️⃣ VS Code로 이동 💻

### 📂 1. 폴더 생성
- 작업할 폴더 생성
- ⚠️ **폴더 안에 repo 이름과 같은 파일 생성**

---

### 🖥️ 2. 터미널 열기 & Repository 가져오기 (clone)
- 해당 폴더에서 **터미널 열기**
- 아래 명령어 입력 👇
- 명령어는 <>code누르면 복붙할 수 있게 뜸
`git clone https://github.com/TeamChoiKim/20251230T2.git`


### 🛠 react 실행하기
`npm create vite 파일명`  
*대문자는 사용 안됨!!!!  
이걸로 넘겨서 react 실행하면 댐~~

## 3️⃣ 신규 브랜치 연결하기 🌿
### 🔄 1. 원격 브랜치 정보 가져오기
```
git fetch origin
git checkout 신규브런치이름
```

한번에 두줄 다 입력해도 됨

## 4️⃣ 브랜치 연결 확인 방법 ✅
`git branch`
* 표시가 되어 있고 색이 들어온 브랜치가
👉 현재 연결된 브랜치

## 5️⃣ 작업 완료 후 다른 브랜치로 이동 🔀
`git checkout [이동할브랜치명]`
- 예시
  - main
  - develop
  - 다른 issue 브랜치


## 6️⃣ 작업 확인하는 방법 ✅
1. 내가 수정한 사항이 있을 때 파일 올리기
```
git add .
git commit -m "커밋설명"
git push
```
위 코드 하나씩 입력하면 push 됨
2. 상대가 수정한 파일 받기
상대 branch로 이동 후
`git pull`


## ⭐ 업데이트 항목 코드
<img width="659" height="263" alt="image" src="https://github.com/user-attachments/assets/0be6d573-b305-4300-ad8a-2a781384de3a" />


# Router
## 1️⃣ 라우터(Router)의 역할
SPA(Single Page Application)  
즉 한 페이지 안에서 모든 화면이 바뀌는 구조
-URL이 바뀌어도 페이지 전체를 새로고침하지 않고, 컴포넌트만 바꿔서 보여주는 것이 라우터의 핵심 역할

- `/` → 메인 페이지 보여주기
- `/about` → 소개 페이지 보여주기
- `/contact` → 연락처 페이지 보여주기

### 💾설치명령어
```
npm i react-router
```

### 🖥Router 설정 내용
```
import React from "react";
import ReactDOM from "react-dom/client";
import { createBrowserRouter } from "react-router";
import { RouterProvider } from "react-router/dom";

const router = createBrowserRouter([      //React Router에서 제공하는 함수
  {
    path: "/",
    element: <div>Hello World</div>,
  },
]);

const root = document.getElementById("root");

ReactDOM.createRoot(root).render(
  <RouterProvider router={router} />,
);
```