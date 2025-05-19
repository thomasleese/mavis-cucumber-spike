import allure
import os

from playwright.sync_api import BrowserType, Playwright
import pytest


@pytest.fixture(scope="session")
def base_url():
    return os.environ["BASE_URL"]


@pytest.fixture(scope="session")
def browser_type(playwright: Playwright, device: str) -> BrowserType:
    browser_name = playwright.devices[device]["default_browser_type"]
    return getattr(playwright, browser_name)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    if "BASIC_AUTH_USERNAME" in os.environ and "BASIC_AUTH_PASSWORD" in os.environ:
        http_credentials = {
            "username": os.environ["BASIC_AUTH_USERNAME"],
            "password": os.environ["BASIC_AUTH_PASSWORD"],
        }
    else:
        http_credentials = {}

    return {**browser_context_args, "http_credentials": http_credentials}


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    headless = "CI" in os.environ

    return {**browser_type_launch_args, "headless": headless}


@pytest.fixture(autouse=True)
def allure_device(device: str):
    # Allure doesn't support environments with spaces.
    device_name = device.lower().replace(" ", "_")

    yield

    allure.dynamic.label("device", device_name)
