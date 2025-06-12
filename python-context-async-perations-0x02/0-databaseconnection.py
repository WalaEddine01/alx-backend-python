#!/usr/bin/python3
"""
"""
from mysql import connector
from os import getenv
from dotenv import load_dotenv


class DatabaseConnection():
    """
    """
    def __init__(self, user, password, database, host, port):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.port = port
    
    def __enter__(self):
        self.db_connection = connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )
        return self.db_connection

    def __exit__(self, exc_type, exc_value, traceback):
        self.db_connection.close()

if __name__ == '__main__':
    load_dotenv()
    host=getenv("MYSQL_HOST")
    port=getenv("MYSQL_PORT")
    user=getenv("MYSQL_USER")
    password=getenv("MYSQL_PASSWORD")
    database=getenv("MYSQL_DB")

    print(type(port))
    with DatabaseConnection(user, password, database, host, port) as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users")
        x = cursor.fetchall()
        print(x)