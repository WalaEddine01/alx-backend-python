#!/usr/bin/python3
"""
"""
import sqlite3
import functools
import logging
from datetime import datetime


#### decorator to lof SQL queries
custom_prefix = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
format_string = f'{custom_prefix} - %(levelname)s - %(message)s'
logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    format=format_string
)

def log_queries(function):
   """
   """
   @functools.wraps(function)
   def wrapper(*args, **kwargs):
       """
       """
       print("Logging query")
       logging.info(args, kwargs)
       function(*args, **kwargs)
       print("query executed")
       
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