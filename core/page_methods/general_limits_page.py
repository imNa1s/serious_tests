from core.core_mt import BaseMt
from core.locators import AdmSideBarLocators


class AdmGeneralLimitPage(BaseMt):
    def general_limit_page_open(self):
        assert self.is_element_present(*AdmSideBarLocators.general_limits_menu), 'can\'t find button "general limit"'
        self.find_el_click(*AdmSideBarLocators.general_limits_menu)
