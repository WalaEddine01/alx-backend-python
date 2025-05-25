#!/usr/bin/python3

import mysql.connector
from typing import Iterator, Optional

def connect_db() -> mysql.connector.connection.MySQLConnection:
    """Establish database connection."""
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ALX_prodev'
    )

def stream_user_ages() -> Iterator[Optional[float]]:
    """
    Generator function that yields user ages one by one.
    
    Yields:
        float: Age of each user, or None if no more rows
    """
    connection = connect_db()
    cursor = connection.cursor()
    
    try:
        cursor.execute("SELECT age FROM user_data")
        while True:
            age = cursor.fetchone()
            if not age:
                break
            yield age[0]  # Yield just the age value
    finally:
        cursor.close()
        connection.close()

def calculate_average_age() -> float:
    """
    Calculate the average age using the generator without loading all data into memory.
    
    Returns:
        float: Average age of all users
    """
    total = 0
    count = 0
    
    for age in stream_user_ages():
        total += age
        count += 1
    
    return total / count if count > 0 else 0.0