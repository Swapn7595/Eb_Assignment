class AutomationError(Exception):
    """Base class for automation layer errors."""


class TestDataError(AutomationError):
    """Raised when ``data/test_data.json`` is missing, invalid, or malformed."""
