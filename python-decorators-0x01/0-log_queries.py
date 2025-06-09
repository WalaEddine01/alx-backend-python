#!/usr/bin/python3
"""
"""
import sqlite3
import functools
import logging


#### decorator to lof SQL queries
logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def log_queries(function):
   """
   """
   @functools.wraps(function)
   def wrapper(*args, **kwargs):
       """
       """
       logging.info(args, kwargs)
       function(*args, **kwargs)
       
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