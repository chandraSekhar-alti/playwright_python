from pages.home_page_sidebar_validation import HomePageSideBar
from dotenv import find_dotenv, load_dotenv
from playwright.sync_api import expect
import json
import os

load_dotenv(find_dotenv())


json_file_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "data", "homePage.json")
)
print("json_file_path is ::- ", json_file_path)

with open(json_file_path, "r") as json_file:
    loaded_data = json.load(json_file)

side_bar_list_inactive_items = loaded_data["sideBarListInactive_items"]


def test_homepage_sidepanel_validation(page):
    # Instantiate the HomePageSideBar class with the page instance
    homePage = HomePageSideBar(page)
    expect(homePage.client_brand_banner).to_be_visible()

    for item in side_bar_list_inactive_items:
        try:
            homePage.homePagesideBarValidation(item, int(os.getenv("semi_time_wait")))

        except Exception as e:
            print(f"Error in loop iteration for item {item}: {e}")
