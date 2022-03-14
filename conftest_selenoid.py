import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome',
                              'version': '99.0'},
        options=chrome_options)

    browser.maximize_window()

    yield browser
    browser.quit()