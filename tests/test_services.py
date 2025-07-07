import pytest
from unittest.mock import Mock, patch
from services.get_message import get_message
from models.schemas import ChatMessage

@pytest.fixture
def mock_openai():
    with patch("services.get_message.OpenAIEmbeddings") as mock_embeddings, \
         patch("services.get_message.init_chat_model") as mock_llm:
        mock_embeddings.return_value = Mock()
        mock_llm.return_value = Mock()
        yield {
            "embeddings": mock_embeddings,
            "llm": mock_llm
        }

@pytest.fixture
def mock_pinecone():
    with patch("services.get_message.Pinecone") as mock_pinecone, \
         patch("services.get_message.PineconeVectorStore") as mock_vector_store:
        mock_index = Mock()
        mock_pinecone.return_value.Index.return_value = mock_index
        mock_vector_store.return_value.as_retriever.return_value = Mock()
        yield {
            "pinecone": mock_pinecone,
            "vector_store": mock_vector_store
        }

def test_get_message_integration(mock_openai, mock_pinecone):
    """Test get_message function with mocked external services"""
    # Setup test data
    question = ChatMessage(role="user", content="What are healthy breakfast options?")
    history = [
        ChatMessage(role="user", content="Hello"),
        ChatMessage(role="system", content="Hi, how can I help you?")
    ]

    # Configure mock responses
    mock_openai["llm"].return_value.invoke.return_value = "Mocked response"
    
    # Call the function
    result = get_message(question, history)
    
    # Verify the result structure
    assert isinstance(result, dict)
    assert "role" in result
    assert "content" in result
    assert result["role"] == "system"
    
    # Verify external service calls
    mock_openai["embeddings"].assert_called_once()
    mock_openai["llm"].assert_called_once()
    mock_pinecone["pinecone"].assert_called_once()
    mock_pinecone["vector_store"].assert_called_once() 