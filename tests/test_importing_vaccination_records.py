from functools import partial

from playwright.sync_api import expect
import pytest_bdd
from pytest_bdd import parsers, then, when

from mavis.testing.reporting import attach_screenshot


scenario = partial(pytest_bdd.scenario, "importing_vaccination_records.feature")


@scenario("Whitespace is normalised")
def test_whitespace_is_normalised():
    pass


@when(parsers.parse("I import vaccination records from {filename}"))
def when_i_import_vaccination_records(
    dashboard_page, imports_page, choose_import_page, upload_import_page, filename
):
    dashboard_page.import_records()
    imports_page.import_records()
    choose_import_page.vaccination_records()
    upload_import_page.upload(filename)


@then("I see the imported vaccination records")
def then_i_see_the_imported_vaccination_records(page, import_page):
    attach_screenshot(page, "Import")

    expect(import_page.status_tag).to_be_visible()
    expect(import_page.status_tag).to_have_text("Completed")
