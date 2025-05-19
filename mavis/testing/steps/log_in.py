import os

from playwright.sync_api import Page
from pytest_bdd import given, parsers

from ..models import LogInPage, StartPage


@given(parsers.parse("I am logged in as a {role}"))
def given_logged_in(page: Page, role: str):
    page.goto("/")

    start_page = StartPage(page)
    start_page.start()

    username = os.environ[f"{role.upper()}_USERNAME"]
    password = os.environ[f"{role.upper()}_PASSWORD"]

    log_in_page = LogInPage(page)
    log_in_page.log_in(username, password)
    log_in_page.select_role("SAIS organisation")
