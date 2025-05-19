from ..reporting import attach_screenshot


class StartPage:
    def __init__(self, page):
        self.page = page

        self.start_link = page.get_by_role("link", name="Start now")

    def start(self):
        attach_screenshot(self.page, "Start")
        self.start_link.click()
