# QuizGen Python Server
///////////////////////////////////////////////////
*THIS WILL NEED CHANGING AS WE UPDATE THE CODEBASE*
///////////////////////////////////////////////////
## Overview
This is the backend server for QuizGen, built with Python/Flask and integrated with AI services for question generation. The server provides RESTful APIs for flashcard management, user authentication, and AI-powered question generation.

## Features
- 🔐 JWT-based authentication
- 📝 CRUD operations for flashcards and decks
- 🤖 AI integration for question generation
- 📊 Study progress tracking
- 🔄 Real-time updates
- 📈 Performance monitoring

## Tech Stack
- Python 3.8+
- Flask
- SQLAlchemy (Database ORM)
- PostgreSQL
- PyJWT for authentication
- pytest for testing
- OpenAI/Claude API integration

## Project Structure
```
server/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── config.py            # Configuration settings
│   ├── models/              # Database models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── card.py
│   │   └── deck.py
│   ├── routes/              # API routes
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── cards.py
│   │   └── ai.py
│   ├── services/            # Business logic
│   │   ├── __init__.py
│   │   ├── ai_service.py
│   │   └── card_service.py
│   ├── utils/               # Helper functions
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── validators.py
│   └── middleware/          # Custom middleware
│       ├── __init__.py
│       └── auth.py
├── tests/                   # Test files
│   ├── __init__.py
│   ├── test_auth.py
│   └── test_ai.py
├── requirements.txt         # Python dependencies
├── run.py                  # Application entry point
└── .env                    # Environment variables
```

## Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL
- virtualenv
- pip

### Installation

1. Create and activate virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create environment file:
```bash
cp .env.example .env
```

4. Configure environment variables:
```env
# Flask Configuration
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your_secret_key

# Database
DATABASE_URL=postgresql://username:password@localhost:5432/quizgen

# Authentication
JWT_SECRET_KEY=your_jwt_secret
JWT_ACCESS_TOKEN_EXPIRES=86400

# AI Service
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key

# Logging
LOG_LEVEL=DEBUG
```

### Available Scripts
```bash
# Start development server
flask run

# Run tests
pytest

# Run with debugging
flask run --debug

# Run linting
flake8
```

## Example Implementations

### AI Service Integration
```python
# app/services/ai_service.py
from openai import OpenAI
import anthropic
import os

class AIService:
    def __init__(self):
        self.openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.anthropic_client = anthropic.Client(api_key=os.getenv('ANTHROPIC_API_KEY'))

    async def generate_questions(self, text_content):
        """Generate questions from text content using AI."""
        try:
            response = await self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Generate study questions from the following text."},
                    {"role": "user", "content": text_content}
                ]
            )
            return self._parse_questions(response)
        except Exception as e:
            logger.error(f"Error generating questions: {str(e)}")
            raise
```

### Route Example
```python
# app/routes/ai.py
from flask import Blueprint, request, jsonify
from app.services.ai_service import AIService
from app.middleware.auth import jwt_required

ai_bp = Blueprint('ai', __name__)
ai_service = AIService()

@ai_bp.route('/generate', methods=['POST'])
@jwt_required
async def generate_questions():
    """Generate questions from provided text."""
    data = request.get_json()
    text_content = data.get('text')
    
    if not text_content:
        return jsonify({'error': 'No text provided'}), 400
        
    try:
        questions = await ai_service.generate_questions(text_content)
        return jsonify({'questions': questions}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
```

### Model Example
```python
# app/models/card.py
from app import db
from datetime import datetime

class Card(db.Model):
    __tablename__ = 'cards'
    
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.String(500), nullable=False)
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    ai_generated = db.Column(db.Boolean, default=False)
```

## API Documentation

### Authentication
```
POST /api/auth/register
POST /api/auth/login
GET /api/auth/profile
PUT /api/auth/profile
```

### Flashcards
```
GET /api/cards
POST /api/cards
GET /api/cards/<id>
PUT /api/cards/<id>
DELETE /api/cards/<id>
```

### AI Generation
```
POST /api/ai/generate
POST /api/ai/improve
```

## Development Guidelines

### Code Style
- Follow PEP 8 guidelines
- Use type hints
- Document functions with docstrings
- Use async/await for I/O operations

### Error Handling
```python
from flask import jsonify

class APIError(Exception):
    def __init__(self, message, status_code=400):
        super().__init__()
        self.message = message
        self.status_code = status_code

@app.errorhandler(APIError)
def handle_api_error(error):
    response = jsonify({'error': error.message})
    response.status_code = error.status_code
    return response
```

## Testing
```python
# tests/test_ai.py
import pytest
from app.services.ai_service import AIService

def test_question_generation():
    ai_service = AIService()
    text = "The mitochondria is the powerhouse of the cell."
    questions = ai_service.generate_questions(text)
    assert len(questions) > 0
    assert all(isinstance(q, dict) for q in questions)
```

## Performance Optimization
- Use async/await for I/O operations
- Implement caching with Redis
- Use connection pooling
- Optimize database queries
- Implement rate limiting

## Contributing
1. Create feature branch
2. Follow PEP 8
3. Write tests
4. Update documentation
5. Submit pull request

Would you like me to:
1. Provide more implementation details for any component?
2. Add example code for other features?
3. Explain the AI integration process in more detail?