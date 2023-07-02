import pytest
from selene import browser


@pytest.fixture(scope='function', autouse = True)
def brow_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1440
    browser.config.window_width = 2160

    yield

    browser.quit()