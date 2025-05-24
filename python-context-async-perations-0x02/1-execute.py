#!/usr/bin/python3

import sqlite3
from contextlib import contextmanager

class ExecuteQuery:
    """
    A context manager that handles database connection and query execution.
    Takes a query and parameters, executes the query, and returns the results.
    """
    def __init__(self, db_name='users.db', query=None, params=None):
        self.db_name = db_name
        self.query = query
        self.params = params
        self.connection = None
        self.cursor = None
        self.results = None
    
    def __enter__(self):
        """Initialize the connection and execute the query when entering the context"""
        try:
            # Establish database connection
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            
            # Execute the query with parameters
            if self.params is None:
                self.cursor.execute(self.query)
            else:
                self.cursor.execute(self.query, self.params)
            
            # Fetch all results
            self.results = self.cursor.fetchall()
            return self.results
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")
            raise
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Clean up resources when exiting the context"""
        # Handle any exceptions that occurred
        if exc_type:
            # Rollback if an error occurred
            if self.connection:
                self.connection.rollback()
        else:
            # Commit if no errors occurred
            if self.connection:
                self.connection.commit()
        
        # Close resources
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

# Example usage
query = "SELECT * FROM users WHERE age > ?"
age = 25

try:
    with ExecuteQuery(query=query, params=(age,)) as results:
        print("Query results:")
        for row in results:
            print(row)
except sqlite3.Error as e:
    print(f"Database operation failed: {e}")
