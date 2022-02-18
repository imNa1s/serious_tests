from core.core_mt import BaseMt
from core.locators import AdmSideBarLocators


class AdmRateServicesPage(BaseMt):
    def rate_services_page_open(self):
        assert self.is_element_present(*AdmSideBarLocators.rates_services_menu), 'can\'t find button "rates_services"'
        self.find_el_click(*AdmSideBarLocators.rates_services_menu)
