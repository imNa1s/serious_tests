from core.core_mt import BaseMt
from core.locators import AdmSideBarLocators


class AdmPercentBuyoutPage(BaseMt):
    def percent_buyout_page_open(self):
        assert self.is_element_present(*AdmSideBarLocators.percent_buyout_menu), 'can\'t find button "percent buyout"'
        self.find_el_click(*AdmSideBarLocators.percent_buyout_menu)
