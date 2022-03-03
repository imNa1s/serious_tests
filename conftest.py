import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    chromeOptions = Options()
    # chromeOptions.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=chromeOptions)
    yield browser
    print("\nquit browser..")
    browser.quit()
