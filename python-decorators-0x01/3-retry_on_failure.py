#!/usr/bin/python3
import time
import sqlite3 
import functools
with_db_connection = __import__("1-with_db_connection")\
    .with_db_connection

#### paste your with_db_decorator here

def retry_on_failure(retries=3, delay=2):
    """
    """
    def decorator(func):
        """
        """
        def wrapper(*args, **kwargs):
            """
            """
            for i in range(retries):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f'Attempt {i+1} failed: {e}. Retrying in {delay}s...')
                    time.sleep(delay)
                    error_message = e
                    continue
            raise error_message
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=2)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT num FROM users")
    return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure
users = fetch_users_with_retry()
print(users)
