import pytest

from pages.practice_page import PracticePage
from utils.config import test_step_logger
from utils.practice_test_data import load_practice_test_data


def test_radio_button_example_select(driver, config, radio_value, assertion_screenshot):
    """Radio Button Example: each option can be selected and stays selected"""
    test_step_logger.log_step(f"Radio test for {radio_value}")
    base_url = config["base_url"]
    page = PracticePage(driver)
    page.open(base_url)

    test_step_logger.log_step(f"Click radio {radio_value}")
    page.select_radio(radio_value)

    test_step_logger.log_step("Assert radio is selected")
    assert page.is_radio_selected(radio_value), f"Expected {radio_value} to be selected"
    assertion_screenshot(f"radio_selected_{radio_value}")


def test_dropdown_example_select_option(driver, config, option_text, assertion_screenshot):
    """Dropdown Example: select Option1, Option2, Option3 and verify selection"""
    test_step_logger.log_step(f"Dropdown test for {option_text}")
    base_url = config["base_url"]
    page = PracticePage(driver)
    page.open(base_url)

    test_step_logger.log_step(f"Select '{option_text}' from dropdown")
    page.select_dropdown_by_visible_text(option_text)

    test_step_logger.log_step("Assert displayed selection matches")
    assert page.get_selected_dropdown_text() == option_text
    page.prepare_dropdown_assertion_evidence(option_text)
    try:
        assertion_screenshot(f"dropdown_{option_text}")
    finally:
        page.clear_dropdown_assertion_evidence()


def test_radio_and_dropdown_on_same_page(driver, config, assertion_screenshot):
    """End-to-end: first entry in test_data.json radio_values, then first entry in dropdown_options."""
    test_step_logger.log_step("Combined radio + dropdown flow")
    data = load_practice_test_data()
    radios = data.get("radio_values") or []
    drops = data.get("dropdown_options") or []
    if not radios or not drops:
        pytest.skip("Add at least one value to radio_values and one to dropdown_options in data/test_data.json")

    radio_value = radios[0]
    option_text = drops[0]

    base_url = config["base_url"]
    page = PracticePage(driver)
    page.open(base_url)

    test_step_logger.log_step(f"Select radio {radio_value}")
    page.select_radio(radio_value)

    test_step_logger.log_step("Assert radio is selected")
    assert page.is_radio_selected(radio_value)
    assertion_screenshot("combined_radio_assert")

    test_step_logger.log_step(f"Select dropdown {option_text}")
    page.select_dropdown_by_visible_text(option_text)

    test_step_logger.log_step("Assert displayed selection matches")
    assert page.get_selected_dropdown_text() == option_text
    page.prepare_dropdown_assertion_evidence(option_text)
    try:
        assertion_screenshot("combined_dropdown_assert")
    finally:
        page.clear_dropdown_assertion_evidence()



