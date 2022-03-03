import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    chromeOptions = Options()
    chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--window-size=1920,1080")
    browser = webdriver.Chrome(options=chromeOptions)
    yield browser
    print("\nquit browser..")
    browser.quit()
