import pytest
from pages.home_page import HomePage
from pages.integrations_page import IntegrationsPage


@pytest.mark.usefixtures("driver")
class TestLambdaTestAdvanced:

    def test_scenario(self, driver):
        home_page = HomePage(driver)
        integrations_page = IntegrationsPage(driver)

        # 1. Navigate to https://www.lambdatest.com.
        home_page.navigate_to_home()

        # 2. Perform an explicit wait till the time all the elements in the DOM are available.
        # Handled by the find_element and find_elements methods in BasePage

        # 3. Scroll to the WebElement ‘Explore all Integrations’ using the scrollIntoView() method.
        home_page.scroll_to_element(home_page.EXPLORE_INTEGRATIONS_LINK)

        # 4. Click on the link and ensure that it opens in the new tab.
        existing_handles = driver.window_handles
        home_page.click_explore_integrations()
        home_page.switch_to_new_tab(existing_handles)

        # 5. Save the window handles in a List (or array). Print the window handles.
        all_handles = driver.window_handles
        print("Window Handles:", all_handles)
        assert len(all_handles) == 2

        # 6. Verify whether the URL is the same as the expected URL.
        expected_integrations_url = "https://www.lambdatest.com/integrations"
        assert driver.current_url == expected_integrations_url, f"Expected URL: {expected_integrations_url}, Actual URL: {driver.current_url}"

        # 7. On that page, scroll to the page where the WebElement (Codeless Automation) is present.
        integrations_page.scroll_to_codeless_automation()

        # 8. Click the ‘INTEGRATE TESTING WHIZ WITH LAMBDATEST’ link.
        integrations_page.click_testing_whiz_link()

        # 9. Check if the title of the page is ‘TestingWhiz Integration With LambdaTest’.
        expected_testingwhiz_title = "TestingWhiz Integration With LambdaTest"
        assert driver.title == expected_testingwhiz_title, f"Expected Title: {expected_testingwhiz_title}, Actual Title: {driver.title}"

        # 10. Close the current window using the window handle obtained in step (5).
        driver.close()

        # Switch back to the original window
        home_page.switch_to_tab(all_handles[0])

        # 11. Print the current window count.
        print("Current Window Count:", len(driver.window_handles))
        assert len(driver.window_handles) == 1

        # 12. On the current window, set the URL to https://www.lambdatest.com/blog.
        driver.get("https://www.lambdatest.com/blog")

        # 13. Click on the ‘Community’ link and verify whether the URL is https://community.lambdatest.com/.
        home_page.click_community_link()
        expected_community_url = "https://community.lambdatest.com/"
        assert driver.current_url == expected_community_url, f"Expected URL: {expected_community_url}, Actual URL: {driver.current_url}"

        # 14. Close the current browser window.
        driver.quit()  # Already handled in the teardown of the fixture
