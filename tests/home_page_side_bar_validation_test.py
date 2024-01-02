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
    home_page = HomePageSideBar(page)
    expect(home_page.client_brand_banner).to_be_visible()

    for item in side_bar_list_inactive_items:
        try:
            home_page.home_page_sidebar_validation(
                item, int(os.getenv("semi_time_wait"))
            )

        except Exception as e:
            print(f"Error in loop iteration for item {item}: {e}")


def test_home_page_search_bar_validation(page):
    home_page = HomePageSideBar(page)
    expect(home_page.search_bar_logo).to_be_visible()
    home_page.search_bar_input_field.fill("Leave")
    expect(home_page.leave_section_side_bar).to_be_visible()
    home_page.leave_section_side_bar.click()
    page.wait_for_timeout(2000)
    expect(home_page.leave_breadcrum_text).to_be_visible()
    url_to_assert = f'{os.getenv("Home_page_URL")}/leave/viewLeaveList'

    expect(page).to_have_url(url_to_assert)
