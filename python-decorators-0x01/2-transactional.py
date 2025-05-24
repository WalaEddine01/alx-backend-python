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
        conn = args[0]  # Get the connection from the arguments
        try:
            # Start transaction
            cursor = conn.cursor()
            cursor.execute("BEGIN TRANSACTION")
            
            # Execute the function
            result = func(*args, **kwargs)
            
            # Commit if successful
            conn.commit()
            return result
        except Exception as e:
            # Rollback if error occurs
            conn.rollback()
            raise e
        finally:
            # Ensure transaction is always ended
            cursor.execute("COMMIT")
    return wrapper

@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    return cursor.rowcount

# Example usage
try:
    rows_affected = update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
    print(f"Updated {rows_affected} row(s)")
except sqlite3.Error as e:
    print(f"Error updating email: {e}")
