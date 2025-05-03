import mysql.connector
from mysql.connector import Error
from chatbot.config import Config
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        self.connection = None
        self.connect()
        self.setup_database()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=Config.DB_HOST,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_NAME,
                port=Config.DB_PORT
            )
            logger.info("Connected to MySQL database")
        except Error as e:
            logger.error(f"Error connecting to MySQL: {e}")
            self.connection = None

    def setup_database(self):
        if not self.connection:
            return
            
        try:
            cursor = self.connection.cursor()
            
            # Create responses table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS responses (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    intent VARCHAR(50) NOT NULL,
                    response TEXT NOT NULL
                )
            """)
            
            # Create account_types table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS account_types (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    description TEXT,
                    min_balance DECIMAL(10,2)
                )
            """)
            
            # Insert initial data if tables are empty
            cursor.execute("SELECT COUNT(*) FROM responses")
            if cursor.fetchone()[0] == 0:
                initial_responses = [
                    ('greeting', 'Hello! How can I help you today?'),
                    ('greeting', 'Hi there! What can I do for you?'),
                    ('farewell', 'Goodbye! Have a great day!'),
                    ('thanks', 'You\'re welcome!'),
                    ('account_query', 'We offer several account types'),
                    ('help', 'I can tell you about our banking services')
                ]
                
                cursor.executemany(
                    "INSERT INTO responses (intent, response) VALUES (%s, %s)",
                    initial_responses
                )
                logger.info("Inserted initial responses data")
            
            cursor.execute("SELECT COUNT(*) FROM account_types")
            if cursor.fetchone()[0] == 0:
                account_types = [
                    ('Savings', 'Basic savings account with interest', 100.00),
                    ('Current', 'Business account with no interest', 500.00),
                    ('Fixed Deposit', 'High-interest account with fixed term', 1000.00)
                ]
                
                cursor.executemany(
                    "INSERT INTO account_types (name, description, min_balance) VALUES (%s, %s, %s)",
                    account_types
                )
                logger.info("Inserted initial account types data")
            
            self.connection.commit()
            cursor.close()
            
        except Error as e:
            logger.error(f"Error setting up database: {e}")
            if self.connection:
                self.connection.rollback()

    def get_response(self, intent):
        if not self.connection:
            return None
            
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(
                "SELECT response FROM responses WHERE intent = %s ORDER BY RAND() LIMIT 1",
                (intent,)
            )
            result = cursor.fetchone()
            cursor.close()
            return result['response'] if result else None
        except Error as e:
            logger.error(f"Error fetching response: {e}")
            return None

    def get_account_types(self):
        if not self.connection:
            return None
            
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT name, description, min_balance FROM account_types")
            results = cursor.fetchall()
            cursor.close()
            return results
        except Error as e:
            logger.error(f"Error fetching account types: {e}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()
            logger.info("Database connection closed")