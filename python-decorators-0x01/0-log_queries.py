#!/usr/bin/python3
"""
This module I am applying decorators concept
on logging Data base Queries
"""
import sqlite3
import functools
from datetime import datetime

#### decorator to lof SQL queries

def log_queries(func):
    """
    A decorator that logs SQL queries before they are executed.
    Logs include the query string and current timestamp.
    """
    @functools.wraps(func)
    
    def wrapper(*args, **kwargs):
        try:
            # Get the query from arguments
            logs = {"query": kwargs.get("query"), 'Time': str(datetime.now())}
            if not logs["query"]:
                raise ValueError('Missing Query parameter')
            print(logs)
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error executing query: {str(e)}")
            raise
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
