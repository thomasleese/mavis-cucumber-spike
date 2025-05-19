from functools import partial

from playwright.sync_api import expect
import pytest_bdd
from pytest_bdd import given, parsers, then, when

from mavis.testing.reporting import attach_screenshot


scenario = partial(pytest_bdd.scenario, "authentication.feature")


@scenario("Logging in and out (<role>)")
def test_logging_in_and_out():
    pass


@then(parsers.parse("I see the following dashboard links:"))
def then_i_see_the_message(page, dashboard_page, datatable):
    attach_screenshot(page, "After log in")
    expected_links = [row[0] for row in datatable]
    expect(dashboard_page.links).to_have_text(expected_links)


@when("I log out")
def when_log_out(dashboard_page):
    dashboard_page.log_out()


@then("I see the start page")
def then_start_page(page, start_page):
    attach_screenshot(page, "After log out")
    expect(start_page.start_link).to_be_visible()


@scenario("Invalid username or password ('<username>' and '<password>')")
def test_invalid_username_or_password():
    pass


@given("I am on the log in page")
def given_i_am_on_log_in_page(log_in_page):
    log_in_page.goto()


@when(
    parsers.re("I try to log in with '(?P<username>[a-z]*)' and '(?P<password>[a-z]*)'")
)
def when_i_try_to_log_in(log_in_page, username, password):
    log_in_page.log_in(username, password)


@then(parsers.parse("I see the message '{message}'"))
def then_i_see_the_message(log_in_page, message):
    pass
