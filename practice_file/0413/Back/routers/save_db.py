from core.settings import settings
# from ollama import Client
from core.db import getConn
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from langchain_ollama import ChatOllama


router = APIRouter(
    prefix="/db",
    tags=["DB저장"]
)

class UserInput(BaseModel):
    user_input: str

llm = ChatOllama(
  model=settings.ollama_model_name,
  base_url=settings.ollama_base_url,
)

def execute_sql_from_llm(sql_text: str):
    """LLM이 생성한 SQL 텍스트를 정제하고 실행하는 공통 함수"""
    # 마크다운 태그 제거 및 공백 정제
    clean_sql = sql_text.replace("```sql", "").replace("```", "").strip()
    
    conn = getConn()
    try:
        cursor = conn.cursor()
        final_sqls = clean_sql.split(';')
        for final_sql in final_sqls:
            sql = final_sql.strip()
            if sql:
                print(f"Executing: {sql}")
                cursor.execute(sql)
        conn.commit()
    finally:
        cursor.close()
        conn.close()

@router.post("/init")
async def db_init(request: UserInput):
    system_context = """
   너는 MariaDB 전문가야. 사용자의 요구사항을 분석해서 SQL만 출력해.
    - 사용자 입력값에 DB명이 있으면: CREATE DATABASE IF NOT EXISTS [DB명];
    - 사용자 입력값에 테이블명이 있으면: USE [DB명]; CREATE TABLE IF NOT EXISTS [테이블명] (...);
    - 반드시 SQL 문장 끝에 세미콜론(;)을 붙여.
    - SQL 외의 설명(말대답)은 절대 하지 마.
    """
    try:
        messages = [
            ("system", system_context),
            ("user", request.user_input),
        ]
        response = llm.invoke(messages)
        sql = response.content
        execute_sql_from_llm(sql)
        
        return {"status": True, "message": "DB저장에 성공했습니다. ✅"}
    except Exception as e:
        print(f"오류 발생 : {e}")
        return {"status": False, "message": str(e)}
    #     conn = getConn()
    #     clean_sql = sql.replace("```sql","").replace("```","").strip()
    #     cursor = conn.cursor()
    #     final_sqls = clean_sql.split(';')
    #     for final_sql in final_sqls:
    #         sql = final_sql.strip()
    #         if sql:
    #             print(sql)
    #             cursor.execute(sql)
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    #     return {"status":True, "message":"DB저장에 성공했습니다."}
    # except Exception as e:
    #     print(f"오류 발생 : {e}")
    #     return {"status": False, "message": str(e)}

@router.post("/insert")
async def db_insert(request: UserInput):
    system_context = """
    너는 MariaDB 데이터 조작 전문가야. 
    대상 데이터베이스: sooah_board
    대상 테이블: board (컬럼: id, title, user_name, content)

    작업 규칙:
    1. 사용자의 요청을 분석해서 INSERT, UPDATE, DELETE 중 적절한 SQL만 생성해.
    2. 모든 문장 시작 전에 'USE sooah_board;'를 반드시 포함해.
    3. 문장 끝에는 세미콜론(;)을 붙여.
    4. SQL 외의 설명은 절대 하지 마.
    
    예시:
    - 입력: "홍길동이 '하이'라는 제목으로 안녕 얘들아라고 글 써줘" 
      출력: USE sooah_board; INSERT INTO board (user_name, title, content) VALUES ('홍길동', '하이', '안녕 얘들아');
    - 입력: "1번 글 제목을 '수정됨'으로 바꿔줘"
      출력: USE sooah_board; UPDATE board SET title='수정됨' WHERE id=1;
    """
    try:
        messages = [
            ("system", system_context),
            ("user", request.user_input),
        ]
        response = llm.invoke(messages)
        sql = response.content
        check_keywords = ['INSERT', 'UPDATE', 'DELETE']
        if not any(keyword in sql.upper() for keyword in check_keywords):
            return {"status": False, "message": "아 나한테는 좀 어렵다구리. 이렇게 써달라구리. \n (예: 제목, 내용, 작성자 포함)"}
        execute_sql_from_llm(sql)                    
        return {"status":True, "message":"아 성공이다구리구리~~!~!"}
    except Exception as e:
        print(f"오류 발생 : {e}")
        return {"status": False, "message": str(e)}
           
