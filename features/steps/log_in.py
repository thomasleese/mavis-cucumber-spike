import os

import allure
from behave import given


@given("I am logged in as a {role}")
def step_impl(context, role=None):
    page = context.playwright_page

    page.goto("/")

    allure.attach(
        page.screenshot(),
        name="Start page",
        attachment_type=allure.attachment_type.PNG,
    )

    page.get_by_role("link", name="Start now").click()

    username = os.environ[f"{role.upper()}_USERNAME"]
    password = os.environ[f"{role.upper()}_PASSWORD"]

    page.get_by_role("textbox", name="Email address").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("button", name="Log in").click()

    page.get_by_role("button", name="SAIS organisation").click()
