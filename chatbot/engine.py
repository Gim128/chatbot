from chatbot.database import Database
from chatbot.config import Config
import random
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class InferenceEngine:
    def __init__(self):
        self.db = Database()
        
    def _get_static_response(self, intent):
        responses = Config.STATIC_RESPONSES.get(intent, Config.STATIC_RESPONSES['default'])
        return random.choice(responses)
        
    def get_response(self, intent):
        db_response = self.db.get_response(intent) if self.db.connection else None
        return db_response if db_response else self._get_static_response(intent)
    
    def get_account_info(self):
        if not self.db.connection:
            return self._get_static_response('account_query')
            
        accounts = self.db.get_account_types()
        if not accounts:
            return "We currently don't have any account information available."
            
        response = "We offer the following account types:\n"
        for account in accounts:
            response += (
                f"- {account['name']}: {account['description']} "
                f"(Min balance: ${account['min_balance']:.2f})\n"
            )
        return response.strip()
    
    def process_input(self, user_input):
        user_input = user_input.lower().strip()
        
        if not user_input:
            return "Please enter your query."
            
        # Basic intent detection
        if any(word in user_input for word in ['hi', 'hello', 'hey']):
            return self.get_response('greeting')
        elif any(word in user_input for word in ['bye', 'goodbye']):
            return self.get_response('farewell')
        elif 'thank' in user_input:
            return self.get_response('thanks')
        elif any(word in user_input for word in ['account', 'save', 'current', 'deposit']):
            return self.get_account_info()
        elif any(word in user_input for word in ['help', 'support']):
            return self.get_response('help')
        else:
            return self.get_response('default')