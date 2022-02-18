from core.core_mt import BaseMt
from core.locators import AdmSideBarLocators


class AdmLandingPage(BaseMt):
    def orders_page_open(self):
        assert self.is_element_present(*AdmSideBarLocators.payments_menu), 'can\'t find button "payments"'
        self.find_el_click(*AdmSideBarLocators.payments_menu)
        assert self.is_element_present(*AdmSideBarLocators.orders_menu), 'can\'t find button "orders"'
        self.find_el_click(*AdmSideBarLocators.orders_menu)
