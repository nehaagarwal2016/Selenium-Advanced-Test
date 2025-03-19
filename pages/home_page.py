from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    """Page object for the LambdaTest homepage."""

    EXPLORE_INTEGRATIONS_LINK = (By.XPATH, "//a[contains(text(),'Explore all Integrations')]")
    COMMUNITY_LINK = (By.CSS_SELECTOR, "a[href='https://community.lambdatest.com/']") # CSS Selector

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_home(self):
        """Navigates to the LambdaTest homepage."""
        self.driver.get("https://www.lambdatest.com/")

    def click_explore_integrations(self):
        """Clicks the 'Explore all Integrations' link."""
        self.click(self.EXPLORE_INTEGRATIONS_LINK)

    def click_community_link(self):
        """Clicks the 'Community' link."""
        self.click(self.COMMUNITY_LINK)
