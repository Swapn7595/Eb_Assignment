import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from pages.practice_page import PracticePage
from pages.locators import PracticePageLocators

from utils.config import *
#from utils.screenshot_manager import capture_assertion
import time
from utils.helper import *

 
 
 
def test_dropdown_selection(driver, config, request):
    """Test dropdown selection on practice page"""
    try:
        test_step_logger.log_step("Starting test: Dropdown Selection")
        
        # Load test data
        with open('data/test_data.json') as f:
            data = json.load(f)

        base_url = config['base_url']
        test_step_logger.log_step(f"Opening practice page: {base_url}")
        practice_page = PracticePage(driver)
        practice_page.open(base_url)

        # Wait for dropdown to be clickable before action
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "dropdown-class-example"))
        )
        
        # Capture screenshot after selection is complete
        capture_assertion(driver, request.node.name, "before_assertion")
        
        
        test_step_logger.log_step(f"Selecting dropdown option: {data['visible_text']}")
        practice_page.select_dropdown_option(data['visible_text'])
        
        # Wait for dropdown to show selected value before capturing screenshot
        '''WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "dropdown-class-example"), data['visible_text'])
        )'''
        

        # Verify dropdown selection
        dropdown_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "dropdown-class-example"))
        )
        assert data['visible_text'] in dropdown_element.text, \
            f"Expected '{data['visible_text']}' in dropdown, got: {dropdown_element.text}"

        test_step_logger.log_step(f"Dropdown '{data['visible_text']}' selected successfully")
        
        time.sleep(2)  # Small delay to ensure dropdown state is updated screenshot
        # Capture screenshot after assertion passed
        capture_assertion(driver, request.node.name, "after_assertion_passed")
        
    except Exception as e:
        test_step_logger.log_step(f"✗ Test Failed: {e}")
        logger.error(f"Test failed: {e}")
        capture_assertion(driver, request.node.name, "error")
        raise
    
    



def test_radio_button_selection(driver, config, request):
    """Test radio button selection on practice page"""
    try:
        test_step_logger.log_step("Starting test: Radio Button Selection")
        
        # Load test data
        with open('data/test_data.json') as f:
            data = json.load(f)

        base_url = config['base_url']
        test_step_logger.log_step(f"Opening practice page: {base_url}")
        practice_page = PracticePage(driver)
        practice_page.open(base_url)

        test_step_logger.log_step(f"Selecting radio button option: {data['value']}")
        
        # Capture screenshot before assertion
        capture_assertion(driver, request.node.name, "before_assertion")
        
        practice_page.select_radio_button_option(data['value'])
        

        # Verify radio button selection
        radio_button_locator = (
            PracticePageLocators.RADIO_BUTTON_OPTION[0],
            PracticePageLocators.RADIO_BUTTON_OPTION[1].format(value=data['value'])
        )
        radio_button_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(radio_button_locator)
        )
        assert radio_button_element.is_selected(), \
            f"Expected radio button with value '{data['value']}' to be selected."

        test_step_logger.log_step(f" Radio button with value '{data['value']}' selected successfully")
        
        # Capture screenshot after assertion passed
        capture_assertion(driver, request.node.name, "after_assertion_passed")
        
    except Exception as e:
        test_step_logger.log_step(f"Test Failed: {e}")
        logger.error(f"Test failed: {e}")
        capture_assertion(driver, request.node.name, "error")
        raise
    
    

 