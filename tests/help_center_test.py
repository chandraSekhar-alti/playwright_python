from playwright.sync_api import Page, expect
from pages.help_center_page import HelpCenterPage
from dotenv import load_dotenv, find_dotenv
import os

def test_help_center_validation(page):
    help_center_page = HelpCenterPage(page)
    expect(help_center_page.question_mark_symbol).to_be_visible()

    # Get popup after a specific action (e.g., click)
    # page handling (The below code handel the new pages that are automatically open when click on a element)
    with page.expect_popup() as popup_info:
        help_center_page.question_mark_symbol.click()

    newPage = popup_info.value
    newPage.wait_for_load_state()

    help_center_page = HelpCenterPage(newPage)

    expect(help_center_page.search_bar).to_be_visible()
    expect(help_center_page.admin_user_guide_button).to_be_visible()
    help_center_page.admin_user_guide_button.hover()
    newPage.wait_for_timeout(int(os.getenv("hover_time")))
    expect(help_center_page.search_bar).to_be_visible()
    expect(help_center_page.employee_user_guide_button).to_be_visible()
    help_center_page.employee_user_guide_button.hover()
    newPage.wait_for_timeout(int(os.getenv("hover_time")))
    expect(help_center_page.search_bar).to_be_visible()
    expect(help_center_page.FAQ_button).to_be_visible()
    help_center_page.FAQ_button.hover()
    newPage.wait_for_timeout(int(os.getenv("hover_time")))
    expect(help_center_page.search_bar).to_be_visible()
    expect(help_center_page.mobile_App_button).to_be_visible()
    help_center_page.mobile_App_button.hover()
    newPage.wait_for_timeout(int(os.getenv("hover_time")))

    help_center_page.admin_user_guide_button.click()
    newPage.wait_for_timeout(int(os.getenv("small_time_wait")))

    page.bring_to_front()
    page.wait_for_timeout(int(os.getenv("small_time_wait")))


def test_help_center_page_search_bar_validation(page):
    help_center_page = HelpCenterPage(page)
    expect(help_center_page.question_mark_symbol).to_be_visible()

    # Get popup after a specific action (e.g., click)
    # page handling (The below code handel the new pages that are automatically open when click on a element)
    with page.expect_popup() as popup_info:
        help_center_page.question_mark_symbol.click()

    newPage = popup_info.value
    newPage.wait_for_load_state()

    help_center_page = HelpCenterPage(newPage)

    expect(help_center_page.orange_hrm_logo).to_be_visible()
    expect(help_center_page.search_bar).to_be_visible()
    help_center_page.search_bar.fill("sample text entering here for validation purpose")
    expect(help_center_page.footer_hrm_text).to_be_visible()
