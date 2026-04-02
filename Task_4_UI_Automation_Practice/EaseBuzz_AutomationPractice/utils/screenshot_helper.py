import os
from datetime import datetime

from selenium.common.exceptions import WebDriverException

from utils.config import logger

SCREENSHOTS_ROOT = os.path.join(os.getcwd(), ".screenshots")
ASSERTIONS_DIR = os.path.join(SCREENSHOTS_ROOT, "assertions")
FAILURES_DIR = os.path.join(SCREENSHOTS_ROOT, "failures")


def _ensure_dir(path: str) -> None:
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        logger.error("Cannot create screenshot directory %s: %s", path, e)
        raise


def capture_assertion(driver, test_name: str, label: str) -> str:
    """Save a screenshot as evidence at assertion time (typically after a passing assert)."""
    _ensure_dir(ASSERTIONS_DIR)
    safe_test = test_name.replace("::", "_").replace("/", "_").replace("[", "_").replace("]", "_")
    safe_label = "".join(c if c.isalnum() or c in "-_" else "_" for c in label)[:80]
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]
    filename = f"{safe_test}__{safe_label}__{ts}.png"
    path = os.path.join(ASSERTIONS_DIR, filename)
    try:
        driver.save_screenshot(path)
    except (WebDriverException, OSError) as e:
        logger.error("Assertion screenshot failed (%s): %s", path, e)
        raise RuntimeError(f"Could not save assertion screenshot: {path}") from e
    return path


def capture_failure(driver, nodeid: str, exc_name: str) -> str:
    """Save a screenshot when a test fails (call phase)."""
    _ensure_dir(FAILURES_DIR)
    safe = nodeid.replace("::", "_").replace("/", "_")
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{safe}_{exc_name}_{ts}.png"
    path = os.path.join(FAILURES_DIR, filename)
    try:
        driver.save_screenshot(path)
    except (WebDriverException, OSError) as e:
        logger.error("Failure screenshot failed (%s): %s", path, e)
        raise RuntimeError(f"Could not save failure screenshot: {path}") from e
    return path



