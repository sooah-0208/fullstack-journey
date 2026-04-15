from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.db import getConn

router = APIRouter(
    prefix="/board",
    tags=["게시글 조회"]
)

@router.get("")
@router.get("/")
async def get_posts():
    conn = getConn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM board ORDER BY id DESC")
    posts = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"status":True, "data": posts}

class PostUpdate(BaseModel):
    title: str
    content: str

@router.put("/{post_id}")
async def update_post(post_id: int, post: PostUpdate):
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute("UPDATE board SET title=%s, content=%s WHERE id=%s", (post.title, post.content, post_id))
    conn.commit()
    cursor.close()
    conn.close()
    return {"status": True, "message": "성공적으로 수정되었습니다."}

@router.delete("/{post_id}")
async def delete_post(post_id: int):
    conn = getConn()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM board WHERE id=%s", (post_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"status": True, "message": "성공적으로 삭제되었습니다."}