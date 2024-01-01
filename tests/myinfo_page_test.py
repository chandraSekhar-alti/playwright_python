from playwright.sync_api import expect
from dotenv import find_dotenv, load_dotenv
import os
from pages.myinfo_page import MyInfoTab

load_dotenv(find_dotenv())


def test_my_info_page_data_inserting(page):
    my_info_tab = MyInfoTab(page)
    expect(my_info_tab.my_info_label).to_be_visible()
    expect(my_info_tab.my_info_label).to_have_text("My Info")
    my_info_tab.my_info_label.click()
    page.wait_for_timeout(2000)

    # Validating the my info page URL
    assert page.url == os.getenv(
        "myInfoPage_URL"
    ), f"URL does not match the expected URL. Actual URL: {page.url}"

    expect(my_info_tab.profile_pic).to_be_visible()
    expect(my_info_tab.tab_title).to_be_visible()
    expect(my_info_tab.tab_title).to_have_text("Personal Details")

    # Filling some input fields
    my_info_tab.first_name.fill("firstName")
    my_info_tab.sibling_name.fill("this is sibling name")
    my_info_tab.employee_id.fill("FS1000")
    my_info_tab.other_id.fill("This is other ID field")
    my_info_tab.driver_license.fill("CRPSJVS5689VI")

    # Selecting the calendar date
    my_info_tab.licence_expire_date_calender.click()
    my_info_tab.licence_expire_date_calender.fill("2030-06-09")

    # Selecting the nationality drop-down
    my_info_tab.nationality_drop_down.click()
    my_info_tab.nationality_option.click()

    # Selecting the marital status drop-down
    expect(my_info_tab.marital_status_text).to_be_visible()
    my_info_tab.marital_status_drop_down.click()
    my_info_tab.marital_status_drop_down_value.click()

    expect(my_info_tab.military_services_text).to_be_visible()
    my_info_tab.military_services_input_field.fill("I don't have any experience")
    expect(my_info_tab.date_of_birth_text).to_be_visible()
    my_info_tab.date_of_birth_input_field.clear()
    my_info_tab.date_of_birth_input_field.type("2002-06-07")
    expect(my_info_tab.gender_text).to_be_visible()
    my_info_tab.gender_option.click()
    expect(my_info_tab.smoker_text).to_be_visible()

    # Click on the save button and validate the success message
    my_info_tab.personal_details_save_button.click()

    # Checking the visibility of custom field name and selecting the blood group
    expect(my_info_tab.custom_field_text).to_be_visible()
    my_info_tab.blood_type_drop_down.click()
    my_info_tab.blood_type_value.click()

    # Click on the save button and validate the success message
    my_info_tab.custom_field_save_button.click()

    expect(my_info_tab.attachment_text).to_be_visible()
    expect(my_info_tab.add_button).to_be_visible()
    my_info_tab.add_button.click()

    file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "refrenceNotes.txt")
    )

    # File upload with the input tag
    with page.expect_file_chooser() as fc_info:
        page.locator("//div[text()='Browse']").click()

    file_chooser = fc_info.value
    file_chooser.set_files(file_path)

    page.wait_for_timeout(2000)
    my_info_tab.comment_box.fill(
        "I have uploaded a reference document in this section for further reference to understand everything properly"
    )
    my_info_tab.upload_file_save_button.click()
