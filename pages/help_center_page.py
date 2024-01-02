from playwright.sync_api import Page

class HelpCenterPage:
    def __init__(self,page) -> None:
        self.page = page
        self.question_mark_symbol = page.locator('//button[@title="Help"]')
        self.admin_user_guide_button = page.locator('//span[@class="blocks-item-title" and text()="Admin User Guide"]')
        self.employee_user_guide_button = page.locator('//span[@class="blocks-item-title" and text()="Employee User Guide"]')
        self.FAQ_button = page.locator('//span[@class="blocks-item-title" and text()="FAQs"]')
        self.mobile_App_button = page.locator('//span[@class="blocks-item-title" and text()="Mobile App"]')
        self.orange_hrm_text_link = page.locator("//a[text()='OrangeHRM' and @href='/hc/en-us']/parent::li")
        self.search_bar = page.locator('//input[@placeholder="Search"]')
        self.orange_hrm_logo = page.locator('//img[@alt="OrangeHRM Help Center home page"]')
        self.next_button = page.locator('//a[@class="pagination-next-link"]')
        self.footer_hrm_text = page.locator('//div[@class="footer-inner"]')
        pass