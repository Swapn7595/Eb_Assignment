import json
import pytest
from jsonschema import validate
from core import APIClient, setup_logger, SCHEMA_MAP
from config import ENDPOINTS

logger = setup_logger(__name__)


def test_status_code(api_client):
    """Test that posts endpoint returns 200."""
    response, _ = api_client.get(ENDPOINTS["posts"])
    assert response.status_code == 200


def test_each_post_has_required_keys(api_client):
    """Test that each post has required fields."""
    response, _ = api_client.get(ENDPOINTS["posts"])
    posts = response.json()
    assert isinstance(posts, list)
    
    required_keys = {"userId", "id", "title", "body"}
    for post in posts:
        assert required_keys.issubset(post.keys())


def test_save_first_5_posts(api_client):
    """Test saving first 5 posts to JSON file in output folder."""
    from pathlib import Path
    
    response, _ = api_client.get(ENDPOINTS["posts"])
    posts = response.json()
    first_5 = posts[:5]
    
    # Save to actual output folder
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    file_path = output_dir / "first_5_posts.json"
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(first_5, f, indent=2, ensure_ascii=False)

    # Verify file was created
    assert file_path.exists(), f"File not created at {file_path}"
    
    # Verify file contains correct data
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) == 5, f"Expected 5 posts, got {len(data)}"
    
    # Validate each post against schema
    for idx, post in enumerate(data):
        validate(instance=post, schema=SCHEMA_MAP["posts"])
    
    logger.info(f"[OK] Successfully saved first 5 posts to {file_path}")
