#!/usr/bin/python3

import mysql.connector
from typing import Iterator, List, Dict

def connect_db() -> mysql.connector.connection.MySQLConnection:
    """Establish database connection."""
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ALX_prodev'
    )

def paginate_users(page_size: int, offset: int = 0) -> List[Dict]:
    """
    Fetches a page of users from the database.
    
    Args:
        page_size: Number of records to fetch
        offset: Starting position for the query (default: 0)
        
    Returns:
        List[Dict]: List of user dictionaries
    """
    connection = connect_db()
    cursor = connection.cursor(dictionary=True)
    
    try:
        query = "SELECT * FROM user_data LIMIT %s OFFSET %s"
        cursor.execute(query, (page_size, offset))
        return cursor.fetchall()
    finally:
        cursor.close()
        connection.close()

def lazy_paginate(page_size: int) -> Iterator[List[Dict]]:
    """
    Generator function that implements lazy pagination.
    
    Args:
        page_size: Number of records per page
        
    Yields:
        List[Dict]: List of user dictionaries for each page
    """
    while True:
        page = paginate_users(page_size)
        if not page:
            break
        yield page
