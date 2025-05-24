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
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper

def transactional(func):
    """
    A decorator that wraps a database operation in a transaction.
    Commits if successful, rolls back if an error occurs.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = args[0]
        try:

            cursor = conn.cursor()
            cursor.execute("BEGIN TRANSACTION")
            
            result = func(*args, **kwargs)
            
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cursor.execute("COMMIT")
    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    return cursor.rowcount

try:
    rows_affected = update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
    print(f"Updated {rows_affected} row(s)")
except sqlite3.Error as e:
    print(f"Error updating email: {e}")
