from pages.login_page import LoginPage
from dotenv import load_dotenv, find_dotenv
import re
from playwright.sync_api import Page, expect
import os

# Load environment variables from .env file
load_dotenv(find_dotenv())
base_url = os.getenv("main_url")

def test_example(page):
    # creating the instance for the login page
    loginPage = LoginPage(page)

    # calling the declraed function
    loginPage.navigate_to_url(base_url)

    #explicitly timeout to load the page
    medium_time_wait = int(os.getenv("medium_time_wait"))
    loginPage.page.wait_for_timeout(medium_time_wait)
    
    loginPage.login(os.getenv("orangeHrmUserName"),os.getenv("orangeHrmPassword"))

    #validating the home page URL
    expect(page).to_have_url(re.compile(r"/web/index.php/dashboard/index"))
    print(page.url)
    
