from behave import use_fixture

from fixtures import (
    playwright_browser,
    playwright_context,
    playwright_device,
    playwright_page,
)


def before_all(context):
    use_fixture(playwright_browser, context)
    use_fixture(playwright_device, context)
    use_fixture(playwright_context, context)


def before_scenario(context, scenario):
    use_fixture(playwright_page, context)
