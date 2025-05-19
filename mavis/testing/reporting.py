import allure

from playwright.sync_api import Page


def attach_screenshot(page: Page, name: str):
    allure.attach(
        page.screenshot(),
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )
