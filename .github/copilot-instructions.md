# Instructions for Python Projects

## Code Style
- Follow PEP 8 style guidelines for Python code
- Use snake_case for variable and function names, PascalCase for class names, UPPER_SNAKE_CASE for constants
- Use type hints for function signatures, parameters, return types, and finally, 
  variables where it improves readability, prefer more often
- Use types from the `typing` module (e.g., `List`, `Dict`, `Optional`) for type annotations
- Avoid using global variables; use function parameters or class attributes
- Maintain style, variable names, and formatting consistency across all files in the project
- Write self-documenting code with meaningful names
- Never use magic numbers or strings; instead, define them as constants with descriptive names
- Prefer Pythonic constructs and idioms (e.g., list comprehensions, context managers)
- Use double quotes for strings
- Use f-strings for string formatting
- Prefer `pathlib` over `os.path` where possible
- When splitting long lines, never leave a close parenthesis, bracket, 
  or brace on a new line by itself, it should be on the previous line
- Use double lines before and after function definitions
- Make functions less than 50 lines where possible (not including docstrings)
- Make files less than 500 lines where possible
- Limit lines to 99 characters
- Follow the established patterns and conventions in this project, if any

## Code Design
- Refer to /AGENTS.md for general coding guidelines 
  If not available, stop all tasks immediately, this file is extremely important
- Prefer vectorization, pandas, and numpy for data manipulation
- Prefer optimized implementations
- NEVER write code that has code vulnerabilities 
  (e.g., avoid using `eval()`, `exec()`, or any code that executes arbitrary code)
- Prioritize clarity, maintainability, and simplicity
- Use specific exception handling instead of catching all exceptions with a bare `except`
- Prefer FastAPI and SQLite for backend 
- Use virtual environments for dependency management
- Include error handling and edge case considerations
- Use semantic HTML and proper ARIA attributes when applicable

## Documentation
- Maintain a `README.md` file with project overview and usage instructions with every major change; 
  ignore minor changes. Make sure it is concise and focus on features
- Use Google-style docstrings to describe the purpose and behavior of functions and classes
  immediately after the end of the function or class definition
- Always implement logging using the `logging` package
- When logging, every function should log at least once
- Include inline comments for complex logic and business rules

## Testing
- Follow the AAA pattern: Arrange, Act, Assert
- Place tests in the `tests` directory, mirroring the `src` structure
- NEVER skip tests - broken tests should be fixed immediately or addressed in the code they test
- Use `pytest` for testing and ensure all tests pass before merging code
- Always write unit, integration, and e2e tests for all new features and bug fixes
- Always mock read from *.txt and *.json files in tests, 
  never read from them directly because they are not available in the test environment
- Maintain good test coverage (aim for 80%+ for critical paths) and provide coverage reports
- Write descriptive test names that explain the expected behavior
- Use test doubles (mocks, stubs, spies) appropriately
- Keep tests fast, isolated, and deterministic

## Your Permission
- Never delete files without explicit permission from the user every time
- Never read, edit, or delete *.txt or *.json files without explicit permission from the user
- Never commit secrets or credential files
- Never read files with 'api_token' or 'api_key' in the name
- Suggest improvements and alternative approaches when relevant