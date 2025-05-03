import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
    DB_NAME = os.getenv("DB_NAME", "chatbot_db")
    DB_PORT = os.getenv("DB_PORT", 3306)

    STATIC_RESPONSES = {
        'greeting': ['Hello!', 'Hi there!', 'How can I help?'],
        'farewell': ['Goodbye!', 'See you later!', 'Bye!'],
        'thanks': ['You\'re welcome!', 'Happy to help!'],
        'default': ["I'm not sure I understand", "Could you rephrase that?"],
        'help': ['I can help with account information', 'Ask me about banking services']
    }
