import os
import mariadb
from setting import settings

conn_params ={
  'user':settings.mariadb_user,
  'password':settings.mariadb_password,
  'host':settings.mariadb_host,
  'database':settings.mariadb_database,
  'port':settings.mariadb_port
}

def getConn():
  try:
    return mariadb.connect(**conn_params)
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
