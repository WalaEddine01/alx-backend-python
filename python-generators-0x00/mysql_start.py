#!/usr/bin/python3
import os
import sys
from mysql.connector import connect, Error
from dotenv import load_dotenv

def mysql_start(db_user, db_name, db_pass):
    try:
        
        load_dotenv()
        root_user = os.getenv('MYSQL_USER', 'root')
        root_pass = os.getenv('MYSQL_PASSWORD', '')
        host = os.getenv('MYSQL_HOST', 'localhost')
        port = int(os.getenv('MYSQL_PORT', '3306'))

        connection = connect(
            host=host,
            port=port,
            user=root_user,
            password=root_pass,
        )

        cursor = connection.cursor()

        # Execute SQL commands
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{db_name}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        cursor.execute(f"CREATE USER IF NOT EXISTS '{db_user}'@'localhost' IDENTIFIED BY '{db_pass}'")
        cursor.execute(f"GRANT ALL PRIVILEGES ON `{db_name}`.* TO '{db_user}'@'localhost'")
        cursor.execute("FLUSH PRIVILEGES")

        connection.commit()
        print(f"✅ Successfully created:")
        print(f"- Database: {db_name}")
        print(f"- User: {db_user}")
        print(f"- Privileges: ALL on {db_name}.*")

    except Error as err:
        print(f"❌ MySQL Error: {err}", file=sys.stderr)
        sys.exit(1)
    except ValueError as ve:
        print(f"❌ Validation Error: {ve}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected Error: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python create_mysql_db.py <username> <dbname> <dbpassword>")
        sys.exit(1)
    
    mysql_start(sys.argv[1], sys.argv[2], sys.argv[3])