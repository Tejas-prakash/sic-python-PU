import pymysql

class Person:
    def __init__(self, name="", gender="", dob="", location=""):
        self.name       = name
        self.gender     = gender
        self.dob        = dob
        self.location   = location

    def __str__(self):
        return f'Name: {self.name}, Location: {self.location}, Gender: {self.gender}, Date of Birth: {self.dob}'

class Db_operations:
    def __init__(self):
        pass

    def connect_db(self):
        try:
            connection = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                password='Zoey@301105',
                database='db1',
                charset='utf8'
            )
            print('DB connected')
            return connection
        except pymysql.MySQLError as e:
            print(f"DB connection failed: {e}")
            return None

    def disconnect_db(self, connection):
        try:
            if connection:
                connection.close()
                print('DB dis-connected')
            else:
                print('No connection to close.')
        except pymysql.MySQLError as e:
            print(f"Error while disconnecting DB: {e}")

    def create_db(self):
        connection = self.connect_db()
        if connection is None:
            print("Cannot create database, connection failed.")
            return
        
        query = 'CREATE DATABASE IF NOT EXISTS nithin_db;'
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()
        print('DB created (if not exists)')
        self.disconnect_db(connection)

    def create_table(self):
        connection = self.connect_db()
        if connection is None:
            print("Cannot create table, connection failed.")
            return
        
        query = """CREATE TABLE IF NOT EXISTS persons (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    name VARCHAR(32) NOT NULL,
                    gender CHAR(1) CHECK (gender IN ('m', 'M', 'f', 'F')),
                    location VARCHAR(32),
                    dob DATE
                );"""
        cursor = connection.cursor()
        cursor.execute(query)
        cursor.close()
        print('Table created (if not exists)')
        self.disconnect_db(connection)

    def read_person_details(self):
        name = input('Enter person name: ')
        gender = input('Enter person gender (m/f): ')[0]
        location = input('Enter person location: ')
        dob = input('Enter person date of birth (yyyy-mm-dd): ')
        return (name, gender, location, dob)

    def insert_row(self, person):
        if not person:
            print("No person details provided.")
            return None

        query = 'INSERT INTO persons(name, gender, location, dob) VALUES (%s, %s, %s, %s);'
        person_tuple = (person.name, person.gender, person.location, person.dob)
        connection = self.connect_db()
        if connection is None:
            print("Cannot insert row, connection failed.")
            return None

        cursor = connection.cursor()
        cursor.execute(query, person_tuple)
        connection.commit()
        cursor.close()
        self.disconnect_db(connection)
        
        id = self.get_latest_row_id()
        return id

    def update_row(self, data):
        query = 'UPDATE persons SET name = %s, gender = %s, location = %s, dob = %s WHERE id = %s'
        connection = self.connect_db()
        if connection is None:
            print("Cannot update")
