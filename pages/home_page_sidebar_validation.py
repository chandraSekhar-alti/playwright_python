from playwright.sync_api import Page,expect

class HomePageSideBar:
    def __init__(self, page) -> None:
        self.page = page
        self.client_brand_banner = page.locator('//img[@alt="client brand banner"]')


        pass
    


