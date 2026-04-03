import os
from datetime import datetime
from selenium.common.exceptions import WebDriverException
from utils.config import logger

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import time






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




class ElementHighlighter:
    """Utility class to highlight elements on the browser"""
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def highlight_element(self, element: WebElement, duration: float = 2):
        """
        Highlight an element with a red border and yellow background
        
        Args:
            element: WebElement to highlight
            duration: Time in seconds to keep the highlight (default: 2)
        """
        try:
            original_style = element.get_attribute('style')
            highlight_style = "border: 3px solid red; background-color: yellow;"
            
            self.driver.execute_script(
                f"arguments[0].setAttribute('style', '{highlight_style}');",
                element
            )
            
            time.sleep(duration)
            
            # Restore original style
            self.driver.execute_script(
                f"arguments[0].setAttribute('style', '{original_style}');",
                element
            )
        except Exception as e:
            print(f"Error highlighting element: {e}")
    
    def highlight_and_click(self, element: WebElement):
        """Highlight element and click it"""
        self.highlight_element(element, duration=1)
        element.click()
    
    def highlight_and_send_keys(self, element: WebElement, text: str):
        """Highlight element and send keys to it"""
        self.highlight_element(element, duration=1)
        element.send_keys(text)