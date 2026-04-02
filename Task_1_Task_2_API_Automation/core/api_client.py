import requests
import time
from typing import List, Dict, Any
from .logger_setup import setup_logger
from config import BASE_URL, TIMEOUT

logger = setup_logger(__name__)


class APIClient:
    """API Client wrapper with logging and error handling."""

    def __init__(self, base_url: str = BASE_URL, timeout: int = TIMEOUT):
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        logger.info(f"APIClient initialized with base_url: {base_url}")

    def get(self, endpoint: str) -> tuple:
        """
        Perform GET request and return response with response time.
        """
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET request to: {url}")

        start_time = time.time()
        try:
            response = self.session.get(url, timeout=self.timeout)
            response_time = time.time() - start_time

            logger.info(
                f"Response received - Status: {response.status_code}, "
                f"Response Time: {response_time:.3f}s"
            )
            return response, response_time

        except requests.exceptions.Timeout:
            logger.error(f"Timeout error for {url}")
            raise
        except requests.exceptions.ConnectionError:
            logger.error(f"Connection error for {url}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error for {url}: {str(e)}")
            raise

    def close(self):
        """Close the session."""
        self.session.close()
        logger.info("APIClient session closed")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
