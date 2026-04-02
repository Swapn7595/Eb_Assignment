#  Folder Structure 



```
EaseBuzz/
├── config/
│   ├── __init__.py                 # Package initialization
│   └── settings.py                 # Configuration (BASE_URL, TIMEOUT, ENDPOINTS)
│
├── core/
│   ├── __init__.py                 # Package initialization
│   ├── api_client.py               # Reusable API client wrapper
│   ├── logger_setup.py             # Structured logging setup
│   └── models.py                   # JSONSchema definitions
│
├── tests/
│   ├── __init__.py                 # Package initialization
│   ├── conftest.py                 # Pytest fixtures & configuration
│   ├── test_api_suite.py           # Main test suite (13 parameterized tests)
│   └── test_api_posts.py           # Basic pytest tests (3 tests)
│
├── output/
│   └── first_5_posts.json          # Generated JSON output from script
│
├── logs/
│   └── api_automation.log          # Execution logs (console + file)
│
├── docs/
│   ├── README.md                   # Framework guide
│
├── requirements.txt                # Python dependencies
├── pytest.ini                      # Pytest configuration
└── .gitignore                      # Git ignore rules
```

---



---

##  Quick Start

### From Root Directory
```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run standalone script
python scripts/api_automation_posts.py

# View logs
type logs\api_automation.log

# View generated output
type output\first_5_posts.json

# Read documentation
type docs\README.md
```



## Package Imports

### In Test Files
```python
from core import APIClient, setup_logger, SCHEMA_MAP
from config import RESPONSE_TIME_THRESHOLD, ENDPOINTS
```

### In Scripts
```python
from core import APIClient
from config import ENDPOINTS
```

### In Core Modules
```python
from config import BASE_URL, TIMEOUT, LOG_LEVEL, LOG_FILE
```

---

## Next Steps

1. **Add More Endpoints**: Update `config/settings.py` + `core/models.py`
2. **Add Performance Tests**: New test file in `tests/`
---


