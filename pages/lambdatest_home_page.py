from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LambdaTestHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.weekday_checkbox_parent_locator = (By.ID, "chip_cdu_weekday_01")
        self.weekday_checkbox_input_locator = (By.CSS_SELECTOR, "input[name='weekdayNoTimeSelection']")
        self.checkmark_span_locator = (By.CSS_SELECTOR, "span[class='checkmark']")

    def navigate_to_home(self):
        self.driver.get("https://www.lambdatest.com")
        print(f"Navigated to: {self.driver.current_url}")

    def wait_for_dom_ready(self, timeout=30):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.XPATH, "//*")))
        print("DOM elements are available.")

    def get_weekday_checkbox_parent(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(self.weekday_checkbox_parent_locator)
        )

    def get_weekday_checkbox_input(self, parent_element):
        return parent_element.find_element(*self.weekday_checkbox_input_locator)

    def get_checkmark_span(self, parent_element):
        return parent_element.find_element(*self.checkmark_span_locator)

    def get_initial_checkbox_state(self, input_element):
        return input_element.is_selected()

    def click_checkmark(self, checkmark_element):
        checkmark_element.click()
        print("Clicked the checkmark.")

    def wait_for_checkbox_state_change(self, input_element, initial_state, timeout=10):
        expected_value = '0' if initial_state else '1'
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"input[name='weekdayNoTimeSelection'][data-val-current='{expected_value}']"))
        )

    def get_final_checkbox_state(self, input_element):
        return input_element.is_selected()
