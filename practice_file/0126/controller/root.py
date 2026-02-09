from fastapi import APIRouter
from configs.db import getConn
import mariadb

router = APIRouter(tags=['기본'], prefix='/root')

@router.get(path="/")
def root():
    try:
        conn = getConn()
        cur = conn.cunsor()
        sql = 'select 1 as no'
        cur.execute(sql)
        columns = [desc[0] for desc in cur.description]
        row = cur.fetchone()
        result = dict(zip(columns, row) if row else None)
        return {'status':True, 'result':result}
    except mariadb.Error as e:
        print(f'SQL 오류: {e}')
    return {'status': False}