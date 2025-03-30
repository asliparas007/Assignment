import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def initialize_browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:3000/login")
    yield page
    page.close()
    browser.close()
