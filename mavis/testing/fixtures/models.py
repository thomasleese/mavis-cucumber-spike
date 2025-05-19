import pytest

from playwright.sync_api import Page

from ..models import (
    ChooseImportPage,
    DashboardPage,
    ImportPage,
    ImportsPage,
    LogInPage,
    StartPage,
    UploadImportPage,
)


@pytest.fixture
def choose_import_page(page: Page):
    return ChooseImportPage(page)


@pytest.fixture
def dashboard_page(page: Page):
    return DashboardPage(page)


@pytest.fixture
def import_page(page: Page):
    return ImportPage(page)


@pytest.fixture
def imports_page(page: Page):
    return ImportsPage(page)


@pytest.fixture
def log_in_page(page: Page):
    return LogInPage(page)


@pytest.fixture
def start_page(page: Page):
    return StartPage(page)


@pytest.fixture
def upload_import_page(page: Page):
    return UploadImportPage(page)
