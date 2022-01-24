from selenium.webdriver.support.ui import Select

from core.core_mt import BaseMt
from core.locators import PartnerLocators


class GoToPartnerPage(BaseMt, PartnerLocators):
    def partner_button(self):
        assert self.is_element_present(*PartnerLocators.partner_button), 'can\'t find button partner'
        self.find_el_click(*PartnerLocators.partner_button)

    def testmail_parnter(self):
        assert self.is_element_present(*PartnerLocators.test_partner), 'can\'t find test partner'
        self.find_el_click(*PartnerLocators.test_partner)

    def testmail_autorization(self):
        assert self.is_element_present(*PartnerLocators.test_authorization), 'can\'t find button autorization'
        self.find_el_click(*PartnerLocators.test_authorization)
        self.switch_to_new_win()


class PartnerNavBorder(BaseMt, PartnerLocators):
    def partner_settings(self):
        assert self.is_element_present(*PartnerLocators.partner_settings), 'can\'t find button settings'
        self.find_el_click(*PartnerLocators.partner_settings)

    def partner_stream(self):
        assert self.is_element_present(*PartnerLocators.partner_stream), 'can\'t find button stream'
        self.find_el_click(*PartnerLocators.partner_stream)

    # def partner_id(self):
    #     assert self.is_element_present(*PartnerLocators.partner_id), 'can\'t find id'
    #     id_number = self.browser.find_element(*PartnerLocators.partner_id).text
    #     return print(id_number)


class PartnerCreate(BaseMt, PartnerLocators):
    def partner_str_create(self):
        assert self.is_element_present(*PartnerLocators.create_stream), 'can\'t find button create stream'
        self.find_el_click(*PartnerLocators.create_stream)

    def type_stream(self):
        assert self.is_element_present(*PartnerLocators.type_stream_select), 'can\'t find field type'
        select = Select(self.browser.find_element(*PartnerLocators.type_stream_select))
        select.select_by_value("1")

    def stream_name(self):
        assert self.is_element_present(*PartnerLocators.stream_name), 'can\'t find field to name'
        self.find_el_write(*PartnerLocators.stream_name, 'autotest')

    def stream_url(self):
        assert self.is_element_present(*PartnerLocators.stream_url), 'can\'t find field to url'
        self.find_el_clear(*PartnerLocators.stream_url)
        self.find_el_write(*PartnerLocators.stream_url, 'http://google.com')

    def create_button(self):
        assert self.is_element_present(*PartnerLocators.create_stream_button), 'can\'t find button create'
        self.find_el_click(*PartnerLocators.create_stream_button)
