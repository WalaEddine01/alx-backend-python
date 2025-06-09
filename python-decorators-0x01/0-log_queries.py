#!/usr/bin/python3
"""
"""
import sqlite3
import functools
import logging
from datetime import datetime


#### decorator to lof SQL queries
logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_queries(function):
   """
   """
   @functools.wraps(function)
   def wrapper(*args, **kwargs):
       """
       """
       query = kwargs.get('query') or\
        (args[0] if args else None)
       print("Logging query")
       logging.info(f"Executing query: {query}")
       result = function(*args, **kwargs)
       logging.info("Query executed successfully.")
       print("query executed")
       return result
       
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