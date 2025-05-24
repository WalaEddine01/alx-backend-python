#!/usr/bin/python3

import sqlite3

class DatabaseConnection:
    """
    A custom context manager class for handling database connections.
    Automatically opens and closes connections when used with 'with' statement.
    """
    def __init__(self, db_name='users.db'):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
    
    def __enter__(self):
        """Initialize the connection when entering the 'with' block"""
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            return self
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            raise
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Clean up resources when exiting the 'with' block"""
        if exc_type:
            if self.connection:
                self.connection.rollback()
        else:
            if self.connection:
                self.connection.commit()
        
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
    
    def execute_query(self, query, params=None):
        """Execute a SQL query and return the results"""
        try:
            if params is None:
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            raise

# Example usage
try:
    with DatabaseConnection() as db:
        results = db.execute_query("SELECT * FROM users")
        
        for row in results:
            print(row)
except sqlite3.Error as e:
    print(f"Database operation failed: {e}")
