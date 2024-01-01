from playwright.sync_api import Page, expect

class HomePageSideBar:
    def __init__(self, page) -> None:
        self.page = page
        self.client_brand_banner = page.locator('//img[@alt="client brand banner"]')
        self.side_bar_menu_list = lambda generic_text: page.locator(
            f'//a[@class="oxd-main-menu-item"]/descendant::span[text()="{generic_text}"]'
        )
        # self.dashboard_item = page.locator('//a[@class="oxd-main-menu-item active"]/descendant::span[text()="Dashboard"]')
        self.maintenance_cancel_button = page.locator("//button[text()=' Cancel ']")
        pass

    def home_page_sidebar_validation(self, text, time):
        # checking the click functionality

        if text == "Maintenance":
            self.page.wait_for_timeout(time)
            self.side_bar_menu_list("Maintenance").hover()
            self.side_bar_menu_list("Maintenance").click()
            self.page.wait_for_timeout(time)
            self.maintenance_cancel_button.click()

        else:
            self.page.wait_for_timeout(time)
            self.side_bar_menu_list(text).hover()
            self.side_bar_menu_list(text).click()
