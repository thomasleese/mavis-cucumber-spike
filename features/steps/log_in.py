import os

from behave import given

from mavis.testing.models import LogInPage, StartPage


@given("I am logged in as a {role}")
def step_impl(context, role=None):
    start_page = StartPage(context.playwright_page)
    start_page.start()

    username = os.environ[f"{role.upper()}_USERNAME"]
    password = os.environ[f"{role.upper()}_PASSWORD"]

    log_in_page = LogInPage(context.playwright_page)
    log_in_page.log_in(username, password)
    log_in_page.select_role("SAIS organisation")
