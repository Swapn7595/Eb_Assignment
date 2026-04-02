"""
JSON Schema definitions for API endpoints validation.
"""

# Post endpoint schema
POST_SCHEMA = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer", "minimum": 1},
        "id": {"type": "integer", "minimum": 1},
        "title": {"type": "string", "minLength": 1},
        "body": {"type": "string", "minLength": 1}
    },
    "required": ["userId", "id", "title", "body"],
    "additionalProperties": True
}

# Comment endpoint schema
COMMENT_SCHEMA = {
    "type": "object",
    "properties": {
        "postId": {"type": "integer", "minimum": 1},
        "id": {"type": "integer", "minimum": 1},
        "name": {"type": "string", "minLength": 1},
        "email": {"type": "string", "format": "email"},
        "body": {"type": "string", "minLength": 1}
    },
    "required": ["postId", "id", "name", "email", "body"],
    "additionalProperties": True
}

# User endpoint schema
USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer", "minimum": 1},
        "name": {"type": "string", "minLength": 1},
        "username": {"type": "string", "minLength": 1},
        "email": {"type": "string", "format": "email"},
        "phone": {"type": ["string", "null"]},
        "website": {"type": ["string", "null"]}
    },
    "required": ["id", "name", "username", "email"],
    "additionalProperties": True
}

# Schema mapping for endpoints
SCHEMA_MAP = {
    "posts": POST_SCHEMA,
    "comments": COMMENT_SCHEMA,
    "users": USER_SCHEMA
}
