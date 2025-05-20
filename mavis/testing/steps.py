import os

import allure
from pytest_bdd import given, parsers, then
from playwright.sync_api import expect, Page

from .generators import ClassListGenerator, CohortGenerator, VaccinationsGenerator
from .models import ImportPage, LogInPage, StartPage
from .reporting import attach_screenshot


@given(parsers.re("I am logged in as an? (?P<role>[a-z]+)"))
def given_logged_in(role: str, start_page: StartPage, log_in_page: LogInPage):
    start_page.goto()
    start_page.start()

    username = os.environ[f"{role.upper()}_USERNAME"]
    password = os.environ[f"{role.upper()}_PASSWORD"]

    log_in_page.log_in(username, password)
    log_in_page.select_role("SAIS organisation")


@given(parsers.parse("a class list file named {filename} exists with:"))
def given_class_list_file(filename: str, datatable: [[str]], faker, tmp_path):
    path = tmp_path / filename
    ClassListGenerator(datatable, faker).save(path)
    allure.attach(
        path.read_bytes(),
        name=filename,
        attachment_type=allure.attachment_type.CSV,
    )


@given(parsers.parse("a cohort file named {filename} exists with:"))
def given_cohort_file(filename: str, datatable: [[str]], faker, tmp_path):
    path = tmp_path / filename
    CohortGenerator(datatable, faker).save(tmp_path / filename)
    allure.attach(
        path.read_bytes(),
        name=filename,
        attachment_type=allure.attachment_type.CSV,
    )


@given(parsers.parse("a {kind} vaccinations file named {filename} exists with:"))
def given_vaccinations(kind: str, filename: str, datatable: [[str]], faker, tmp_path):
    path = tmp_path / filename
    VaccinationsGenerator(kind, datatable, faker).save(tmp_path / filename)
    allure.attach(
        path.read_bytes(),
        name=filename,
        attachment_type=allure.attachment_type.CSV,
    )


@then(parsers.parse("I see a {status} import"))
def then_successful_import(status: str, page: Page, import_page: ImportPage):
    attach_screenshot(page, "Import details")
    expect(import_page.status_tag).to_have_text(status.capitalize())
