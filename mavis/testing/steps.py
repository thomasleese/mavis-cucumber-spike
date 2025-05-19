import os

from pytest_bdd import given, parsers

from .models import LogInPage, StartPage


@given(parsers.re("I am logged in as an? (?P<role>[a-z]+)"))
def given_logged_in(start_page: StartPage, log_in_page: LogInPage, role: str):
    start_page.goto()
    start_page.start()

    username = os.environ[f"{role.upper()}_USERNAME"]
    password = os.environ[f"{role.upper()}_PASSWORD"]

    log_in_page.log_in(username, password)
    log_in_page.select_role("SAIS organisation")
