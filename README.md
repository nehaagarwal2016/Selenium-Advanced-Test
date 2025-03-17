# LambdaTest Checkbox Interaction Test

This project contains a Selenium test written in Python using pytest, following the Page Object Model, to interact with a checkbox on the LambdaTest website. The test is configured to run in parallel on LambdaTest Cloud Selenium Grid.

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
    * Ensure you have set `LT_USERNAME` and `LT_ACCESS_KEY` as Gitpod secrets (Workspace Settings -> Secrets). The `conftest.py` will automatically retrieve them.

## Running the Test on Gitpod (LambdaTest Cloud)

1.  Ensure you have the `.gitpod.yml` file configured in the repository (as provided).
2.  Open the repository in Gitpod (using the single-click Gitpod button).
3.  Gitpod will automatically:
    * Install the necessary Python dependencies.
    * Execute the pytest command to run the test in parallel on LambdaTest.

## Viewing Test Results

* The console output in Gitpod will show the progress of the tests and any assertions.
* The LambdaTest Session IDs for each parallel test (for Chrome and Firefox) will be printed in the console after the drivers are quit.
* You can view detailed test results, including network logs, video recordings, and screenshots, on the LambdaTest platform by navigating to the Automation section and searching for your build name ("LambdaTest Checkbox Test") or test name.

## Test Details

The project follows the Page Object Model:

* **`page_objects/lambdatest_home_page.py`:** Defines the `LambdaTestHomePage` class, which encapsulates the locators and interactions for the LambdaTest homepage elements related to the checkbox.
* **`tests/test_lambdatest_checkbox.py`:** Contains the test case `test_checkbox_interaction`, which uses the `LambdaTestHomePage` object to perform the test steps.

The test case:

* Navigates to `https://www.lambdatest.com`.
* Waits for the DOM to be ready.
* Locates the parent, input, and checkmark elements of the weekday checkbox.
* Checks the initial state of the checkbox.
* Clicks the checkmark to toggle the checkbox.
* Waits for the checkbox state to change.
* Verifies that the final state is different from the initial state.

## Parallel Execution

The `pytest -n auto` command in `.gitpod.yml` and the `pytest-xdist` plugin ensure that the test is run in parallel across the specified browsers (Chrome and Firefox) on the LambdaTest grid.

## Final Test IDs

After the test execution is complete, the LambdaTest Session IDs will be printed in the Gitpod console. Please note these IDs for your submission.
