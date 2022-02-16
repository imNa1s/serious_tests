from selenium.webdriver.support.ui import Select

from core.core_mt import BaseMt
from core.locators import PartnerLocators


class PartnerCreateSource(BaseMt):
    def partner_source_create(self):
        assert self.is_element_present(*PartnerLocators.create_source), 'can\'t find button create source'
        self.find_el_click(*PartnerLocators.create_source)

    def type_source(self):
        assert self.is_element_present(*PartnerLocators.type_source_select), 'can\'t find field type'
        select = Select(self.browser.find_element(*PartnerLocators.type_source_select))
        select.select_by_value("1")

    def source_name(self):
        assert self.is_element_present(*PartnerLocators.source_name), 'can\'t find field to name'
        self.find_el_write(*PartnerLocators.source_name, 'autotest')

    def source_url(self):
        assert self.is_element_present(*PartnerLocators.source_url), 'can\'t find field to url'
        self.find_el_clear(*PartnerLocators.source_url)
        self.find_el_write(*PartnerLocators.source_url, 'http://google.com')

    def create_source_button(self):
        assert self.is_element_present(*PartnerLocators.create_source_button), 'can\'t find button create'
        self.find_el_click(*PartnerLocators.create_source_button)