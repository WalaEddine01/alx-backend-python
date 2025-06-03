#!/usr/bin/python3
from mysql import connector
from os import getenv
from dotenv import load_dotenv
from itertools import islice
load_dotenv()
import sys


def stream_users_in_batches(batch_size):
    """
     uses a generator to fetch rows one by one from the user_data table.
     must use the Yield python generator.
    """
    connection = connector.connect(
        host=getenv("MYSQL_HOST"),
        port=getenv("MYSQL_PORT"),
        user=getenv("MYSQL_USER"),
        password=getenv("MYSQL_PASSWORD"),
        database=getenv("MYSQL_DB")
    )
    cursor = connection.cursor()
    users = cursor.execute('SELECT * from user_data LIMIT %s', (batch_size, ))
    users = cursor.fetchall()
    for i in range(batch_size):
        user = {'user_id': users[i][0], 'name': users[i][1],
                'email': users[i][2], 'age': users[i][3]}

        print(user)
        yield user
    cursor.close()

def batch_processing(batch_size):
    """
    that processes each batch to filter users over the age of25
    """
    connection = connector.connect(
        host=getenv("MYSQL_HOST"),
        port=getenv("MYSQL_PORT"),
        user=getenv("MYSQL_USER"),
        password=getenv("MYSQL_PASSWORD"),
        database=getenv("MYSQL_DB")
    )
    cursor = connection.cursor()
    users = cursor.execute('SELECT * FROM user_data WHERE age > 25 LIMIT %s', (batch_size, ))
    users = cursor.fetchall()
    for i in range(batch_size):
        user = {'user_id': users[i][0], 'name': users[i][1],
                'email': users[i][2], 'age': users[i][3]}

        yield user
        return user
    cursor.close()


if __name__ == "__main__":
    try:
        stream_users_in_batches(50)
    except BrokenPipeError:
        sys.stderr.close()
