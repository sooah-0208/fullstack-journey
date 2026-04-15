from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.db import getConn

router = APIRouter(
    prefix="/board",
    tags=["게시글 조회"]
)

@router.get("/")
async def get_posts():
    conn = getConn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM board ORDER BY id DESC")
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"status":True, "data": posts}