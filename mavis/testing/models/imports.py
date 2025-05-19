import re
import os.path


class ChooseImportPage:
    def __init__(self, page):
        self.page = page

        self.vaccination_records_radio = page.get_by_role(
            "radio", name="Vaccination records"
        )
        self.submit_button = page.get_by_role("button", name="Continue")

    def vaccination_records(self):
        self.vaccination_records_radio.click()
        self.submit_button.click()


class ImportPage:
    def __init__(self, page):
        self.page = page

        self.status_tag = page.get_by_text(
            re.compile("Processing|Invalid|Completed"), exact=True
        )


class ImportsPage:
    def __init__(self, page):
        self.page = page

        self.import_records_link = page.get_by_role("link", name="Import records")

    def import_records(self):
        self.import_records_link.click()


class UploadImportPage:
    def __init__(self, page):
        self.page = page

        self.upload_button = page.get_by_role("button", name="Upload file")
        self.submit_button = page.get_by_role("button", name="Continue")

    def upload(self, filename):
        self.upload_button.set_input_files(os.path.join("files", filename))
        self.submit_button.click()
