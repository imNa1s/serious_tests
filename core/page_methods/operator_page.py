from selenium.webdriver.support.ui import Select

from core.core_mt import BaseMt
from core.locators import OperatorLocators


class OperatorMT(BaseMt):
    def operator_page_open(self):
        assert self.is_element_present(*OperatorLocators.landing_menu), 'can\'t find landing'
        self.find_el_click(*OperatorLocators.landing_menu)
        assert self.is_element_present(*OperatorLocators.operator), 'can\'t find button operators'
        self.find_el_click(*OperatorLocators.operator)

    def operator_create_button(self):
        assert self.is_element_present(*OperatorLocators.operator_create), 'can\'t find button create operator'
        self.find_el_click(*OperatorLocators.operator_create)

    def operator_give_name(self):
        assert self.is_element_present(*OperatorLocators.operator_name), 'can\'t find field to name operator'
        self.find_el_write(*OperatorLocators.operator_name, 'autotest')

    def operator_subnet(self):
        assert self.is_element_present(*OperatorLocators.operator_subnet), 'can\'t find field to write subnet'
        self.find_el_write(*OperatorLocators.operator_subnet, '94.41.230.0/22')

    def operator_denied_devices(self):
        assert self.is_element_present(*OperatorLocators.opeartor_denied_devices), 'can\'t find field denied devices'
        self.find_el_write(*OperatorLocators.opeartor_denied_devices, '{"desktop":true}')

    def operator_country(self):
        assert self.is_element_present(*OperatorLocators.operator_country), 'can\'t find country selector'
        select = Select(self.browser.find_element(*OperatorLocators.operator_country))
        select.select_by_value('1')

    def operator_status(self):
        assert self.is_element_present(*OperatorLocators.operator_on), 'can\'t find status checkbox'
        self.find_el_click(*OperatorLocators.operator_on)

    def operator_web(self):
        assert self.is_element_present(*OperatorLocators.operator_web), 'can\'t find status checkbox'
        self.find_el_click(*OperatorLocators.operator_web)

    def operator_create_end_button(self):
        assert self.is_element_present(*OperatorLocators.operator_create_button), 'can\'t find button create'
        self.find_el_click(*OperatorLocators.operator_create_button)
