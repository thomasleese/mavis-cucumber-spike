from ..reporting import attach_screenshot

from playwright.sync_api import Page


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

        self.import_records_link = page.get_by_role("link", name="Import records")
        self.links = (
            page.get_by_role("main").get_by_role("listitem").get_by_role("link")
        )
        self.log_out_button = page.get_by_role("button", name="Log out")

    def log_out(self):
        self.log_out_button.click()

    def import_records(self):
        attach_screenshot(self.page, "Dashboard")

        self.import_records_link.click()
