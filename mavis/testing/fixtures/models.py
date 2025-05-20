import pytest

from playwright.sync_api import Page

from ..models import (
    ChildPage,
    ChooseImportTypePage,
    DashboardPage,
    ImportClassListPage,
    ImportCohortPage,
    ImportVaccinationsPage,
    ImportPage,
    ImportsPage,
    LogInPage,
    StartPage,
    VaccinationPage,
)


@pytest.fixture
def child_page(page: Page) -> ChildPage:
    return ChildPage(page)


@pytest.fixture
def choose_import_type_page(page: Page) -> ChooseImportTypePage:
    return ChooseImportTypePage(page)


@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    return DashboardPage(page)


@pytest.fixture
def import_class_list_page(page: Page) -> ImportClassListPage:
    return ImportClassListPage(page)


@pytest.fixture
def import_cohort_page(page: Page) -> ImportCohortPage:
    return ImportCohortPage(page)


@pytest.fixture
def import_vaccinations_page(page: Page) -> ImportVaccinationsPage:
    return ImportVaccinationsPage(page)


@pytest.fixture
def import_page(page: Page) -> ImportPage:
    return ImportPage(page)


@pytest.fixture
def imports_page(page: Page) -> ImportsPage:
    return ImportsPage(page)


@pytest.fixture
def log_in_page(page: Page) -> LogInPage:
    return LogInPage(page)


@pytest.fixture
def start_page(page: Page) -> StartPage:
    return StartPage(page)


@pytest.fixture
def vaccination_page(page: Page) -> VaccinationPage:
    return VaccinationPage(page)
