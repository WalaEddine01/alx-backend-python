#!/usr/bin/python3
from mysql import connector
from os import getenv
from dotenv import load_dotenv
from itertools import islice


load_dotenv()
def stream_users():
    """
    """
    connection = connector.connect(
        host=getenv("MYSQL_HOST"),
        port=getenv("MYSQL_PORT"),
        user=getenv("MYSQL_USER"),
        password=getenv("MYSQL_PASSWORD"),
        database=getenv("MYSQL_DB")
    )
    cursor = connection.cursor()
    users = cursor.execute('SELECT * from user_data')
    users = cursor.fetchall()
    for user in users:
        user = {'user_id': user[0], 'name': user[1], 'email': user[2], 'age': user[3]}
        
        yield user
    cursor.close()


if __name__ == "__main__":
    stream_users()
    for user in islice(stream_users(), 6):
        print(user)
