from behave import then, when
from playwright.sync_api import expect

from mavis.testing.models import (
    ChooseImportPage,
    DashboardPage,
    ImportPage,
    ImportsPage,
    UploadImportPage,
)
from mavis.testing.reporting import attach_screenshot


@when("I import vaccination records from {filename}")
def step_impl(context, filename=None):
    dashboard_page = DashboardPage(context.playwright_page)
    dashboard_page.import_records()

    imports_page = ImportsPage(context.playwright_page)
    imports_page.import_records()

    choose_import_page = ChooseImportPage(context.playwright_page)
    choose_import_page.vaccination_records()

    upload_import_page = UploadImportPage(context.playwright_page)
    upload_import_page.upload(filename)


@then("I see the imported vaccination records")
def step_impl(context):
    import_page = ImportPage(context.playwright_page)

    attach_screenshot(context.playwright_page, "Import")

    expect(import_page.status_tag).to_be_visible()
    expect(import_page.status_tag).to_have_text("Completed")
