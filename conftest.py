import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser_fixture():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        browser.close()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {

        "viewport": {
            "width": 1920,
            "height": 1080,
        },

        "storage_state": {
            "cookies": [
                {
                    "name": "stepik",
                    "value": "sd4fFfv!x_cfcstepik",
                    "url": "https://example.com"  # Замените на нужный URL
                },
            ]
        },
    }

import pytest

@pytest.mark.skip_browser("firefox")
def test_visit_example(page):
    page.goto("https://example.com")


@pytest.mark.only_browser("chromium")
def test_visit_example(page):
    page.goto("https://example.com")