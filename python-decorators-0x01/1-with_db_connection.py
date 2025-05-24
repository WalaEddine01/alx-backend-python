#!/usr/bin/python3

import sqlite3
import functools

def with_db_connection(func):
    """
    A decorator that automatically handles database connections.
    Opens a connection before executing the decorated function and
    closes it afterward.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Create a new connection
        conn = sqlite3.connect('users.db')
        try:
            # Execute the function with the connection
            result = func(conn, *args, **kwargs)
        finally:
            # Ensure connection is always closed
            conn.close()
        return result
    return wrapper

@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

# Fetch user by ID with automatic connection handling
user = get_user_by_id(user_id=1)
print(user)
