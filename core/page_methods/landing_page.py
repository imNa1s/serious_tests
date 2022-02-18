from core.core_mt import BaseMt
from core.locators import AdmSideBarLocators


class AdmLandingPage(BaseMt):
    def lp_page_open(self):
        assert self.is_element_present(*AdmSideBarLocators.landing_menu), 'can\'t find button "landing"'
        self.find_el_click(*AdmSideBarLocators.landing_menu)
        assert self.is_element_present(*AdmSideBarLocators.lp_menu), 'can\'t find button "lp"'
        self.find_el_click(*AdmSideBarLocators.lp_menu)
