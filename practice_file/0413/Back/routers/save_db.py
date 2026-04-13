import ollama
from core.db import getConn
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(
    prefix="/db",
    tags=["DB저장"]
)

class UserInput(BaseModel):
    user_input: str

@router.post("/init")
async def db_init(request: UserInput):
    user_input = request.user_input
    system_context = """
   너는 MariaDB 전문가야. 사용자의 요구사항을 분석해서 SQL만 출력해.
    - 데이터베이스가 없으면: CREATE DATABASE IF NOT EXISTS [DB명];
    - 테이블이 없으면: USE [DB명]; CREATE TABLE IF NOT EXISTS [테이블명] (...);
    - 반드시 SQL 문장 끝에 세미콜론(;)을 붙여.
    - SQL 외의 설명(말대답)은 절대 하지 마.
    """
    try:
        response = ollama.chat(model='gemma4:e4b', messages=[
            {'role': 'system', 'content': system_context},
            {'role': 'user', 'content': user_input}])
        sql = response['message']['content']
        conn = getConn()
        clean_sql = sql.replace("```sql","").replace("```","").strip()
        cursor = conn.cursor()
        final_sqls = clean_sql.split(';')
        for final_sql in final_sqls:
            sql = final_sql.strip()
            if sql:
                print(sql)
                cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return {"status":True, "message":"DB저장에 성공했습니다."}
    except Exception as e:
        print(f"오류 발생 : {e}")
        return {"status": False, "message": str(e)}

@router.post("/insert")
async def db_insert(request: UserInput):
    user_input = request.user_input
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
        response = ollama.chat(model='gemma4:e4b', messages=[
            {'role': 'system', 'content': system_context},
            {'role': 'user', 'content': user_input}])
        sql = response['message']['content']
        conn = getConn()
        clean_sql = sql.replace("```sql","").replace("```","").strip()
        cursor = conn.cursor()
        final_sqls = clean_sql.split(';')
        for final_sql in final_sqls:
            sql = final_sql.strip()
            if sql:
                print(sql)
                cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()
        return {"status":True, "message":"게시글 수정에 성공했습니다."}
    except Exception as e:
        print(f"오류 발생 : {e}")
        return {"status": False, "message": str(e)}
           
