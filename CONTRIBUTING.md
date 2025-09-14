# Contributing to Career-bot 🤝

We love your input! We want to make contributing to Career-bot as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

## Pull Requests

Pull requests are the best way to propose changes to the codebase. We actively welcome your pull requests:

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Development Setup

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git

### Local Development

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/Career-bot.git
   cd Career-bot
   ```

2. **Set up the backend**
   ```bash
   cd Portal/career_counselling_portal
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env
   # Fill in your environment variables
   python manage.py migrate
   python manage.py runserver
   ```

3. **Set up the frontend**
   ```bash
   cd Portal
   npm install
   cp .env.example .env
   # Configure your environment variables
   npm run dev
   ```

4. **Set up the AI chatbot**
   ```bash
   # In the root directory
   pip install -r requirements.txt
   cp .env.example .env
   # Add your GEMINI_API_KEY
   streamlit run main.py
   ```

## Code Style

### Python (Django Backend)
- Follow PEP 8
- Use `black` for code formatting
- Use `flake8` for linting
- Maximum line length: 88 characters

```bash
# Format code
black .

# Lint code
flake8 .
```

### JavaScript/React (Frontend)
- Follow ESLint configuration
- Use Prettier for code formatting
- Use meaningful variable and function names

```bash
# Lint and format
npm run lint
npm run format
```

## Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools

### Examples
```
feat(auth): add JWT token authentication
fix(chat): resolve message ordering issue
docs(readme): update installation instructions
style(frontend): format code with prettier
```

## Branch Naming

Use descriptive branch names:
- `feature/add-user-authentication`
- `fix/resolve-chat-bug`
- `docs/update-api-documentation`
- `refactor/improve-error-handling`

## Testing

### Backend Testing
```bash
cd Portal/career_counselling_portal
python manage.py test
```

### Frontend Testing
```bash
cd Portal
npm test
```

### End-to-End Testing
We use Cypress for E2E testing:
```bash
cd Portal
npm run cypress:open
```

## Documentation

- Update the README.md if you change functionality
- Add docstrings to new Python functions
- Comment complex logic
- Update API documentation for backend changes

## Issue Reporting

When reporting issues, please include:

1. **Bug Description**: A clear description of the bug
2. **Steps to Reproduce**: Detailed steps to reproduce the issue
3. **Expected Behavior**: What you expected to happen
4. **Actual Behavior**: What actually happened
5. **Environment**: OS, Python version, Node.js version, browser
6. **Screenshots**: If applicable

### Bug Report Template

```markdown
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**
 - OS: [e.g. Windows 10, macOS Big Sur, Ubuntu 20.04]
 - Python Version: [e.g. 3.9.7]
 - Node.js Version: [e.g. 16.14.0]
 - Browser: [e.g. Chrome 96, Firefox 94]

**Additional context**
Add any other context about the problem here.
```

## Feature Requests

We welcome feature requests! Please provide:

1. **Use Case**: Describe the problem this feature would solve
2. **Proposed Solution**: Your idea for how to implement it
3. **Alternatives**: Other solutions you've considered
4. **Implementation Details**: Technical considerations if any

## Project Structure

```
Career-bot/
├── main.py                    # Streamlit AI chatbot
├── backend.py                 # Gemini AI integration
├── Portal/                    # Main web application
│   ├── src/                   # React frontend source
│   │   ├── components/        # Reusable components
│   │   ├── pages/            # Page components
│   │   ├── features/         # Feature-specific code
│   │   └── assets/           # Static assets
│   └── career_counselling_portal/  # Django backend
│       ├── career_portal/    # Main Django app
│       ├── settings.py       # Django settings
│       └── urls.py          # URL routing
└── docs/                     # Documentation
```

## Areas for Contribution

### High Priority
- [ ] Improve error handling and validation
- [ ] Add comprehensive testing
- [ ] Enhance accessibility (a11y)
- [ ] Performance optimizations
- [ ] Security improvements

### Medium Priority
- [ ] Add internationalization (i18n)
- [ ] Mobile app development
- [ ] Advanced AI features
- [ ] Analytics and reporting
- [ ] Email notifications

### Low Priority
- [ ] Dark mode theme
- [ ] Social media integration
- [ ] Advanced search features
- [ ] Export functionality

## Code Review Process

1. **Automated Checks**: All PRs must pass CI/CD checks
2. **Manual Review**: At least one maintainer will review your code
3. **Testing**: Ensure your changes don't break existing functionality
4. **Documentation**: Update docs if needed

## Community

- **Discussions**: Use GitHub Discussions for questions and ideas
- **Issues**: Use GitHub Issues for bug reports and feature requests
- **Pull Requests**: Use PRs for code contributions

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- GitHub contributors page

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Don't hesitate to ask questions! You can:
- Open a GitHub Discussion
- Create an issue
- Contact the maintainers

Thank you for contributing to Career-bot! 🚀