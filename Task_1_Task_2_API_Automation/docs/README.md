# API Automation Framework - 


Professional-grade API automation framework built for JSONPlaceholder API with:
- Parameterized test suite (13 tests covering 3 endpoints)
- JSONSchema validation
- Response time monitoring (< 2 seconds threshold)
- Structured logging (console + file output)
- Reusable API client
- Comprehensive assertions

---

## Folder Structure

```
EaseBuzz/
├── config/
│   ├── __init__.py                 # Package init
│   └── settings.py                 # Configuration
│
├── core/
│   ├── __init__.py                 # Package init
│   ├── api_client.py               # API client wrapper
│   ├── logger_setup.py             # Logging setup
│   └── models.py                   # JSONSchema definitions
│
├── tests/
│   ├── __init__.py                 # Package init
│   ├── conftest.py                 # Pytest fixtures
│   ├── test_api_suite.py           # Main test suite (13 tests)
│   └── test_api_posts.py           # Basic tests
│
├── output/
│   └── first_5_posts.json          # Generated JSON output
│
├── logs/
│   └── api_automation.log          # Execution logs
│
├── docs/
│   ├── README.md                   # This file
│
├── requirements.txt                # Python dependencies
├── pytest.ini                      # Pytest configuration
└── .gitignore                      # Git ignore rules
```

---



### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run All Tests
```bash
pytest
```

### 3. Run Specific Tests
```bash
# Test only posts endpoint
pytest -k "posts" -v

# Test only response time checks
pytest -k "response_time" -v

# Test only schema validation
pytest -k "schema_validation" -v
```

### 4. Run Standalone Script
```bash
python scripts/api_automation_posts.py
```

### 5. Generate HTML Report
```bash
pytest --html=report.html --self-contained-html
```

---

## Test Suite Details

### Total Tests: 12 (All Passing )
- **Status Code**: 3 tests (posts, comments, users)
- **Response Time**: 3 tests (< 2 seconds threshold)
- **Schema Validation**: 3 tests (JSONSchema for 610 items)
- **Content Validation**: 3 tests (fields, integrity, type)

### Test Execution
```
pytest test_api_suite.py -v
============================= 13 passed in 10.47s =============================
```

---

## Validation Features

### Levels of Validation
1. HTTP Status Code (200)
2. Response Time (< 2 seconds)
3. JSONSchema validation
4. Required fields check
5. Data type validation
6. Content integrity check
7. Content-type validation

### Schema Examples

**Post Schema**
```python
{
    "userId": integer (> 0),
    "id": integer (> 0),
    "title": string (non-empty),
    "body": string (non-empty)
}
```

**Comment Schema**
```python
{
    "postId": integer (> 0),
    "id": integer (> 0),
    "name": string (non-empty),
    "email": string (email format),
    "body": string (non-empty)
}
```

**User Schema**
```python
{
    "id": integer (> 0),
    "name": string (non-empty),
    "username": string (non-empty),
    "email": string (email format),
    "phone": string (optional),
    "website": string (optional)
}
```

---

## Logging

All test executions logged to `logs/api_automation.log`:

```
2026-04-01 14:32:15 - api_client - INFO - APIClient initialized
2026-04-01 14:32:15 - api_client - INFO - GET request to: https://jsonplaceholder.typicode.com/posts
2026-04-01 14:32:16 - api_client - INFO - Response received - Status: 200, Response Time: 0.856s
2026-04-01 14:32:16 - test_api_suite - INFO - ✓ posts schema validation passed for 100 items
```

---

## Configuration

Edit `config/settings.py` to customize:

```python
BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10  # seconds
RESPONSE_TIME_THRESHOLD = 2.0  # seconds
ENDPOINTS = {
    "posts": "/posts",
    "comments": "/comments",
    "users": "/users"
}
LOG_LEVEL = "INFO"
LOG_FILE = "logs/api_automation.log"
```

---

## API Client Usage

Reusable for other endpoints:

```python
from core import APIClient
from config import ENDPOINTS

with APIClient() as client:
    response, response_time = client.get(ENDPOINTS["posts"])
    print(f"Status: {response.status_code}")
    print(f"Time: {response_time:.3f}s")
    data = response.json()
```

---

## Dependencies

```
requests==2.31.0       # HTTP client
pytest==7.4.3          # Testing
jsonschema==4.20.0     # Schema validation
python-dotenv==1.0.0   # Environment variables
```

---


### Run with Markers
```bash
pytest -m "api" -v
```

### Parallel Execution
```bash
pip install pytest-xdist
pytest -n auto -v
```

### Coverage Report
```bash
pip install pytest-cov
pytest --cov=. --cov-report=html
```

### Verbose Debug Output
```bash
pytest -vv --log-cli-level=DEBUG
```



