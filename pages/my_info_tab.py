from playwright.sync_api import Page, expect

class MyInfoTab:
    def __init__(self,page) -> None:
        self.page = page
        self.myInfoLabel = page.locator('//span[text()="My Info"]')
        self.profilePic = page.locator('//img[@alt="profile picture"]/parent::div')
        self.tabTitle = page.locator('(//div[@class="orangehrm-edit-employee-content"]//child::h6)[1]')
        self.firstName = page.locator('//input[@name="firstName"]')
        pass