import mysql.connector
from mysql.connector import Error
from chatbot.config import Config

def test_database_connection():
    """Utility function to test database connection"""
    try:
        connection = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
            port=Config.DB_PORT
        )
        if connection.is_connected():
            print("Successfully connected to MySQL database!")
            connection.close()
            return True
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    return False