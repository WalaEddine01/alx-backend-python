#!/usr/bin/python3

import mysql.connector
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
from os import getenv
from uuid import uuid4
load_dotenv()


def connect_db():
    """
    connects to the mysql database server
    """
    connection = mysql.connector.connect(
        user=getenv('MYSQL_ROOT_USER'),
        password=getenv('MYSQL_ROOT_PASSWORD'),
        host=getenv('MYSQL_HOST', 'localhost'),
        port=int(getenv('MYSQL_PORT')),
    )
    return connection


def create_database(connection):
    """
    creates the database ALX_prodev if it does not exist
    """
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS ALX_prodev")


def connect_to_prodev():
    """
    connects the the ALX_prodev database in MYSQL
    """
    try:
        connection = mysql.connector.connect(
            user=getenv('MYSQL_ROOT_USER'),
            password=getenv('MYSQL_ROOT_PASSWORD'),
            host=getenv('MYSQL_HOST', 'localhost'),
            port=int(getenv('MYSQL_PORT')),
            database='ALX_prodev'
        )
        print('✅successfully connceted to prodev')
        return connection
    except Error as e:
        print(f"❌ Error Connection Database: {e}")


def create_table(connection):
    """
    creates a table user_data if it does not exists with the required fields
    """
    query1 = 'DROP TABLE IF EXISTS user_data'
    query = """
CREATE TABLE IF NOT EXISTS user_data(
                       user_id VARCHAR(255) PRIMARY KEY,
                       name VARCHAR(64) NOT NULL,
                       email VARCHAR(65) NOT NULL UNIQUE,
                       age DECIMAL NOT NULL)
"""
    try:
        cursor = connection.cursor()
        cursor.execute(query1)
        cursor.execute(query)
        print("✅ Table 'user_data' created successfully")
    except Error as e:
        print(f"❌ Error creating table: {e}")
        cursor.close()


def insert_data(connection, data):
    """
    inserts data in the database if it does not exist
    """
    try:
        cursor = connection.cursor()
        query = """INSERT INTO user_data (user_id, name, email, age)
        VALUES (%s, %s, %s, %s)"""

        with open(data, 'r') as file:
            next(file)
            prepared_data = [
                (str(uuid4()), name.strip(), email.strip(),
                 int(age.strip().strip('"')))
                for line in file
                for name, email, age in [line.strip().split(',')]
            ]
        cursor.executemany(query, prepared_data)  # Bulk insert
        connection.commit()

        print(f"✅ Inserted {len(data)} users successfully")
    except Error as e:
        connection.rollback()
        print(f"❌ Error inserting users: {e}")
        raise
    finally:
        cursor.close()


if __name__ == '__main__':
    connection = mysql.connector.connect(
                user=getenv('MYSQL_ROOT_USER'),
                password=getenv('MYSQL_ROOT_PASSWORD'),
                host=getenv('MYSQL_HOST', 'localhost'),
                port=int(getenv('MYSQL_PORT')),
                database='ALX_prodev'
            )
    cursor = connection.cursor()
    cursor.execute("SELECT * from user_data")
