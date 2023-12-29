
# from pages.fixtures import HomePageSideBar
from pages.home_page_sidebar_validation import HomePageSideBar
from dotenv import find_dotenv, load_dotenv
from playwright.sync_api import expect

load_dotenv(find_dotenv())

# Test function using the browser and page fixtures
def test_homepage_sidepanel_validation( page):
    # Instantiate the HomePageSideBar class with the page instance
    homePage = HomePageSideBar(page)

    # Your test logic goes here
    # page.wait_for_timeout(5000)
    expect(homePage.client_brand_banner).to_be_visible()

# You can add more test functions as needed
