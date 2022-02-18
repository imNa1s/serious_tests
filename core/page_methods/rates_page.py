from core.core_mt import BaseMt
from core.locators import AdmSideBarLocators


class AdmRatesPage(BaseMt):
    def rates_page_open(self):
        assert self.is_element_present(*AdmSideBarLocators.rates_menu), 'can\'t find button "rates"'
        self.find_el_click(*AdmSideBarLocators.rates_menu)
