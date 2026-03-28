import mariadb


conn_params = {
  "user": "root",
  "password": "1234",
  "host": "192.168.0.201",
  "database" : "db_air",
  "port" : int(3306)
}

def main():
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


if __name__ == "__main__":
    main()
