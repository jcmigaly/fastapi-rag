# FastAPI RAG (Retrieval-Augmented Generation) Application

A production-ready FastAPI application that implements RAG pattern for enhanced AI responses using OpenAI and Pinecone for vector storage. This project demonstrates modern Python development practices, including comprehensive testing, clean architecture, and industry-standard tooling.

## 🚀 Features

- **RAG Implementation**: Combines OpenAI's LLM capabilities with Pinecone vector storage for context-aware responses
- **RESTful API**: Clean FastAPI endpoints with Pydantic validation
- **Production-Ready**: Structured project layout with separation of concerns
- **Comprehensive Testing**: Extensive test suite with mocking and coverage reporting
- **Type Safety**: Leverages Python type hints and Pydantic models throughout

## 🏗 Architecture

```
fastapi-rag/
├── models/          # Pydantic models and schemas
├── routes/          # FastAPI route handlers
├── services/        # Business logic and external service integration
│   └── utils/      # Helper utilities
└── tests/          # Comprehensive test suite
```

## 🔧 Technical Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **OpenAI**: State-of-the-art language models
- **Pinecone**: Vector database for efficient similarity search
- **Pydantic**: Data validation using Python type annotations
- **pytest**: Feature-rich testing framework

## 🛠 Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd fastapi-rag
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```bash
# Create .env file with:
OPENAI_API_KEY=your_openai_key
PINECONE_API_KEY=your_pinecone_key
```

## 🚀 Running the Application

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## 📝 API Endpoints

### Root Endpoint

- `GET /`: Health check endpoint

### Chat Endpoint

- `POST /chat`: Process chat messages with RAG
  - Request Body: `ChatRequest` with message history
  - Response: AI-generated response with context

## 🧪 Testing Infrastructure

This project features a comprehensive testing suite that demonstrates strong Python testing practices:

### Test Structure

```
tests/
├── __init__.py
├── conftest.py          # Shared test fixtures
├── test_main.py         # API endpoint tests
├── test_chat.py         # Chat functionality tests
└── test_services.py     # Service layer tests
```

### Test Coverage

- **API Tests**: Endpoint validation, response formats, error handling
- **Schema Tests**: Data validation, type checking, edge cases
- **Service Tests**: Business logic, external service mocking
- **Integration Tests**: End-to-end flow testing with mocked dependencies

### Testing Tools

- **pytest**: Primary testing framework
- **pytest-cov**: Coverage reporting
- **pytest-asyncio**: Async test support
- **httpx**: FastAPI client testing

### Running Tests

```bash
# Run all tests with coverage report
python -m pytest

# View coverage report in terminal
python -m pytest --cov=. --cov-report=term-missing

# Generate HTML coverage report
python -m pytest --cov=. --cov-report=html
```

### Test Fixtures

- `client`: FastAPI test client
- `mock_openai`: OpenAI service mocks
- `mock_pinecone`: Pinecone service mocks
- `sample_chat_request`: Sample test data

### Mocking Strategy

- External services (OpenAI, Pinecone) are properly mocked
- Deterministic test behavior
- Isolated test cases
- Comprehensive edge case coverage

## 🔍 Code Quality

- Type hints throughout the codebase
- Pydantic models for data validation
- Comprehensive docstrings
- Clean code principles
- Separation of concerns

## 📈 Future Improvements

1. Add more sophisticated RAG strategies
2. Implement caching layer
3. Add authentication and rate limiting
4. Expand test coverage for edge cases
5. Add performance testing
6. Implement CI/CD pipeline

## 👥 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details
