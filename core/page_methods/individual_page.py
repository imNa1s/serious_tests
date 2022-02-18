from core.core_mt import BaseMt
from core.locators import AdmSideBarLocators


class AdmIndividualCommPage(BaseMt):
    def individual_comm_page_open(self):
        assert self.is_element_present(*AdmSideBarLocators.payments_menu), 'can\'t find button "payments"'
        self.find_el_click(*AdmSideBarLocators.payments_menu)
        assert self.is_element_present(*AdmSideBarLocators.individual_commissions_menu), 'can\'t find "individual"'
        self.find_el_click(*AdmSideBarLocators.individual_commissions_menu)
