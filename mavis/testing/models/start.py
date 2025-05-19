from ..reporting import attach_screenshot

from playwright.sync_api import Page


class StartPage:
    def __init__(self, page: Page):
        self.page = page

        self.start_link = page.get_by_role("link", name="Start now")

    def goto(self):
        self.page.goto("/")

    def start(self):
        attach_screenshot(self.page, "Start")
        self.start_link.click()
