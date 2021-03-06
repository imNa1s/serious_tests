import requests
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException


class BaseMt:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def ref(self):
        self.browser.refresh()

    def switch_to_new_win(self):
        self.browser.switch_to.window(self.browser.window_handles[1])

    def switch_to_old_win(self):
        self.browser.switch_to.window(self.browser.window_handles[0])

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def find_el_click(self, how, what):
        A = self.browser.find_element(how, what)
        A.click()

    def find_el_write(self, how, what, write):
        A = self.browser.find_element(how, what)
        A.send_keys(write)

    def find_el_clear(self, how, what):
        A = self.browser.find_element(how, what)
        A.clear()

    def scroll_to(self, to):
        try:
            self.browser.execute_script("return arguments[0].scrollIntoView(true);", to)
        except AssertionError:
            return False
        return True

    def image_load(self, how, what):
        A = self.browser.find_element(how, what)
        A.send_keys("")

    def just_click(self):
        request = requests.get(self)
        assert request.status_code == requests.codes.ok, f'request status code = {request.status_code}'
        return request

    def save_stats(self):
        page_txt = self.browser.page_source
        soup = BeautifulSoup(page_txt, 'html.parser')
        return soup
