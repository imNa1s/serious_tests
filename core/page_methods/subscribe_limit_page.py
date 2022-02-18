from core.core_mt import BaseMt
from core.locators import AdmSideBarLocators


class AdmSubLimitPage(BaseMt):
    def sub_limit_page_open(self):
        assert self.is_element_present(*AdmSideBarLocators.sub_limits_menu), 'can\'t find button "sub limit"'
        self.find_el_click(*AdmSideBarLocators.sub_limits_menu)
