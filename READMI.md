# Playwright Python Tests for MyInfo Page and Home Page Sidebar Validation

This repository contains Playwright tests implemented in Python for filling out and submitting the MyInfo page on a website and validating the functionality of the sidebar on the home page.

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

## Prerequisites

- Python installed on your machine.
- Playwright Python package installed (`pip install playwright`).
- Dependencies installed (`playwright install`).

## Running the Tests

1. Clone the repository:
```bash
git clone <repository_url>

2. Navigate to the project directory:
cd <project_directory>

3. Run the tests using Playwright test runner:
playwright test


Configuration :-
* Configuration settings are stored in the .env file.
* Adjust the .env file to match your environment and test requirements.

License
This project is licensed under the MIT License

Replace `<repository_url>` and `<project_directory>` with the actual repository URL and project directory. Adjust the description and test scenarios sections based on your project's specifics.
