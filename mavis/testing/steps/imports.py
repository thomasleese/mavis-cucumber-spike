from pytest_bdd import parsers, then, when

from playwright.sync_api import expect, Page

from ..models import (
    ChooseImportPage,
    DashboardPage,
    ImportPage,
    ImportsPage,
    UploadImportPage,
)
from ..reporting import attach_screenshot


@when(parsers.parse("I import vaccination records from {filename}"))
def when_i_import_vaccination_records(page: Page, filename: str):
    dashboard_page = DashboardPage(page)
    dashboard_page.import_records()

    imports_page = ImportsPage(page)
    imports_page.import_records()

    choose_import_page = ChooseImportPage(page)
    choose_import_page.vaccination_records()

    upload_import_page = UploadImportPage(page)
    upload_import_page.upload(filename)


@then("I see the imported vaccination records")
def then_i_see_the_imported_vaccination_records(page):
    import_page = ImportPage(page)

    attach_screenshot(page, "Import")

    expect(import_page.status_tag).to_be_visible()
    expect(import_page.status_tag).to_have_text("Completed")
