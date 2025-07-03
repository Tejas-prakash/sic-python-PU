import pymysql
def connectiondb():
    connection= None
    try:
        connection=pymysql.connect(host='localhost',user='root',password='Zoey@301105',database='tejas_db',charset='upf8')
        print('Database connected')
    except:
        print("Database not connected")
    return connection
connectiondb()