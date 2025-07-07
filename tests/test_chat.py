import pytest
from models.schemas import ChatMessage, ChatRequest, ChatResponse

def test_chat_endpoint_success(client, sample_chat_request, mock_get_message):
    """Test successful chat endpoint request"""
    response = client.post("/chat", json=sample_chat_request)
    assert response.status_code == 200
    assert "role" in response.json()
    assert "content" in response.json()
    assert response.json()["role"] == "system"

def test_chat_endpoint_invalid_request(client):
    """Test chat endpoint with invalid request"""
    invalid_request = {"messages": [{"invalid_field": "test"}]}
    response = client.post("/chat", json=invalid_request)
    assert response.status_code == 422

def test_chat_message_schema():
    """Test ChatMessage schema validation"""
    # Test valid message
    valid_message = ChatMessage(role="user", content="test message")
    assert valid_message.role == "user"
    assert valid_message.content == "test message"

    # Test default values
    default_message = ChatMessage()
    assert default_message.role == "system"
    assert default_message.content == "Hi, how can I help you today?"

    # Test invalid role
    with pytest.raises(ValueError):
        ChatMessage(role="invalid_role", content="test message")

def test_chat_request_schema():
    """Test ChatRequest schema validation"""
    messages = [
        ChatMessage(role="user", content="test message"),
        ChatMessage(role="system", content="test response")
    ]
    request = ChatRequest(messages=messages)
    assert len(request.messages) == 2
    assert request.messages[0].role == "user"
    assert request.messages[1].role == "system"

def test_chat_response_schema():
    """Test ChatResponse schema validation"""
    response = ChatResponse(answer="test answer")
    assert response.answer == "test answer" 