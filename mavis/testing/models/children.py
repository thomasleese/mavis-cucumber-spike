from playwright.sync_api import Page

from ..reporting import attach_screenshot


class ChildPage:
    def __init__(self, page: Page):
        self.page = page

        self.terms = page.get_by_role("term")
        self.definitions = page.get_by_role("definition")

    @property
    def summary_list(self):
        attach_screenshot(self.page, "Child details")

        terms = [term.text_content() for term in self.terms.all()]
        definitions = [
            definition.text_content() for definition in self.definitions.all()
        ]
        return dict(zip(terms, definitions))
