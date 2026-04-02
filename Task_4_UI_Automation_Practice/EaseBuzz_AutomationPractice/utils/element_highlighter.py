import logging
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

logger = logging.getLogger("EaseBuzzApplication")


class ElementHighlighter:
    """Utility class to highlight elements on the browser"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def highlight_element(self, element: WebElement, duration: float = 2):
        try:
            original_style = element.get_attribute("style")
            highlight_style = "border: 3px solid red; background-color: yellow;"

            self.driver.execute_script(
                f"arguments[0].setAttribute('style', '{highlight_style}');",
                element,
            )

            time.sleep(duration)

            self.driver.execute_script(
                f"arguments[0].setAttribute('style', '{original_style}');",
                element,
            )
        except Exception as e:
            logger.warning("Highlight failed (continuing): %s", e)

    def highlight_and_click(self, element: WebElement):
        self.highlight_element(element, duration=1)
        element.click()

    def highlight_and_send_keys(self, element: WebElement, text: str):
        self.highlight_element(element, duration=1)
        element.send_keys(text)
