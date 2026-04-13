import mariadb

conn_params = {
  "user": "root",
  "password": "1234",
  "host": "192.168.0.201",
  "port" : int(3306)
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