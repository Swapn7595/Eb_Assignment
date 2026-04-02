import logging
from typing import Optional

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from utils.element_highlighter import ElementHighlighter

logger = logging.getLogger("Practice UI Application")

DEFAULT_TIMEOUT = 15


class BasePage:
    def __init__(self, driver, enable_highlight: bool = True, timeout: int = DEFAULT_TIMEOUT):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)
        self.highlighter = ElementHighlighter(driver) if enable_highlight else None

    def wait_for(self, condition, timeout: Optional[int] = None):
        """Explicit wait for a custom expected condition (callable or EC)."""
        seconds = timeout if timeout is not None else self.timeout
        wait = WebDriverWait(self.driver, seconds)
        try:
            return wait.until(condition)
        except TimeoutException:
            logger.error("Timed out after %ss waiting for condition", seconds)
            raise

    def open(self, url):
        if self.driver.current_url != url:
            logger.info(f"Opening URL: {url}")
            try:
                self.driver.get(url)
            except WebDriverException as e:
                logger.error("Navigation failed to %s: %s", url, e)
                raise
            self.wait_for(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
        else:
            logger.info(f"URL already open: {url}")

    def find_element(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            if self.highlighter:
                self.highlighter.highlight_element(element, duration=1)
            return element
        except TimeoutException:
            logger.error(f"Timeout while waiting for element with locator: {locator}")
            logger.error(f"Current URL: {self.driver.current_url}")
            logger.error(f"Page Source: {self.driver.page_source[:500]}...")
            raise

    def find_clickable(self, locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            if self.highlighter:
                self.highlighter.highlight_element(element, duration=1)
            return element
        except TimeoutException:
            logger.error(f"Timeout waiting for clickable element: {locator}")
            logger.error(f"Current URL: {self.driver.current_url}")
            raise

    def click(self, locator):
        logger.info(f"Clicking on element with locator: {locator}")
        element = self.find_clickable(locator)
        if self.highlighter:
            self.highlighter.highlight_and_click(element)
        else:
            element.click()

    def enter_text(self, locator, text):
        logger.info(f"Entering text into element with locator: {locator}")
        element = self.find_clickable(locator)
        if self.highlighter:
            self.highlighter.highlight_and_send_keys(element, text)
        else:
            element.clear()
            element.send_keys(text)

    def click_element_direct(self, element):
        logger.info("Clicking element directly")
        if self.highlighter:
            self.highlighter.highlight_and_click(element)
        else:
            element.click()

    def get_elements(self, locator):
        logger.info(f"Finding elements with locator: {locator}")
        try:
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            logger.error("Timeout waiting for visible elements: %s", locator)
            logger.error("Current URL: %s", self.driver.current_url)
            raise
