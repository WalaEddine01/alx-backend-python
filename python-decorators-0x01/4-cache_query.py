#!/usr/bin/python3

import time
import sqlite3
import functools

query_cache = {}

def cache_query(func):
    """
    A decorator that caches database query results based on the SQL query string.
    Avoids redundant database calls by storing and reusing query results.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get the query from arguments (assuming it's the first positional arg)
        query = args[0] if args else kwargs.get('query')
        
        # Check if result is in cache
        if query in query_cache:
            print("Retrieving result from cache...")
            return query_cache[query]
        
        # If not in cache, execute the query and store result
        print("Executing query...")
        result = func(*args, **kwargs)
        query_cache[query] = result
        return result
    
    return wrapper

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

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# Example usage
# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
