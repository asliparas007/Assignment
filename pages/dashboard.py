import time


class DashboardPage:
    def __init__(self, page):
        self.page = page

    def create_first_dashboard(self):
        self.page.locator(".css-1qm1lh").filter(has_text="Create your first dashboard").click()

    def add_visualization(self):
        self.page.locator(".css-1riaxdn").filter(has_text="Add visualization").click()

    def configure_new_data_source(self):
        with self.page.expect_popup() as newpageinfo:
            self.page.locator(".css-1riaxdn").filter(has_text="Configure a new data source").nth(1).click()
        return newpageinfo.value
