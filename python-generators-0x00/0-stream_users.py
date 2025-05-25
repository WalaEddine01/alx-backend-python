#!/usr/bin/python3
import mysql.connector
from typing import Iterator, Dict

def connect_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to MySQL database."""
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ALX_prodev'
    )

def stream_users() -> Iterator[Dict]:
    """
    Generator function that streams users one by one from the database.
    
    Yields:
        dict: Dictionary containing user information
    """
    # Create connection and cursor
    cnx = connect_db()
    cursor = cnx.cursor(dictionary=True)
    
    try:
        # Execute query
        cursor.execute("SELECT * FROM user_data")
        
        # Fetch and yield one row at a time
        while True:
            row = cursor.fetchone()
            if not row:
                break
            yield dict(row)
            
    finally:
        # Ensure cleanup happens even if there's an error
        cursor.close()
        cnx.close()
