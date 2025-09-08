# Contributing to resumeio-dl

Thank you for considering contributing to resumeio-dl! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

Please be respectful and considerate of others when contributing to this project.

## How to Contribute

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Add or update tests as necessary
5. Ensure all tests pass
6. Submit a pull request

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/resumeio-dl.git
   cd resumeio-dl
   ```

2. Create a virtual environment and install development dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

## Testing

Run tests using pytest:
```bash
pytest
```

## Pull Request Process

1. Update the README.md with details of changes if appropriate
2. Update the version number in `resumeio_dl/__init__.py` following [Semantic Versioning](https://semver.org/)
3. The PR will be merged once reviewed and approved

## Style Guidelines

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Use docstrings for functions and classes
- Write clear commit messages
