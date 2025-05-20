from functools import partial

from playwright.sync_api import expect
import pytest_bdd
from pytest_bdd import parsers, then, when

from mavis.testing.reporting import attach_screenshot


scenario = partial(pytest_bdd.scenario, "importing_vaccinations.feature")


@scenario("Whitespace is normalised")
def test_whitespace_is_normalised():
    pass


@when(parsers.parse("I import vaccinations from {filename}"))
def when_import_vaccinations(
    dashboard_page,
    imports_page,
    choose_import_type_page,
    import_vaccinations_page,
    filename,
    tmp_path,
):
    dashboard_page.import_records()
    imports_page.import_records()
    choose_import_type_page.vaccinations()
    import_vaccinations_page.upload(tmp_path / filename)


@then("I see the following vaccination details:")
def then_i_see_child_details(import_page, child_page, datatable):
    import_page.click_on("SELDON, Hari")

    summary_list = child_page.summary_list

    for row in datatable:
        key = row[0]

        needle = row[1]
        haystack = summary_list[key]

        if key == "NHS number":
            haystack = haystack.replace("\xa0\u200d", " ")

        assert needle in haystack
