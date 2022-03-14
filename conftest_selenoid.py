import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    chromeOptions = Options()
    chromeOptions.add_argument()
    browser = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome',
                              'version': '99.0'},
        options=chromeOptions)

    browser.maximize_window()

    yield browser
    browser.quit()