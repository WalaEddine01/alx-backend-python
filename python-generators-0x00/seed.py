#!/usr/bin/python3
import mysql.connector
from mysql.connector import Error
import uuid
import csv
from typing import Iterator, Tuple, Optional

class DatabaseConnection:
    def __init__(self, config: dict):
        self.config = config
        self.connection = None
            
    def connect(self) -> bool:
        try:
            self.connection = mysql.connector.connect(**self.config)
            return True
        except Error as e:
            print(f"Error connecting to database: {e}")
            return False

def connect_db(config: dict) -> Optional[mysql.connector.MySQLConnection]:
    """
    Establishes a connection to the MySQL database server.
    
    Args:
        config: Dictionary containing database connection parameters
        
    Returns:
        MySQL connection object or None if connection fails
    """
    db_connection = DatabaseConnection(config)
    if db_connection.connect():
        return db_connection.connection
    return None

def create_database(connection: mysql.connector.MySQLConnection) -> None:
    """
    Creates the ALX_prodev database if it doesn't exist.
    """
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()

def connect_to_prodev(connection: mysql.connector.MySQLConnection) -> Optional[mysql.connector.MySQLConnection]:
    """
    Connects to the ALX_prodev database.
    
    Args:
        connection: Existing MySQL connection
        
    Returns:
        New connection object connected to ALX_prodev or None if fails
    """
    try:
        connection.close()
        return mysql.connector.connect(
            **connection.config,
            database='ALX_prodev'
        )
    except Error as e:
        print(f"Error connecting to ALX_prodev: {e}")
        return None

def create_table(connection: mysql.connector.MySQLConnection) -> None:
    """
    Creates the user_data table with specified fields.
    """
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id VARCHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL
    ) ENGINE=InnoDB;
    """
    cursor.execute(query)
    cursor.close()

def insert_data(connection: mysql.connector.MySQLConnection, filename: str) -> None:
    """
    Inserts data from CSV file into the user_data table.
    
    Args:
        connection: Database connection
        filename: Path to CSV file containing user data
    """
    cursor = connection.cursor()
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Generate UUID if not provided
            user_id = uuid.UUID(row['user_id']) if row.get('user_id') else uuid.uuid4()
            
            query = """
            INSERT IGNORE INTO user_data (user_id, name, email, age)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (
                str(user_id),
                row['name'],
                row['email'],
                float(row['age'])
            ))
    connection.commit()
    cursor.close()

def stream_rows_generator(
    connection: mysql.connector.MySQLConnection,
    batch_size: int = 1000
) -> Iterator[Tuple[str, str, str, float]]:
    """
    Generator function that streams rows from the user_data table in batches.
    
    Args:
        connection: Database connection
        batch_size: Number of rows to fetch at once (default: 1000)
        
    Yields:
        Tuple containing (user_id, name, email, age)
    """
    cursor = connection.cursor()
    query = "SELECT user_id, name, email, age FROM user_data"
    
    while True:
        rows = cursor.fetchmany(batch_size)
        if not rows:
            break
            
        for row in rows:
            yield row
            
    cursor.close()
