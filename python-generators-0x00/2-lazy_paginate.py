#!/usr/bin/python3
from mysql import connector
from mysql.connector import Error
import seed


def lazy_paginate(page_size):
    """
    Generator that yields pages of users from the database using LIMIT/OFFSET.
    """
    i = 1
    while (True):
        offset = page_size * (i - 1)
        i += 1
        try:
            rows = paginate_users(page_size, offset)
            if not rows:
                break
            yield rows
        except Error as e:
            print(f"Pagination failed: {e}")
            break


def paginate_users(page_size, offset):
    """
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s",
                   (page_size, offset))
    rows = cursor.fetchall()
    connection.close()
    return rows


if __name__ == "__main__":

    print(lazy_paginate(100))
