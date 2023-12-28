import re
from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page) -> None:
        #HERE WE ARE DECLARING THE ALL LOCATORS
        self.page = page
        self.company_logo_image = page.locator('//img[@alt="company-branding"]')
        self.user_name_present_in_ui = page.locator('(//div[@class="orangehrm-login-error"]/descendant::p)[1]')
        self.user_password_present_in_ui = page.locator('(//div[@class="orangehrm-login-error"]/descendant::p)[2]')
        self.user_name_input_field = page.locator('//input[@name="username"]')
        self.user_password_input_field = page.locator('//input[@type="password"]')
        self.login_button = page.locator("//button[text()=' Login ']")
        self.orangeHRM_fruite_logo = page.locator('(//img[@alt="orangehrm-logo"])[2]')
        self.forgot_password_text = page.locator('//div[@class="orangehrm-login-forgot"]/p')

    def navigate_to_url(self, url):
        self.page.goto(url)
    
    def company_logo_image_visibility(self):
        # checks if the logo image is visible
        return self.company_logo_image.is_visible()

    def user_credentials_getting(self):
        userName = self.user_name_present_in_ui.inner_text()
        userPassword = self.user_password_present_in_ui.inner_text()
        print("userName is :- ", userName)
        print("userPassword is :- ", userPassword)

    def get_forgot_password_text(self):
        #retriving the forgot password text from the UI
        return self.forgot_password_text.text_content()

    def login(self, userName, userPassword):
        #validating the logo of the company should be visible
        assert self.company_logo_image_visibility(), "Company logo is not visible"

        #validating the visibility of the company's logo represented by the fruit symbol.
        assert self.orangeHRM_fruite_logo.is_visible(), "OrangeHRM fruite logo is not visible"

        # entering the user details in the login form
        self.user_name_input_field.click()
        self.user_name_input_field.fill(userName)
        self.user_password_input_field.fill(userPassword)

        #checking the visibility of the forgot password text should be visible
        assert self.forgot_password_text.is_visible(), "Forgot password text is not visible"

        #validating the forgot password text should be correct
        assert self.get_forgot_password_text() == "Forgot your password? ", "Forgot password text does not match expected value"

        #validating the login button should be visible
        assert self.login_button.is_visible(), "Login button is not visible"

        #click on the login button
        self.login_button.click()
       