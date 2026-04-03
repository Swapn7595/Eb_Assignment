from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import test
from .base_page import BasePage
from pages.locators import PracticePageLocators
from utils.config import logger, test_step_logger



class PracticePage(BasePage):
    def select_dropdown_option(self, visible_text):
        try:
            dropdown = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(PracticePageLocators.DROPDPOWN_EXAMPLE)
            )
            self.click_element_direct(dropdown)
            test_step_logger.log_step("Clicked on dropdown")

            option_locator = (
                PracticePageLocators.DROPDOWN_OPTION[0],
                PracticePageLocators.DROPDOWN_OPTION[1].format(visible_text=visible_text)
            )

            option = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(option_locator)
            )
            self.click_element_direct(option)

            test_step_logger.log_step(f"Selected option: {visible_text}")
            return True   #  success

        except Exception as e:
            test_step_logger.log_step(f"Dropdown selection failed: {e}")
            return False   # failure
        
        
    def select_radio_button_option(self, value):
        try:
            radio_locator = (
                PracticePageLocators.RADIO_BUTTON_OPTION[0],
                PracticePageLocators.RADIO_BUTTON_OPTION[1].format(value=value)
            )
            radio_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(radio_locator)
            )
            self.click_element_direct(radio_button)
            test_step_logger.log_step(f"Selected radio button with value: {value}")
            return True   # success

        except Exception as e:
            test_step_logger.log_step(f"Radio button selection failed: {e}")
            return False   # failure
        