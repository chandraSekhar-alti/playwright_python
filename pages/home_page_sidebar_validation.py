from playwright.sync_api import Page, expect


class HomePageSideBar:
    def __init__(self, page) -> None:
        self.page = page
        self.client_brand_banner = page.locator('//img[@alt="client brand banner"]')
        self.sideBarMenuList = lambda genericText: page.locator(
            f'//a[@class="oxd-main-menu-item"]/descendant::span[text()="{genericText}"]'
        )
        # self.dashBoardItem = page.locator('//a[@class="oxd-main-menu-item active"]/descendant::span[text()="Dashboard"]')
        self.MaintenanceCancleButton = page.locator("//button[text()=' Cancel ']")
        pass

    def homePagesideBarValidation(self, text,time):
        # checking the click functionality

        if text == "Maintenance":
            self.page.wait_for_timeout(time)
            self.sideBarMenuList("Maintenance").hover()
            self.sideBarMenuList("Maintenance").click()
            self.page.wait_for_timeout(time)
            self.MaintenanceCancleButton.click()


        else:
            self.page.wait_for_timeout(time)
            self.sideBarMenuList(text).hover()
            self.sideBarMenuList(text).click()
