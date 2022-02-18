from core.core_mt import BaseMt
from core.locators import AdmSideBarLocators


class AdmBalanceHistoryPage(BaseMt):
    def balance_history_page_open(self):
        assert self.is_element_present(*AdmSideBarLocators.payments_menu), 'can\'t find button "payments"'
        self.find_el_click(*AdmSideBarLocators.payments_menu)
        assert self.is_element_present(*AdmSideBarLocators.balance_history_menu), 'can\'t find button "balance history"'
        self.find_el_click(*AdmSideBarLocators.balance_history_menu)
