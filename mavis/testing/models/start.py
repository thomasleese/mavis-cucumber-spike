class StartPage:
    def __init__(self, page):
        self.page = page

        self.start_link = page.get_by_role("link", name="Start now")

    def start(self):
        self.start_link.click()
