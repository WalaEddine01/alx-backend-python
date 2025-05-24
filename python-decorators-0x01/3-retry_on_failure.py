#!/usr/bin/python3

import time
import sqlite3
import functools
import random

def with_db_connection(func):
    """
    A decorator that automatically handles database connections.
    Opens a connection before executing the decorated function and
    closes it afterward.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper

def retry_on_failure(retries=3, delay=2):
    """
    A decorator that retries a function if it fails.
    Args:
        retries: Number of times to retry the function
        delay: Delay in seconds between retries
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except sqlite3.Error as e:
                    if attempt == retries:
                        raise
                    print(f"Attempt {attempt + 1} failed: {str(e)}")
                    print(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Example usage
try:
    users = fetch_users_with_retry()
    print(users)
except sqlite3.Error as e:
    print(f"Failed after all retries: {e}")
