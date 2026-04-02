"""Pytest configuration and fixtures for all tests."""
import pytest
from core import APIClient


@pytest.fixture(scope="module")
def api_client():
    """Fixture to provide API client instance for all tests."""
    client = APIClient()
    yield client
    client.close()
