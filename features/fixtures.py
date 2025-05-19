import os

from behave import fixture
from playwright.sync_api import sync_playwright


playwright = sync_playwright().start()


@fixture
def playwright_device(context):
    device_name = context.config.userdata["device"]
    context.playwright_device = playwright.devices[device_name]


@fixture
def playwright_browser(context):
    device = context.playwright_device

    browser_type = getattr(playwright, device["default_browser_type"])
    browser = browser_type.launch(headless=False)

    context.playwright_browser = browser
    yield browser

    browser.close()


@fixture
def playwright_context(context):
    device = context.playwright_device

    if "BASIC_AUTH_USERNAME" in os.environ and "BASIC_AUTH_PASSWORD" in os.environ:
        http_credentials = {
            "username": os.environ["BASIC_AUTH_USERNAME"],
            "password": os.environ["BASIC_AUTH_PASSWORD"],
        }
    else:
        http_credentials = {}

    playwright_context = context.playwright_browser.new_context(
        base_url=os.environ["BASE_URL"],
        http_credentials=http_credentials,
        **device,
    )

    context.playwright_context = playwright_context


@fixture
def playwright_page(context):
    context.playwright_page = context.playwright_context.new_page()
    context.playwright_page.goto("/")
