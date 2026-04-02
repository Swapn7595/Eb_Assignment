import pytest
import json
from jsonschema import validate, ValidationError
from typing import Any, List
from core import APIClient, setup_logger, SCHEMA_MAP
from config import RESPONSE_TIME_THRESHOLD, ENDPOINTS

logger = setup_logger(__name__)


class TestAPIAutomation:
    """Test suite for API endpoints."""

    @pytest.mark.parametrize("endpoint_name,endpoint_path", [
        ("posts", ENDPOINTS["posts"]),
        ("comments", ENDPOINTS["comments"]),
        ("users", ENDPOINTS["users"])
    ])
    def test_status_code_200(self, api_client, endpoint_name, endpoint_path):
        """Validate that each endpoint returns status code 200."""
        logger.info(f"Testing status code for {endpoint_name}")
        response, _ = api_client.get(endpoint_path)
        assert response.status_code == 200, \
            f"Expected status 200 for {endpoint_name}, got {response.status_code}"
        logger.info(f"{endpoint_name} returned status 200")

    @pytest.mark.parametrize("endpoint_name,endpoint_path", [
        ("posts", ENDPOINTS["posts"]),
        ("comments", ENDPOINTS["comments"]),
        ("users", ENDPOINTS["users"])
    ])
    def test_response_time_threshold(self, api_client, endpoint_name, endpoint_path):
        """Validate that response time is under the threshold."""
        logger.info(f"Testing response time for {endpoint_name}")
        response, response_time = api_client.get(endpoint_path)
        
        assert response_time < RESPONSE_TIME_THRESHOLD, \
            f"Response time {response_time:.3f}s exceeds threshold {RESPONSE_TIME_THRESHOLD}s for {endpoint_name}"
        logger.info(f"{endpoint_name} response time: {response_time:.3f}s (threshold: {RESPONSE_TIME_THRESHOLD}s)")

    @pytest.mark.parametrize("endpoint_name,endpoint_path", [
        ("posts", ENDPOINTS["posts"]),
        ("comments", ENDPOINTS["comments"]),
        ("users", ENDPOINTS["users"])
    ])
    def test_schema_validation(self, api_client, endpoint_name, endpoint_path):
        """Validate response data against JSON schema."""
        logger.info(f"Testing schema validation for {endpoint_name}")
        response, _ = api_client.get(endpoint_path)
        
        assert response.status_code == 200
        data = response.json()
        
        # Get schema for endpoint
        schema = SCHEMA_MAP.get(endpoint_name)
        assert schema is not None, f"Schema not defined for {endpoint_name}"
        
        # Validate response is a list
        assert isinstance(data, list), f"Response data should be a list for {endpoint_name}"
        assert len(data) > 0, f"Response data is empty for {endpoint_name}"
        
        # Validate each item against schema
        for idx, item in enumerate(data):
            try:
                validate(instance=item, schema=schema)
            except ValidationError as e:
                logger.error(f"Schema validation failed for {endpoint_name} item #{idx}: {str(e)}")
                raise AssertionError(
                    f"Schema validation failed for {endpoint_name} item #{idx}: {str(e)}"
                )
        
        logger.info(f"{endpoint_name} schema validation passed for {len(data)} items")

    def test_posts_required_fields(self, api_client):
        """Validate posts contain required fields: userId, id, title, body."""
        logger.info("Testing posts required fields")
        response, _ = api_client.get(ENDPOINTS["posts"])
        posts = response.json()
        
        required_fields = {"userId", "id", "title", "body"}
        
        for idx, post in enumerate(posts[:10]):  # Check first 10
            missing_fields = required_fields - set(post.keys())
            assert not missing_fields, \
                f"Post #{idx} missing fields: {missing_fields}"
        
        logger.info(f"Posts required fields validation passed")

    def test_posts_content_integrity(self, api_client):
        """Validate posts have meaningful content."""
        logger.info("Testing posts content integrity")
        response, _ = api_client.get(ENDPOINTS["posts"])
        posts = response.json()
        
        for idx, post in enumerate(posts[:5]):
            assert isinstance(post["userId"], int) and post["userId"] > 0
            assert isinstance(post["id"], int) and post["id"] > 0
            assert isinstance(post["title"], str) and len(post["title"]) > 0
            assert isinstance(post["body"], str) and len(post["body"]) > 0
        
        logger.info(f"Posts content integrity validation passed")

    def test_response_content_type(self, api_client):
        """Validate response content types."""
        logger.info("Testing response content types")
        for endpoint_name, endpoint_path in ENDPOINTS.items():
            response, _ = api_client.get(endpoint_path)
            assert "application/json" in response.headers.get("content-type", ""), \
                f"{endpoint_name} response content-type is not JSON"
        
        logger.info(f"Response content-type validation passed for all endpoints")
        
    


