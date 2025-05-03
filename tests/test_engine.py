import pytest
from chatbot.engine import InferenceEngine
from chatbot.database import Database
from chatbot.config import Config

class TestInferenceEngine:
    @pytest.fixture
    def engine(self):
        return InferenceEngine()
    
    def test_greeting_response(self, engine):
        response = engine.process_input("hello")
        assert response in Config.STATIC_RESPONSES['greeting'] or "hello" in response.lower()
    
    def test_account_query(self, engine):
        response = engine.process_input("tell me about accounts")
        assert "account" in response.lower() or "savings" in response.lower()
    
    def test_default_response(self, engine):
        response = engine.process_input("random gibberish")
        assert response in Config.STATIC_RESPONSES['default']