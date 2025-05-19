class DashboardPage:
    def __init__(self, page):
        self.page = page

        self.import_records_link = page.get_by_role("link", name="Import records")

    def import_records(self):
        self.import_records_link.click()
