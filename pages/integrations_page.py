from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class IntegrationsPage(BasePage):
    """Page object for the Integrations page."""

    CODELESS_AUTOMATION_HEADING = (By.XPATH, "//h2[contains(text(),'Codeless Automation')]")
    TESTING_WHIZ_LINK = (By.LINK_TEXT, "INTEGRATE TESTING WHIZ WITH LAMBDATEST") # Link Text

    def __init__(self, driver):
        super().__init__(driver)

    def scroll_to_codeless_automation(self):
        """Scrolls to the 'Codeless Automation' heading."""
        self.scroll_to_element(self.CODELESS_AUTOMATION_HEADING)

    def click_testing_whiz_link(self):
        """Clicks the 'INTEGRATE TESTING WHIZ WITH LAMBDATEST' link."""
        self.click(self.TESTING_WHIZ_LINK)
