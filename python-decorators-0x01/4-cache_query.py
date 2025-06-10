#!/usr/bin/python3
"""
"""
import time
import sqlite3 
import functools
with_db_connection = __import__("1-with_db_connection")\
    .with_db_connection


query_cache = {}

def cache_query(func):
    """
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        """
        value = kwargs.get('query')
        print("CACHE HIT" if value in query_cache else "CACHE MISS")
        if value in query_cache:
            return query_cache[value]
        query_cache[value] = func(*args,
                                  **kwargs)
        return query_cache[value]
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")
print(users)
#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
print(users_again)

users_again2 = fetch_users_with_cache(query="SELECT id FROM users")
print(users_again2)

