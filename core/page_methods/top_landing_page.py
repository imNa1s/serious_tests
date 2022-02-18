from core.core_mt import BaseMt
from core.locators import AdmSideBarLocators


class AdmTopLandingPage(BaseMt):
    def landing_top_open(self):
        assert self.is_element_present(*AdmSideBarLocators.landing_menu), 'can\'t find button "landing"'
        self.find_el_click(*AdmSideBarLocators.landing_menu)
        assert self.is_element_present(*AdmSideBarLocators.top_landing_menu), 'can\'t find button "top landing"'
        self.find_el_click(*AdmSideBarLocators.top_landing_menu)