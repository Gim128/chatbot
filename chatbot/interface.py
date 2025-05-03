from chatbot.engine import InferenceEngine
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ChatInterface:
    def __init__(self):
        self.engine = InferenceEngine()
        logger.info("Chatbot initialized")
    
    def start_chat(self):
        print("\nWelcome to Simple Banking Chatbot!")
        print("Type 'quit' or 'exit' to end the conversation\n")
        
        while True:
            try:
                user_input = input("You: ").strip()
                
                if user_input.lower() in ['quit', 'exit']:
                    print("\nChatbot: Goodbye! Have a nice day!")
                    break
                    
                response = self.engine.process_input(user_input)
                print(f"Chatbot: {response}\n")
                
            except KeyboardInterrupt:
                print("\n\nChatbot: Goodbye!")
                break
            except Exception as e:
                logger.error(f"Error in chat session: {e}")
                print("Chatbot: Sorry, I encountered an error. Please try again.")