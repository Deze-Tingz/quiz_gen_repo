# QuizGen - AI-Powered Flashcard Application
///////////////////////////////////////////////////
*THIS WILL NEED CHANGING AS WE UPDATE THE CODEBASE*
///////////////////////////////////////////////////
## Overview
QuizGen is a web-based application that allows users to create, manage, and study with flashcards. It features AI-powered question generation to help users create study materials from their notes or textbook content.

### Key Features
- ✨ Create and manage flashcard decks
- 🤖 AI-powered question generation
- 📚 Organized study materials by categories
- 📊 Track study progress
- 🔐 Secure user authentication

## Getting Started

### Prerequisites
- Node.js (v14.0.0 or higher)
- npm or yarn
- MongoDB (v4.0.0 or higher)
- Git

### Installation

1. Clone the repository
```bash
git clone [your-repository-url]
cd quiz-app
```

2. Install dependencies for both client and server
```bash
# Install root dependencies
npm install

# Install client dependencies
cd client
npm install

# Install server dependencies
cd ../server
npm install
```

3. Set up environment variables
```bash
# In server directory, create .env file
cp .env.example .env

# In client directory, create .env file
cd ../client
cp .env.example .env
```

4. Configure environment variables
```bash
# Server .env
PORT=5000
MONGODB_URI=mongodb://localhost:27000/quizgen
JWT_SECRET=your_jwt_secret
AI_API_KEY=your_ai_api_key

# Client .env
REACT_APP_API_URL=http://localhost:5000
```

### Running the Application

1. Start the server (development mode)
```bash
# From server directory
npm run dev
```

2. Start the client (development mode)
```bash
# From client directory
npm start
```

The application will be available at `http://localhost:3000`

## Project Structure
```
quiz-app/
├── client/                 # Frontend application
│   ├── public/            # Static files
│   └── src/               # Source files
├── server/                # Backend application
│   └── src/               # Source files
└── README.md             # This file
```

See individual README files in client and server directories for more detailed structure information.

## Development Guidelines

### Code Style
- Use consistent naming conventions
- Follow ESLint configuration
- Write meaningful commit messages
- Comment complex logic
- Create comprehensive documentation for APIs

### Branch Strategy
- `main`: Production-ready code
- `development`: Main development branch
- Feature branches: `feature/feature-name`
- Bug fixes: `fix/bug-name`

### Commit Messages
Follow the conventional commits specification:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `test`: Adding or modifying tests

Example: `feat: add AI question generation`

## API Documentation

### Authentication Endpoints
- POST `/api/auth/register` - Register new user
- POST `/api/auth/login` - User login

### Flashcard Endpoints
- GET `/api/cards` - Get all flashcards
- POST `/api/cards` - Create new flashcard
- GET `/api/cards/:id` - Get specific flashcard
- PUT `/api/cards/:id` - Update flashcard
- DELETE `/api/cards/:id` - Delete flashcard

### AI Generation Endpoints
- POST `/api/ai/generate` - Generate questions from text

Detailed API documentation is available in the server/docs directory.

## Testing
Run tests using the following commands:

```bash
# Run client tests
cd client
npm test

# Run server tests
cd server
npm test
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Team Members
- Juansimon Arroyave
- Akiva Yeshurun
- Maria Paula Romero
- Val [LastName]

## License
This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments
- Thanks to Dr. Abdul Rehman Gilal for guidance
- Built using [List of major libraries/frameworks]
- AI capabilities powered by [AI Service Provider]