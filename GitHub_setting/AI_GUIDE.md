# 🚀 Project Context & Rules

## 🛠 Tech Stack
- **Frontend:** React, TypeScript, Tailwind CSS, Vite
- **Backend:** Python 3.10+, FastAPI, SQLAlchemy (PostgreSQL)
- **State Management:** React Query (TanStack Query)

## 📁 Folder Structure Convention
- 모든 컴포넌트는 `src/components/[FeatureName]`에 위치한다.
- 비즈니스 로직과 API 호출은 `src/hooks` 또는 `src/api`에 분리한다.
- 백엔드 API는 `app/api/v1/endpoints`에 위치하며, 엔티티별로 파일을 나눈다.
- 데이터 모델은 `app/models`, 스키마(Pydantic)는 `app/schemas`를 사용한다.

## ✍️ Coding Standard
- **Naming:** 변수/함수는 camelCase(TS), snake_case(Py). 클래스는 PascalCase.
- **Component:** 함수형 컴포넌트(`export const ...`) 사용.
- **Error Handling:** - FE: 에러 발생 시 사용자 알림(Toast) 처리 로직 포함.
  - BE: `HTTPException`을 사용하여 명확한 상태 코드와 메시지 반환.
- **Git:** 커밋 메시지는 `feat:`, `fix:`, `refactor:` 등의 접두사를 붙인다.