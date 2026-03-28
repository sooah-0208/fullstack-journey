import os
import mariadb
# from dotenv import load_dotenv
# load_dotenv()

# conn_params = {
#   'user': 'team2',
#   'password': 'team2',
#   'host': 'db.quadecologics.cloud',
#   'post': 5050,
#   'database':'team2'
# }

def getConn():
  try:
    return mariadb.connect(
      user='team2',
      password='team2',
      host='db.quadecologics.cloud',
      port=5050,
      database='team2'
    )
  except mariadb.Error as e:
    print(f"MariaDB Error : {e}")
    return None
  
def findOne(sql):
  result = None
  try:
    conn = getConn()
    if conn:
      cur = conn.cursor()
      cur.execute(sql)
      row = cur.fetchone() 
      columns = [desc[0] for desc in cur.description]
      cur.close()
      conn.close()
      result = dict(zip(columns, row)) if row else None
  except mariadb.Error as e:
    print(f"MariaDB Error : {e}")
  return result
  
def findAll(sql):
  result = []
  try:
    conn = getConn()
    if conn:
      cur = conn.cursor()
      cur.execute(sql)
      rows = cur.fetchall() 
      columns = [desc[0] for desc in cur.description]
      cur.close()
      conn.close()
      result = [dict(zip(columns, row)) for row in rows]
  except mariadb.Error as e:
    print(f"MariaDB Error : {e}")
  return result

def save(sql):
  result = False
  try:
    conn = getConn()
    if conn:
      cur = conn.cursor()
      cur.execute(sql)
      conn.commit()
      cur.close()
      conn.close()
      result = True
  except mariadb.Error as e:
    print(f"MariaDB Error : {e}")
  return result
