from fastapi import APIRouter
from configs.db import getConn
import mariadb

router = APIRouter(tags=['사용자'], prefix='/user')

@router.get(path='',
            summary='사용자 목록',
            description='edu.userinfo 테이블 가져오기')
def user():
    try:
        conn = getConn()
        cur = conn.cursor()
        sql = 'select * from edu.userinfo'
        cur.execute(sql)
        columns = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
        result = [dict(zip(columns,row)) for row in rows]
        return {'status':True, 'result':result}
    except mariadb.Error as e:
        print(f'SQL 오류: {e}')
    return {'status': False}


@router.post(path="")
def post_root():
    return {"method": "POST"}

@router.put(path="")
def put_root():
    return {"method": "PUT"}

@router.delete(path="")
def delete_root():
    return {"method": "DELETE"}

@router.patch(path="")
def patch_root():
    return {"method": "PATCH"}