from behave import fixture
from playwright.sync_api import sync_playwright


playwright = sync_playwright().start()


@fixture
def playwright_browser(context):
    browser_name = context.config.userdata["browser"]
    browser_type = getattr(playwright, browser_name)
    browser = browser_type.launch(headless=False)

    context.playwright_browser = browser
    yield browser

    browser.close()


@fixture
def playwright_device(context):
    if device_name := context.config.userdata.get("device"):
        context.playwright_device = playwright.devices[device_name]
    else:
        context.playwright_device = {}


@fixture
def playwright_context(context):
    userdata = context.config.userdata

    if "basic_auth_username" in userdata and "basic_auth_password" in userdata:
        http_credentials = {
            "username": userdata["basic_auth_username"],
            "password": userdata["basic_auth_password"],
        }
    else:
        http_credentials = {}

    playwright_context = context.playwright_browser.new_context(
        base_url=userdata["base_url"],
        http_credentials=http_credentials,
        **context.playwright_device,
    )

    context.playwright_context = playwright_context


@fixture
def playwright_page(context):
    context.playwright_page = context.playwright_context.new_page()
