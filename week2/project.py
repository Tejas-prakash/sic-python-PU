import pymysql

def connectiondb():
    connection = None
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='Zoey@301105',
            database='db1',
            charset='utf8'   
        )
        print('Database connected')
    except pymysql.MySQLError as e:
        print("Database not connected")
        print(f"Error: {e}")
    return connection

connectiondb()
     