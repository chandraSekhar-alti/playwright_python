from playwright.sync_api import Page, expect


class MyInfoPage:
    def __init__(self, page) -> None:
        self.page = page
        self.my_info_label = page.locator('//span[text()="My Info"]')
        self.profile_pic = page.locator('//img[@alt="profile picture"]/parent::div')
        self.tab_title = page.locator(
            '(//div[@class="orangehrm-edit-employee-content"]//child::h6)[1]'
        )
        self.first_name = page.locator('//input[@name="firstName"]')
        self.sibling_name = page.locator(
            "//label[text()='Nickname']/parent::div/following-sibling::div/input"
        )
        self.employee_id = page.locator(
            "//label[text()='Employee Id']/parent::div/following-sibling::div/input"
        )
        self.other_id = page.locator(
            "//label[text()='Other Id']/parent::div/following-sibling::div/input"
        )
        self.driver_license = page.locator(
            '//label[text()="Driver\'s License Number"]/parent::div/following-sibling::div/input'
        )
        self.licence_expire_date_calender = page.locator(
            '//label[text()="License Expiry Date"]/parent::div/following-sibling::div/descendant::input'
        )
        self.calender_year = page.locator(
            '//div[@class="oxd-calendar-selector-year-selected"]'
        )
        self.selected_year = page.locator("//li[text()='2002']")
        self.calender_month = page.locator('//li[@class="oxd-calendar-selector-month"]')
        self.selected_month = page.locator("//li[text()='July']")
        self.selected_day = page.locator(
            '//div[text()="6" and @class="oxd-calendar-date --selected"]'
        )
        self.ssn_number = page.locator(
            "//label[text()='SSN Number']/parent::div/following-sibling::div/input"
        )
        self.sin_number = page.locator(
            "//label[text()='SIN Number']/parent::div/following-sibling::div/input"
        )
        self.nationality_drop_down = page.locator(
            '//label[@class="oxd-label" and text()="Nationality"]/parent::div/following-sibling::div'
        )
        self.nationality_option = page.locator(
            '//div[@role="option"]/span[text()="Indian"]'
        )
        self.marital_status_text = page.locator(
            '//label[@class="oxd-label" and text()="Marital Status"]'
        )
        self.marital_status_drop_down = page.locator(
            '//label[text()="Marital Status"]/parent::div/following-sibling::div'
        )
        self.marital_status_drop_down_value = page.locator(
            '//div[@role="option"]/span[text()="Single"]'
        )
        self.military_services_text = page.locator(
            '//label[@class="oxd-label" and text()="Military Service"]'
        )
        self.military_services_input_field = page.locator(
            '//label[@class="oxd-label" and text()="Military Service"]/parent::div/following-sibling::div/input'
        )
        self.date_of_birth_text = page.locator(
            '//label[@class="oxd-label" and text()="Date of Birth"]'
        )
        self.date_of_birth_input_field = page.locator(
            '//label[@class="oxd-label" and text()="Date of Birth"]/parent::div/following-sibling::div/descendant::input'
        )
        self.gender_text = page.locator(
            '//label[@class="oxd-label" and text()="Gender"]'
        )
        self.gender_option = page.locator(
            '(//input[@type="radio"])[1]/following-sibling::span'
        )
        self.smoker_text = page.locator(
            '//label[@class="oxd-label" and text()="Smoker"]'
        )
        self.personal_details_save_button = page.locator(
            '(//button[@type="submit" and text()=" Save "])[1]'
        )
        self.success_message = page.get_by_text("Success", exact=True)
        self.success_message_text = page.get_by_text("Successfully Updated")
        self.custom_field_text = page.locator('//h6[text()="Custom Fields"]')
        self.blood_type_drop_down = page.locator(
            '(//div[@class="oxd-select-text-input"])[3]'
        )
        self.blood_type_value = page.locator('//div[@role="option"]/span[text()="B+"]')
        self.custom_field_save_button = page.locator('(//button[@type="submit"])[2]')
        self.attachment_text = page.locator('//h6[text()="Attachments"]')
        self.add_button = page.locator('//button[@type="button" and text()=" Add "]')
        self.comment_box = page.locator('//textarea[@placeholder="Type comment here"]')
        self.upload_file_save_button = page.locator('(//button[@type="submit"])[3]')
        self.record_section_text = page.locator("//span[text()='(1) Record Found']")
        self.record_table = page.locator('//div[@role="table"]')
        self.table_file_name_text = page.locator('(//div[@role="row"])[1]/descendant::div[text()="File Name"]')
        self.table_description_text = page.locator('(//div[@role="row"])[1]/descendant::div[text()="Description"]')
        self.table_size_text = page.locator('(//div[@role="row"])[1]/descendant::div[text()="Size"]')
        self.table_type_text = page.locator('(//div[@role="row"])[1]/descendant::div[text()="Type"]')
        self.table_added_date_text = page.locator('(//div[@role="row"])[1]/descendant::div[text()="Date Added"]')
        self.table_added_by_text = page.locator('(//div[@role="row"])[1]/descendant::div[text()="Added By"]')
        self.table_action_text =page.locator('(//div[@role="row"])[1]/descendant::div[text()="Actions"]')
        self.uploaded_file_name = lambda fileName : page.locator(f"(//div[text()='{fileName}'])[1]")
        self.copy_right_first_text = page.locator("//p[text()='OrangeHRM OS 5.5']")
        self.copy_right_second_text = page.locator("(//p[@class='oxd-text oxd-text--p orangehrm-copyright'])[2]")

