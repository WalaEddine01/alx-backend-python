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

def stream_users_in_batches(batch_size: int) -> Iterator[List[Dict]]:
    """
    Generator function that yields batches of users from the database.
    
    Args:
        batch_size: Number of records to include in each batch
        
    Yields:
        List[Dict]: List of user dictionaries
    """
    cnx = connect_db()
    cursor = cnx.cursor(dictionary=True)
    
    try:
        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                break
            yield batch
    finally:
        cursor.close()
        cnx.close()

def batch_processing(batch_size: int) -> None:
    """
    Processes users in batches, filtering for those over 25 years old.
    
    Args:
        batch_size: Size of each batch to process
    """
    for batch in stream_users_in_batches(batch_size):
        # Single pass through the batch to filter users
        for user in batch:
            if user['age'] > 25:
                print(user)