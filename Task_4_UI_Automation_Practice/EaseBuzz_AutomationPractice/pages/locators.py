from selenium.webdriver.common.by import By


class PracticePageLocators:
    """UI Automation Practice — Radio Button & Dropdown sections"""

    DROPDOWN = (By.ID, "dropdown-class-example")

    @staticmethod
    def dropdown_option_by_visible_text(visible_text: str):
        """Option under the native <select>; use after opening the dropdown."""
        return (
            By.XPATH,
            f'//select[@id="dropdown-class-example"]/option[normalize-space()="{visible_text}"]',
        )

    @staticmethod
    def radio_by_value(value: str):
        """value: radio1 | radio2 | radio3"""
        return (By.CSS_SELECTOR, f'input[name="radioButton"][value="{value}"]')
