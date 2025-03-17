import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os

# LambdaTest credentials (retrieve from environment variables)
LT_USERNAME = "neha_agarwal1"
LT_ACCESS_KEY = "LT_uBaeQgAiFuphfA0mH8nI0eQUYphdK58o7W8yIbjqwYkQlcu"

@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    desired_caps = {
        "build": "LambdaTest Checkbox Test",
        "name": f"Checkbox Test on {browser}",
        "platform": "Windows 10",
        "browserName": browser,
        "version": "latest",
        "lambdatest:options": {
            "seleniumVersion": "4.0.0",
            "build": "Parallel Testing Build",
            "name": request.node.name,
            "platformVersions": ["10"],
            "browsers": [browser],
            "resolution": "1024x768",
            "network": True,
            "video": True,
            "screenshot": True,
            "console": True
        }
    }

    lt_url = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@hub.lambdatest.com/wd/hub"

    driver = webdriver.Remote(command_executor=lt_url, desired_capabilities=desired_caps)
    yield driver
    session_id = driver.session_id
    driver.quit()
    print(f"\nLambdaTest Session ID: {session_id}")
