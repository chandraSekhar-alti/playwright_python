from playwright.sync_api import expect

from pages.my_info_tab import MyInfoTab

# import os
import re

# import json
# from dotenv import find_dotenv,load_dotenv


def my_info_page_data_inserting(page):
    myInfotab = MyInfoTab(page)

    expect(myInfotab.myInfoLabel).to_be_visible()
    expect(myInfotab.myInfoLabel).to_have_text("My Info")
    myInfotab.myInfoLabel.click()
    page.wait_for_timeout(2000)
    expect(page.url).to_have_url(
        re.compile(r"/web/index.php/pim/viewPersonalDetails/empNumber/7")
    )
    expect(myInfotab.profilePic).to_be_visible()
    expect(myInfotab.tabTitle).to_be_visible()
    expect(myInfotab.tabTitle).to_have_text("Personal Details")

    # expect(myInfotab.firstName)
    myInfotab.firstName.fill("firstName")
