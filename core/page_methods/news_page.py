from core.core_mt import BaseMt
from core.locators import AdmSideBarLocators


class AdmNewsPage(BaseMt):
    def news_page_open(self):
        assert self.is_element_present(*AdmSideBarLocators.news_menu), 'can\'t find button "news"'
        self.find_el_click(*AdmSideBarLocators.news_menu)
