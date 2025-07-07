import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)

@pytest.fixture
def sample_chat_request():
    """Create a sample chat request"""
    return {
        "messages": [
            {"role": "user", "content": "What are healthy breakfast options?"}
        ]
    }

@pytest.fixture
def mock_get_message(monkeypatch):
    """Mock the get_message function"""
    def mock_response(question, history):
        return {
            "role": "system",
            "content": "Here are some healthy breakfast options: oatmeal, eggs, yogurt with fruits."
        }
    
    from services import get_message
    monkeypatch.setattr(get_message, "get_message", mock_response) 