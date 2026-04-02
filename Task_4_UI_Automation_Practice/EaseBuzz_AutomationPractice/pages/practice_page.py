from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, WebDriverException

from pages.locators import PracticePageLocators
from .base_page import BasePage
from utils.config import logger

_STY_ATTR = "data-easebuzz-prev-style"


class PracticePage(BasePage):
    """Page object for https://rahulshettyacademy.com/AutomationPractice/"""

    def select_radio(self, value: str):
        """Select a radio option by value: radio1, radio2, or radio3."""
        logger.info(f"Selecting radio: {value}")
        locator = PracticePageLocators.radio_by_value(value)
        self.click(locator)
        try:
            self.wait_for(lambda d: d.find_element(*locator).is_selected())
        except TimeoutException as e:
            logger.error("Radio %r did not become selected within timeout", value)
            raise TimeoutException(f"Radio '{value}' was not selected after click") from e

    def is_radio_selected(self, value: str) -> bool:
        el = self.find_element(PracticePageLocators.radio_by_value(value))
        return el.is_selected()

    def select_dropdown_by_visible_text(self, visible_text: str):
        """Open the native <select>, then choose an option (more like a real user, options show in headed runs).
        """
        logger.info(f"Selecting dropdown option: {visible_text}")
        self.click(PracticePageLocators.DROPDOWN)
        opt_locator = PracticePageLocators.dropdown_option_by_visible_text(visible_text)
        try:
            self.wait.until(EC.presence_of_element_located(opt_locator))
        except TimeoutException as e:
            logger.error("Dropdown option not found after opening select: %r", visible_text)
            raise TimeoutException(
                f"No <option> with visible text {visible_text!r} under #dropdown-class-example"
            ) from e
        option_el = self.driver.find_element(*opt_locator)
        self.click_element_direct(option_el)
        try:
            self.wait_for(
                lambda d: Select(d.find_element(*PracticePageLocators.DROPDOWN))
                .first_selected_option.text.strip()
                == visible_text
            )
        except TimeoutException as e:
            logger.error("Dropdown did not show selected text %r after option click", visible_text)
            raise TimeoutException(
                f"Dropdown selection did not stick: expected {visible_text!r}"
            ) from e

    def get_selected_dropdown_text(self) -> str:
        dropdown_el = self.find_element(PracticePageLocators.DROPDOWN)
        select = Select(dropdown_el)
        return select.first_selected_option.text.strip()

    def prepare_dropdown_assertion_evidence(self, expected_visible_text: str) -> None:
        """Wait until the UI reports the chosen option, scroll it into view, and highlight the selected so the assertion screenshot matches what was picked.
        """
        try:
            self.wait_for(
                lambda d: Select(d.find_element(*PracticePageLocators.DROPDOWN))
                .first_selected_option.text.strip()
                == expected_visible_text
            )
        except TimeoutException as e:
            logger.error(
                "Assertion evidence: dropdown did not show %r before screenshot",
                expected_visible_text,
            )
            raise TimeoutException(
                f"Cannot prepare evidence screenshot: expected {expected_visible_text!r} selected"
            ) from e
        dropdown_el = self.driver.find_element(*PracticePageLocators.DROPDOWN)
        option_el = Select(dropdown_el).first_selected_option
        try:
            self.driver.execute_script(
                """
                var s = arguments[0], o = arguments[1], k = arguments[2];
                if (!s.getAttribute(k)) s.setAttribute(k, s.getAttribute('style') || '');
                if (!o.getAttribute(k)) o.setAttribute(k, o.getAttribute('style') || '');
                s.scrollIntoView({block: 'center', inline: 'nearest'});
                s.style.setProperty('outline', '4px solid #a00', 'important');
                s.style.setProperty('box-shadow', '0 0 0 3px yellow', 'important');
                o.style.setProperty('outline', '3px solid red', 'important');
                o.style.setProperty('background-color', 'rgba(255,255,0,0.95)', 'important');
                """,
                dropdown_el,
                option_el,
                _STY_ATTR,
            )
        except WebDriverException as e:
            logger.error("Failed to apply dropdown evidence highlight: %s", e)
            raise
        try:
            self.driver.execute_script(
                "return new Promise(function(r) {"
                "requestAnimationFrame(function() { requestAnimationFrame(r); });"
                "});"
            )
        except WebDriverException:
            logger.debug("requestAnimationFrame wait not supported; continuing", exc_info=True)

    def clear_dropdown_assertion_evidence(self) -> None:
        """Restore styles after ``prepare_dropdown_assertion_evidence`` (safe if prepare was not used)."""
        k = _STY_ATTR
        try:
            dropdown_el = self.driver.find_element(*PracticePageLocators.DROPDOWN)
            option_el = Select(dropdown_el).first_selected_option
            self.driver.execute_script(
                """
                function restore(el, key) {
                  if (!el || !el.hasAttribute(key)) return;
                  el.setAttribute('style', el.getAttribute(key) || '');
                  el.removeAttribute(key);
                }
                restore(arguments[0], arguments[1]);
                restore(arguments[2], arguments[1]);
                """,
                dropdown_el,
                k,
                option_el,
            )
        except Exception:
            logger.debug("Dropdown evidence style cleanup skipped", exc_info=True)
