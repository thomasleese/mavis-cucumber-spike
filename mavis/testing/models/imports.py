import re

from ..reporting import attach_screenshot

from playwright.sync_api import expect, Page


class ChooseImportTypePage:
    def __init__(self, page: Page):
        self.page = page

        self.cohort_radio = page.get_by_role("radio", name="Child records")
        self.class_list_radio = page.get_by_role("radio", name="Class list records")
        self.vaccinations_radio = page.get_by_role("radio", name="Vaccination records")
        self.continue_button = page.get_by_role("button", name="Continue")

    def _choose(self, radio):
        radio.click()
        attach_screenshot(self.page, "Choose type of import")
        self.continue_button.click()

    def cohort(self):
        self._choose(self.cohort_radio)

    def class_list(self):
        self._choose(self.class_list_radio)

    def vaccinations(self):
        self._choose(self.vaccinations_radio)


class ImportPage:
    def __init__(self, page: Page):
        self.page = page

        self.status_tag = page.get_by_text(
            re.compile("Processing|Invalid|Completed"), exact=True
        )

        self.table = page.get_by_role("table")
        self.rows = page.get_by_role("row")
        self.cells = page.get_by_role("cell")

    def click_on(self, text):
        cell = self.cells.filter(
            has=self.page.get_by_role("link", name=text, exact=True)
        )
        expect(cell).to_be_visible()
        cell.get_by_role("link").click()


class ImportClassListPage:
    def __init__(self, page: Page):
        self.page = page

        self.school_combobox = page.get_by_role("combobox")
        self.year_checkboxes = {
            year: page.get_by_role("checkbox", name=f"Year {year}")
            for year in range(1, 13)
        }
        self.upload_button = page.get_by_role("button", name="Upload file")
        self.continue_button = page.get_by_role("button", name="Continue")

    def select_school(self, text):
        self.school_combobox.fill(text)
        attach_screenshot(self.page, "Select school")
        self.page.get_by_role("option", name=text).click()
        self.continue_button.click()

    def check_years(self, *years):
        for year in years:
            self.year_checkboxes[year].check()
        attach_screenshot(self.page, "Check year groups")
        self.continue_button.click()

    def upload(self, path):
        self.upload_button.set_input_files(str(path))
        attach_screenshot(self.page, "Upload class list")
        self.continue_button.click()


class ImportCohortPage:
    def __init__(self, page: Page):
        self.page = page

        self.upload_button = page.get_by_role("button", name="Upload file")
        self.continue_button = page.get_by_role("button", name="Continue")

    def upload(self, path):
        self.upload_button.set_input_files(str(path))
        attach_screenshot(self.page, "Upload cohort")
        self.continue_button.click()


class ImportVaccinationsPage:
    def __init__(self, page: Page):
        self.page = page

        self.upload_button = page.get_by_role("button", name="Upload file")
        self.continue_button = page.get_by_role("button", name="Continue")

    def upload(self, path):
        self.upload_button.set_input_files(str(path))
        attach_screenshot(self.page, "Upload vaccinations")
        self.continue_button.click()


class ImportsPage:
    def __init__(self, page: Page):
        self.page = page

        self.import_records_link = page.get_by_role("link", name="Import records")

    def import_records(self):
        attach_screenshot(self.page, "Imports")
        self.import_records_link.click()
