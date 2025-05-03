from chatbot.interface import ChatInterface
from chatbot.utils import test_database_connection
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    print("Starting Simple Banking Chatbot...")
    
    # Test database connection first
    if not test_database_connection():
        print("Warning: Could not connect to MySQL database. Using fallback responses.")
    
    # Start the chatbot
    chatbot = ChatInterface()
    chatbot.start_chat()

if __name__ == "__main__":
    main()