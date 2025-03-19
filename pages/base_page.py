from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Base class for all page objects."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)  # Timeout set to 20 seconds

    def find_element(self, locator):
        """Finds a single element with explicit wait."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """Finds multiple elements with explicit wait."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        """Clicks an element."""
        self.find_element(locator).click()

    def scroll_to_element(self, locator):
        """Scrolls to a specific element using JavaScript."""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_url(self):
        """Gets the current URL."""
        return self.driver.current_url

    def get_title(self):
        """Gets the title of the current page."""
        return self.driver.title

    def switch_to_new_tab(self, existing_handles):
        """Switches to the new tab."""
        new_handle = self.wait.until(lambda driver: any(h not in existing_handles for h in driver.window_handles))
        self.driver.switch_to.window(new_handle)

    def close_current_tab(self):
        """Closes the current tab."""
        self.driver.close()

    def switch_to_tab(self, window_handle):
        """Switches to a specific tab using its handle."""
        self.driver.switch_to.window(window_handle)
