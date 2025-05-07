# hao-backprop-test

A test project for Backprop integration using Python and Flask.

## Project Overview

This is a lightweight, single-component Python 3 Flask-based HTTP server implementation developed as a test environment for Backprop integration. The application serves a simple "Hello, World!" response to all incoming HTTP requests on localhost port 3000.

## Technology Stack

- **Runtime**: Python 3 (3.8+)
- **Framework**: Flask
- **Dependencies**: See `requirements.txt`

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

You can run the application using either of these methods:

```bash
# Method 1: Direct Python execution
python3 app.py

# Method 2: Using Flask CLI
flask run --host=127.0.0.1 --port=3000
```

The server will start and listen on http://localhost:3000

## Technology Transition

This project was migrated from a Node.js implementation to Python/Flask to:
- Enable seamless integration with Python-native AI libraries
- Simplify orchestration with other Python-based services
- Improve maintainability within a unified Python backend environment
- Provide better performance monitoring and debugging capabilities

The migration maintains exact functional parity with the original Node.js implementation.