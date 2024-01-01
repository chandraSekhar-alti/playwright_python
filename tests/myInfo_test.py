from playwright.sync_api import expect
from dotenv import find_dotenv, load_dotenv
import os
from pages.my_info_tab import MyInfoTab

load_dotenv(find_dotenv())


def test_my_info_page_data_inserting(page):
    myInfotab = MyInfoTab(page)
    expect(myInfotab.myInfoLabel).to_be_visible()
    expect(myInfotab.myInfoLabel).to_have_text("My Info")
    myInfotab.myInfoLabel.click()
    page.wait_for_timeout(2000)

    # validating the my info page URL
    assert page.url == os.getenv(
        "myInfoPage_URL"
    ), f"URL does not match the expected URL. Actual URL: {page.url}"

    expect(myInfotab.profilePic).to_be_visible()
    expect(myInfotab.tabTitle).to_be_visible()
    expect(myInfotab.tabTitle).to_have_text("Personal Details")

    # expect(myInfotab.firstName)
    # filling some input fields
    myInfotab.firstName.fill("firstName")
    myInfotab.siblingName.fill("this is sibling name")
    myInfotab.employeId.fill("FS1000")
    myInfotab.otherId.fill("This is other ID field")
    myInfotab.driverLicence.fill("CRPSJVS5689VI")

    # selecting the calender date
    myInfotab.licenceExpireDataCalender.click()
    myInfotab.calenderYear.click()
    myInfotab.seletedYear.click()
    myInfotab.calenderMonth.click()
    myInfotab.seletedMonth.click()
    myInfotab.seletedDay.click()

    # selecting the nationality drop down
    myInfotab.nationalityDropDown.click()
    myInfotab.nationalityOption.click()

    # selecting the maritial status drop down
    expect(myInfotab.maritialStatusText).to_be_visible()
    myInfotab.maritialStatusDropDown.click()
    myInfotab.maritialStatusDropDownValue.click()

    expect(myInfotab.militaryServicesText).to_be_visible()
    myInfotab.militaryServicesInputField.fill("I don't have any expreience")
    expect(myInfotab.dateOfBirthText).to_be_visible()
    myInfotab.dateOfBirthInputField.clear()
    myInfotab.dateOfBirthInputField.type("2002-06-07")
    expect(myInfotab.genderText).to_be_visible()
    myInfotab.genderOption.click()
    expect(myInfotab.smokerText).to_be_visible()

    # click on the save button and validating the success message
    myInfotab.presonalDetailsSaveButton.click()

    # expect(myInfotab.successMessage).to_be_visible()
    # expect(myInfotab.successMessageText).to_be_visible()

    # checking the visibility of custom field name and selecting the blood group
    expect(myInfotab.customFieldText).to_be_visible()
    myInfotab.bloodTypeDropDown.click()
    myInfotab.bloodTypeValue.click()

    # click on the save button and validating the success message
    myInfotab.customFieldSaveButton.click()
    # expect(myInfotab.successMessage).to_be_visible()
    # expect(myInfotab.successMessageText).to_be_visible()

    expect(myInfotab.attachmentText).to_be_visible()
    expect(myInfotab.addButton).to_be_visible()
    myInfotab.addButton.click()
    # myInfotab.fileUploadButton.click()

    # file_path = os.path.abspath(
    #     os.path.join(os.path.dirname(__file__), "..", "refrenceNotes.txt")
    # )

    # file_path = "/path/to/your/file.txt"

    # myInfotab.file_upload(file_path)
    # myInfotab.file_input_selector.click()

    # page.wait_for_timeout(10000)
