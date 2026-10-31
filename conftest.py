import allure
import pytest
from playwright.sync_api import Page


@pytest.fixture(autouse=True)
def screenshot_on_failure(page: Page, request):
    yield

    if request.node.rep_call.failed:
        screenshot = page.screenshot(full_page=True)
        allure.attach(
            screenshot,
            name="Screenshot on failure",
            attachment_type=allure.attachment_type.PNG
        )
