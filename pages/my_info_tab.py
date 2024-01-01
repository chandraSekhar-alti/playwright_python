from playwright.sync_api import Page, expect


class MyInfoTab:
    def __init__(self, page) -> None:
        self.page = page
        self.myInfoLabel = page.locator('//span[text()="My Info"]')
        self.profilePic = page.locator('//img[@alt="profile picture"]/parent::div')
        self.tabTitle = page.locator(
            '(//div[@class="orangehrm-edit-employee-content"]//child::h6)[1]'
        )
        self.firstName = page.locator('//input[@name="firstName"]')
        self.siblingName = page.locator(
            "//label[text()='Nickname']/parent::div/following-sibling::div/input"
        )
        self.employeId = page.locator(
            "//label[text()='Employee Id']/parent::div/following-sibling::div/input"
        )
        self.otherId = page.locator(
            "//label[text()='Other Id']/parent::div/following-sibling::div/input"
        )
        self.driverLicence = page.locator(
            '//label[text()="Driver\'s License Number"]/parent::div/following-sibling::div/input'
        )
        self.licenceExpireDataCalender = page.locator(
            '(//i[@class="oxd-icon bi-calendar oxd-date-input-icon"])[1]'
        )
        self.calenderYear = page.locator(
            '//div[@class="oxd-calendar-selector-year-selected"]'
        )
        self.seletedYear = page.locator("//li[text()='2002']")
        self.calenderMonth = page.locator('//li[@class="oxd-calendar-selector-month"]')
        self.seletedMonth = page.locator("//li[text()='July']")
        self.seletedDay = page.locator(
            "//div[@class='oxd-calendar-date' and text()='6']"
        )
        self.SSN_number = page.locator(
            "//label[text()='SSN Number']/parent::div/following-sibling::div/input"
        )
        self.SIN_number = page.locator(
            "//label[text()='SIN Number']/parent::div/following-sibling::div/input"
        )
        self.nationalityDropDown = page.locator(
            '//label[@class="oxd-label" and text()="Nationality"]/parent::div/following-sibling::div'
        )
        self.nationalityOption = page.locator(
            '//div[@class="oxd-select-option"]/span[text()="Indian"]'
        )
        self.maritialStatusText = page.locator(
            '//label[@class="oxd-label" and text()="Marital Status"]'
        )
        self.maritialStatusDropDown = page.locator(
            '//label[@class="oxd-label" and text()="Marital Status"]/parent::div/following-sibling::div'
        )
        self.maritialStatusDropDownValue = page.locator(
            "//span[text()='Single']/parent::div[@class='oxd-select-option']"
        )
        self.militaryServicesText = page.locator(
            '//label[@class="oxd-label" and text()="Military Service"]'
        )
        self.militaryServicesInputField = page.locator(
            '//label[@class="oxd-label" and text()="Military Service"]/parent::div/following-sibling::div/input'
        )
        self.dateOfBirthText = page.locator(
            '//label[@class="oxd-label" and text()="Date of Birth"]'
        )
        self.dateOfBirthInputField = page.locator(
            '//label[@class="oxd-label" and text()="Date of Birth"]/parent::div/following-sibling::div/descendant::input'
        )
        self.genderText = page.locator(
            '//label[@class="oxd-label" and text()="Gender"]'
        )
        self.genderOption = page.locator(
            '(//input[@type="radio"])[1]/following-sibling::span'
        )
        self.smokerText = page.locator(
            '//label[@class="oxd-label" and text()="Smoker"]'
        )
        self.presonalDetailsSaveButton = page.locator(
            '(//button[@type="submit" and text()=" Save "])[1]'
        )
        self.successMessage = page.get_by_text("Success", exact=True)
        self.successMessageText = page.get_by_text("Successfully Updated")
        self.customFieldText = page.locator('//h6[text()="Custom Fields"]')
        self.bloodTypeDropDown = page.locator(
            '(//div[@class="oxd-select-text-input"])[3]'
        )
        self.bloodTypeValue = page.locator('//div[@role="option"]/span[text()="B+"]')
        self.customFieldSaveButton = page.locator('(//button[@type="submit"])[2]')
        self.attachmentText = page.locator('//h6[text()="Attachments"]')
        self.addButton = page.locator('//button[@type="button" and text()=" Add "]')
        self.file_input_selector = page.locator('//input[@type="file"]/parent::div')
        self.file_input_selector2 = page.locator('//input[@type="file"]/parent::div')


        pass

    async def file_upload(self, file_path):
        input_element = await self.file_input_selector2()
        await input_element.set_input_files(file_path)
        await self.page.wait_for_timeout(2000)


    
