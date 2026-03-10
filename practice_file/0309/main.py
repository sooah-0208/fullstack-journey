import mariadb
from fastapi import FastAPI

app = FastAPI()

conn_params = {
  "user": "root",
  "password": "1234",
  "host": "192.168.0.201",
  "database" : "db_air",
  "port" : int(3306)
}


def etlOne(year:int, month: int):
    print(f"db_air에서 db_to_air 비행 {year}년도 {month}월 데이터 이관 작업")
    try:
        conn = mariadb.connect(**conn_params)
        if conn:
            where = f"WHERE 년도 = {year} AND 월 = {month}"
            sql1 = f'DELETE FROM db_to_air.`비행` {where};'
            sql2 = f'''
            INSERT INTO db_to_air.`비행`
            SELECT * FROM db_air.`비행`
            {where};
            '''
            sql3 = f'SELECT COUNT(*) AS 적재 FROM db_to_air.`비행` {where}'
            cur = conn.cursor()
            cur.execute(sql1)
            cur.execute(sql2)
            conn.commit()
            cur.execute(sql3)
            row = cur.fetchone()
            print(f'적재: {row[0]}건')
            cur.close()
            conn.close()
    except mariadb.Error as e:
        print(f"MariaDB Error : {e}")

# key가 없는 경우는 delete를 하나 truncate를 하나 똑같아짐
# 여기서 delete하는 이유는? 완전 초기화 말고 년/월 별로 지울거라서

def etlAll(table:str, year:int = 0, month: int = 0):
    print(f"db_air에서 db_to_air 데이터 이관 작업")
    try:
        conn = mariadb.connect(**conn_params)
        if conn:
            where = ''
            if year > 0 and month > 0:
                where = f"WHERE 년도 = {year} AND 월 = {month}"
            delete = f'DELETE FROM db_to_air.`{table}` {where};'
            insert = f'INSERT INTO db_to_air.`{table}` SELECT * FROM db_air.`{table}` {where};'
            select = f'SELECT COUNT(*) AS 적재 FROM db_to_air.`{table}` {where}'
            cur = conn.cursor()
            cur.execute(delete)
            cur.execute(insert)
            conn.commit()
            # 혹시 모르니까 insert후에 commit 한번 해줌
            cur.execute(select)
            row = cur.fetchone()
            print(f'{table} 적재: {row[0]}건')
            cur.close()
            conn.close()
    except mariadb.Error as e:
        print(f"MariaDB Error : {e}")

def 운반대():
    print("db_air에서 db_to_air 운반대 데이터 이관 작업")
    try:
        conn = mariadb.connect(**conn_params)
        if conn:
            sql1 = 'TRUNCATE TABLE db_to_air.`운반대`;'
            sql2 = '''
            INSERT INTO db_to_air.`운반대`
            SELECT * FROM db_air.`운반대`;
            '''
            sql3 = 'SELECT COUNT(*) AS 적재 FROM db_to_air.`운반대`'
            cur = conn.cursor()
            cur.execute(sql1)
            cur.execute(sql2)
            conn.commit()
            cur.execute(sql3)
            row = cur.fetchone()
            print(f'적재: {row[0]}건')
            cur.close()
            conn.close()
    except mariadb.Error as e:
        print(f"MariaDB Error : {e}")

def 항공사():
    print("db_air에서 db_to_air 항공사 데이터 이관 작업")
    try:
        conn = mariadb.connect(**conn_params)
        if conn:
            sql1 = 'TRUNCATE TABLE db_to_air.`항공사`;'
            sql2 = '''
            INSERT INTO db_to_air.`항공사`
            SELECT * FROM db_air.`항공사`;
            '''
            sql3 = 'SELECT COUNT(*) AS 적재 FROM db_to_air.`항공사`'
            cur = conn.cursor()
            cur.execute(sql1)
            cur.execute(sql2)
            conn.commit()
            cur.execute(sql3)
            row = cur.fetchone()
            print(f'적재: {row[0]}건')
            cur.close()
            conn.close()
    except mariadb.Error as e:
        print(f"MariaDB Error : {e}")

@app.get("/")
def read():
  return {"status": True}

@app.post('/insert')
def etl3(data:list[dict]):
    print(f"db_air에서 db_to_air 데이터 이관 작업")
    try:
        conn = mariadb.connect(**conn_params)
        if conn:
            year = data['year']
            month = data['month']
            table = data['job_table']
            no = data['no']
            where = ''
            if year > 0 and month > 0:
                where = f"WHERE 년도 = {year} AND 월 = {month}"
            delete = f'DELETE FROM db_to_air.`{table}` {where};'
            insert = f'INSERT INTO db_to_air.`{table}` SELECT * FROM db_air.`{table}` {where};'
            select = f'SELECT COUNT(*) AS 적재 FROM db_to_air.`{table}` {where}'
            cur = conn.cursor()
            cur.execute(delete)
            cur.execute(insert)
            conn.commit()
            # 혹시 모르니까 insert후에 commit 한번 해줌
            cur.execute(select)
            row = cur.fetchone()
            print(f'{table} 적재: {row[0]}건')
            sql = f'update db_to_air.jobs set `cnt` = {row[0]}, `modDate` = now() where `no` = {no}'
            cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
            return data
    except mariadb.Error as e:
        print(f"MariaDB Error : {e}")

@app.post('/read')
def jobs(useYn = tuple):
    try:
        conn = mariadb.connect(**conn_params)
        if conn:
            if isinstance(useYn, (list, tuple)):
                keys = ",".join(map(str, useYn))
            else:
                keys = useYn
            sql = f'SELECT `no`,`job_table`,`year`,`month` FROM db_to_air.jobs WHERE useYn IN ({keys});'
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            cur.close()
            conn.close()
            result = [dict(zip(columns, row)) for row in rows]
            return result
    except mariadb.Error as e:
        print(f"MariaDB Error : {e}")
        return []


@app.post('/useYn')
def useYn(yn:int, table:str):
    try:
        conn = mariadb.connect(**conn_params)
        if conn:
            sql = f"update db_to_air.jobs set `useYn` = {yn} WHERE job_table = '{table}';"
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
            return {"status": "success", "message": f"{table} useYN {yn}업데이트 완료"}
    except mariadb.Error as e:
        print(f"MariaDB Error : {e}")

    
        
# if "__main__" == __name__:
#     useYn = tuple([0])
#     for row in jobs(useYn):
#         if row:
#             etl3(row)
            # etlAll(row['job_table'],row['year'],row['month'])
    # etlOne(1987, 10)
    # etlAll("비행",1987)
    # etlAll("비행",0,10)
    # etlAll("항공사")
    # etlAll("운반대")
    # 항공사()
    # 운반대()
