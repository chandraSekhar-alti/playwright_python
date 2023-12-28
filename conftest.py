import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    page.set_default_timeout(5000)  # Set default timeout to 5000 milliseconds (5 seconds)
    yield page
    page.close()
