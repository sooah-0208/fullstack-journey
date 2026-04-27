import mariadb

# ------------------
# 연결방식1
# ------------------
settings.mariadbUrl="mariadb://root:1234@aiedu.tplinkdns.com/edu" #env 관리

def getConn():
  try:
    with mariadb.connect(settings.mariadbUrl) as conn:
      if conn == None:
        return None
      return conn
  except mariadb.Error as e:
    print(f"접속 오류 : {e}")
    return None
  
# ------------------
# 연결방식2
# ------------------

# env 관리
conn_params = {
  "user": "root",
  "password": "1234",
  "host": "aiedu.tplinkdns.com",
  "database" : "edu",
  "port" : int(55306)
}

def getConn():
  try:
    with mariadb.connect(**conn_params) as conn:
      if conn == None:
        return None
      return conn
  except mariadb.Error as e:
    print(f"접속 오류 : {e}")
    return None


# ------------------
# 연결방식3 SQLAlchemy
# ------------------
from sqlalchemy import create_password_url, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
