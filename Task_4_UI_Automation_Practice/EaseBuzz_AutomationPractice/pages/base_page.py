

import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#from utils.element_highlighter import ElementHighlighter
from utils.helper import *



logger = logging.getLogger('PracticePageTestLogger')

class BasePage:
    def __init__(self, driver, enable_highlight: bool = True):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)  # Increased timeout to 10 seconds
        self.highlighter = ElementHighlighter(driver) if enable_highlight else None

    def open(self, url):
        if self.driver.current_url != url:  # Check if the URL is already open
            logger.info(f"Opening URL: {url}")
            self.driver.get(url)
            # Wait for page to be fully loaded
            WebDriverWait(self.driver, 10).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
        else:
            logger.info(f"URL already open: {url}")

    def find_element(self, locator):
        try:
            # logger.info(f"Finding element with locator: {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            if self.highlighter:
                self.highlighter.highlight_element(element, duration=1)
            return element
        except TimeoutException:
            logger.error(f"Timeout while waiting for element with locator: {locator}")
            logger.error(f"Current URL: {self.driver.current_url}")
            logger.error(f"Page Source: {self.driver.page_source[:500]}...")  # Log first 500 characters of page source
            raise

    def click(self, locator):
        logger.info(f"Clicking on element with locator: {locator}")
        element = self.find_element(locator)
        if self.highlighter:
            self.highlighter.highlight_and_click(element)
        else:
            element.click()

    def enter_text(self, locator, text):
        logger.info(f"Entering text into element with locator: {locator}")
        element = self.find_element(locator)
        if self.highlighter:
            self.highlighter.highlight_and_send_keys(element, text)
        else:
            element.clear()
            element.send_keys(text)

    def click_element_by_locator(self, locator):
        """Find and click element using locator with highlighting"""
        logger.info(f"Clicking element with locator: {locator}")
        element = self.find_element(locator)
        if self.highlighter:
            self.highlighter.highlight_and_click(element)
        else:
            element.click()

    def click_element_direct(self, element):
        """Click element directly with highlighting"""
        logger.info("Clicking element directly")
        if self.highlighter:
            self.highlighter.highlight_and_click(element)
        else:
            element.click()

    def send_keys_to_element_direct(self, element, text):
        """Send keys to element directly with highlighting"""
        logger.info(f"Sending keys to element directly")
        if self.highlighter:
            self.highlighter.highlight_and_send_keys(element, text)
        else:
            element.send_keys(text)

    def get_elements(self, locator):
        """Find multiple elements and highlight them"""
        logger.info(f"Finding elements with locator: {locator}")
        elements = self.wait.until(EC.presence_of_all_elements_located(locator))
        return elements
            
            
            