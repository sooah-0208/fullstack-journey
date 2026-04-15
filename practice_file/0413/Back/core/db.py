from core.settings import settings
import mariadb

conn_params = {
  "user": settings.mariadb_user,
  "password": settings.mariadb_password,
  "host": settings.mariadb_host,
  "port" : settings.mariadb_port,
  "database": settings.mariadb_database
}

def getConn():
  try:
    conn = mariadb.connect(**conn_params)
    if conn == None:
      return None
    return conn
  except mariadb.Error as e:
    print(f"접속 오류 : {e}")
    return None