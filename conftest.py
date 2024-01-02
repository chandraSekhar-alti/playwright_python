from playwright.sync_api import Page, expect
import pytest
from playwright.sync_api import sync_playwright
import re
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    page = browser.new_page()
    page.set_default_timeout(
        int(os.getenv("large_time_wait"))
    )  # Set default timeout to 6000 milliseconds (6 seconds)
    yield page
    page.close()


@pytest.fixture(scope="function", autouse=True)
def global_setup(page):
    # Open the website
    page.goto(os.getenv("Base_URL"), timeout=int(os.getenv("URL_load_time")))
    page.set_viewport_size({"width": 1366, "height": 768})

    # Provide credentials (replace these with your actual credentials)
    page.locator('//input[@name="username"]').fill(os.getenv("orangeHrmUserName"))
    page.locator('//input[@type="password"]').fill(os.getenv("orangeHrmPassword"))
    page.locator("//button[text()=' Login ']").click()
    page.wait_for_timeout(int(os.getenv("medium_time_wait")))
    expect(page).to_have_url(
        re.compile(r"/web/index.php/dashboard/index"),
        timeout=int(os.getenv("medium_time_wait")),
    )


@pytest.fixture(autouse=True, scope="function")
def setup(request, page):
    # Setup code before the test
    yield

    # Teardown code after the test
    def tear_down():
        print("Running tear_down() after the test:", request.node.name)
        # Add your tear_down() logic here
        page.locator('//li[@class="oxd-userdropdown"]/span').click()
        page.wait_for_timeout(int(os.getenv("small_time_wait")))
        page.locator("//a[text()='Logout']").click()
        expect(page).to_have_url(
            os.getenv("base_url"), timeout=int(os.getenv("medium_time_wait"))
        )
        print(f"{request.node.name} test successfully completed !!!!!!!!!!!!!!!")

    request.addfinalizer(tear_down)
