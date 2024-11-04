# QuizGen Client
///////////////////////////////////////////////////
*THIS WILL NEED CHANGING AS WE UPDATE THE CODEBASE*
///////////////////////////////////////////////////
## Overview
This is the frontend application for QuizGen, an AI-powered flashcard study platform. The client is built using React and provides an intuitive interface for creating, managing, and studying flashcards.

## Features
- 📱 Responsive design for desktop and mobile
- 🎨 Modern, intuitive user interface
- ⚡ Real-time updates
- 📊 Interactive study analytics
- 🔄 Seamless AI integration

## Tech Stack
- React
- React Router for navigation
- Redux for state management
- Axios for API requests
- TailwindCSS for styling
- Jest for testing

## Project Structure
```
src/
├── components/              # Reusable UI components
│   ├── common/             # Shared components
│   │   ├── Button.js
│   │   ├── Input.js
│   │   └── Card.js
│   ├── auth/               # Authentication components
│   │   ├── Login.js
│   │   └── Register.js
│   ├── flashcards/         # Flashcard-related components
│   │   ├── CardCreator.js
│   │   ├── CardList.js
│   │   └── StudyMode.js
│   └── ai/                 # AI-related components
│       └── QuestionGenerator.js
├── pages/                  # Full pages
│   ├── Home.js
│   ├── Dashboard.js
│   └── Study.js
├── services/               # API calls and business logic
│   ├── api.js
│   ├── authService.js
│   └── aiService.js
├── utils/                  # Helper functions
│   └── validators.js
├── styles/                 # CSS/styling files
└── App.js                  # Main application component
```

## Getting Started

### Prerequisites
- Node.js (v14.0.0 or higher)
- npm or yarn
- Git

### Installation

1. Navigate to the client directory:
```bash
cd client
```

2. Install dependencies:
```bash
npm install
```

3. Create environment file:
```bash
cp .env.example .env
```

4. Configure environment variables:
```env
REACT_APP_API_URL=http://localhost:5000
REACT_APP_AI_API_KEY=your_ai_api_key
```

### Available Scripts

```bash
# Start development server
npm start

# Build for production
npm run build

# Run tests
npm test

# Run linting
npm run lint

# Fix linting issues
npm run lint:fix
```

## Development Guidelines

### Component Structure
```jsx
// Example component structure
import React from 'react';
import PropTypes from 'prop-types';

const ComponentName = ({ prop1, prop2 }) => {
  return (
    <div>
      {/* Component content */}
    </div>
  );
};

ComponentName.propTypes = {
  prop1: PropTypes.string.required,
  prop2: PropTypes.number
};

export default ComponentName;
```

### Styling Guidelines
- Use TailwindCSS utility classes
- Create custom components for repeated styles
- Follow mobile-first approach
- Maintain consistent spacing and sizing

### State Management
- Use Redux for global state
- Use React Context for theme/auth state
- Use local state for component-specific data

### API Calls
- All API calls should go through the services layer
- Use axios interceptors for common headers
- Implement proper error handling
- Cache responses when appropriate

Example:
```javascript
// services/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json'
  }
});

// Add authorization header
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
```

### Testing
- Write tests for all components
- Use Jest and React Testing Library
- Maintain at least 80% coverage
- Test all user interactions

Example test:
```javascript
import { render, screen } from '@testing-library/react';
import Button from './Button';

describe('Button Component', () => {
  it('renders correctly', () => {
    render(<Button label="Click me" />);
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });
});
```

### Error Handling
- Implement error boundaries
- Show user-friendly error messages
- Log errors for debugging
- Handle offline scenarios

### Performance Optimization
- Lazy load routes
- Implement code splitting
- Optimize images
- Use memoization when appropriate
- Implement proper loading states

## Common Issues & Solutions

### Build Issues
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules
npm install
```

### API Connection Issues
- Verify environment variables
- Check CORS configuration
- Validate API endpoints
- Check network connectivity

## Contributing
1. Create a new branch for your feature
2. Follow the style guide
3. Write tests for new features
4. Update documentation
5. Submit a pull request

## Useful Resources
- [React Documentation](https://reactjs.org/docs)
- [Redux Documentation](https://redux.js.org)
- [TailwindCSS Documentation](https://tailwindcss.com/docs)
- [Jest Documentation](https://jestjs.io/docs)

## Browser Support
- Chrome (last 2 versions)
- Firefox (last 2 versions)
- Safari (last 2 versions)
- Edge (last 2 versions)

## Performance Metrics
- First Contentful Paint: < 1.8s
- Time to Interactive: < 3.9s
- Speed Index: < 3.4s
- Performance Score: > 90

## Todo
- [ ] Add PWA support
- [ ] Improve accessibility
- [ ] Add E2E tests
- [ ] Implement advanced caching