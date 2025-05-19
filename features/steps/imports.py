import os.path

from behave import then, when
from playwright.sync_api import expect


@when("I import vaccination records from {filename}")
def step_impl(context, filename=None):
    page = context.playwright_page

    page.get_by_role("link", name="Import records").click()

    page.get_by_role("link", name="Import records").click()

    page.get_by_role("radio", name="Vaccination records").click()
    page.get_by_role("button", name="Continue").click()

    page.get_by_label("Upload file").set_input_files(os.path.join("files", filename))
    page.get_by_role("button", name="Continue").click()


@then("I see the imported vaccination records")
def step_impl(context):
    page = context.playwright_page

    expect(page.get_by_text("Completed")).to_be_visible()
