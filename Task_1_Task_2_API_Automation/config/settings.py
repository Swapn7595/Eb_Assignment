import os
from dotenv import load_dotenv

load_dotenv()

# Base API Configuration
BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10
RESPONSE_TIME_THRESHOLD = 2.0  # seconds

# Endpoints
ENDPOINTS = {
    "posts": "/posts",
    "comments": "/comments",
    "users": "/users"
}

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = "logs/api_automation.log"
