# Selenium-Advanced-Test
# LambdaTest Website Flow Test

This project contains a Selenium test written in Python using pytest to automate a specific flow on the LambdaTest website. The test is configured to run in parallel on LambdaTest Cloud Selenium Grid.

## Prerequisites

* Python 3.x
* pip (Python package installer)
* A LambdaTest account with valid Username and Access Key.

## Setup

1.  Clone this private repository to your local machine or Gitpod environment.
2.  Navigate to the project directory: `cd your_repository`
3.  Install the required dependencies: `pip install -r requirements.txt`

## Configuration

1.  **LambdaTest Credentials:**
    * Open the `conftest.py` file.
    * Replace `"YOUR_LAMBDATEST_USERNAME"` and `"YOUR_LAMBDATEST_ACCESS_KEY"` with your actual LambdaTest credentials.

## Running the Test on Gitpod (LambdaTest Cloud)

1.  Ensure you have the `.gitpod.yml` file configured in the repository (as provided).
2.  Open the repository in Gitpod (using the single-click Gitpod button).
3.  Gitpod will automatically:
    * Install the necessary Python dependencies.
    * Execute the pytest command to run the test in parallel on LambdaTest.

## Viewing Test Results

* The console output in Gitpod will show the progress of the tests and any assertions.
* The LambdaTest Session IDs for each parallel test (for Chrome and Firefox) will be printed in the console after the drivers are quit.
* You can view detailed test results, including network logs, video recordings, and screenshots, on the LambdaTest platform by navigating to the Automation section and searching for your build name ("LambdaTest Flow Test") or test name.

## Test Details

The `tests/test_lambdatest_flow.py` file contains a single test case:

* `test_lambdatest_website_flow(driver)`:
    * Navigates to `https://www.lambdatest.com`.
    * Waits for all DOM elements to be available.
    * Scrolls to and clicks the 'Explore all Integrations' link, which opens in a new tab.
    * Verifies the URL of the new tab.
    * Scrolls to the 'Codeless Automation' section on the integrations page.
    * Clicks the 'INTEGRATE TESTING WHIZ WITH LAMBDATEST' link.
    * Verifies the title of the TestingWhiz integration page.
    * Closes the TestingWhiz integration tab.
    * Navigates to `https://www.lambdatest.com/blog` in the original tab.
    * Clicks the 'Community' link and verifies the URL.
    * Closes the browser.

## Parallel Execution

The `pytest -n auto` command in `.gitpod.yml` and the `pytest-xdist` plugin ensure that the test is run in parallel across the specified browsers (Chrome and Firefox) on the LambdaTest grid.

## Final Test IDs

After the test execution is complete, the LambdaTest Session IDs will be printed in the Gitpod console. Please note these IDs for your submission.
