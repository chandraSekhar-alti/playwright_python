# Playwright Python Tests for MyInfo Page, Home Page Sidebar, and Client Center Page Validation

This repository contains Playwright tests implemented in Python for various functionalities on a website. The tests cover filling out and submitting the MyInfo page, validating the sidebar functionality on the home page, and testing the client center page.

## Test Files

### 1. myInfo_test.py

#### Description
This test file focuses on filling out the MyInfo page on the website using Playwright with Python. It covers various scenarios related to data entry, form submission, and validation.

#### Test Scenarios
- Data entry for personal details.
- Selection of options in dropdowns.
- Uploading files.
- Submitting the form.
- Validating success messages and other elements.

### 2. home_page_sidebar_validation_test.py

#### Description
This test file validates the functionality of the sidebar on the home page. It uses Playwright with Python to interact with the sidebar menu, hover over items, and perform actions based on the selected item.

#### Test Scenarios
- Hovering over sidebar menu items.
- Clicking on sidebar menu items.
- Verifying expected UI elements on the home page.

### 3. help_center_test.py

#### Description
This test file focuses on validating the client center page and its functionality. It utilizes Playwright with Python to interact with elements on the client center page and ensures that expected behaviors are met.

#### Test Scenarios
- Interacting with various elements on the client center page.
- Verifying the functionality of client center features.
- Ensuring proper error handling and success messages.

## Prerequisites

- Python installed on your machine.
- Playwright Python package installed (`pip install playwright`).
- Dependencies installed (`playwright install`).

## Running the Tests

1. Clone the repository:
```bash
git clone <repository_url>

repository_url = https://github.com/chandraSekhar-alti/playwright_python_POM

2. Navigate to the project directory:
cd <project_directory>

3. Run the tests using Playwright test runner:
playwright test

4. run the tests using pytest runner:
pytest ./tests/


Configuration :-
* Configuration settings are stored in the .env file.
* Adjust the .env file to match your environment and test requirements.

License
This project is licensed under the MIT License

Replace `<repository_url>` and `<project_directory>` with the actual repository URL and project directory. Adjust the description and test scenarios sections based on your project's specifics.

## allure reports step

$ pip install allure-pytest
$ py.test --alluredir=allure-report ./tests
$ allure serve allure-report
