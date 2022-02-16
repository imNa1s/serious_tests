

from core.core_mt import BaseMt
from core.links import LinksReqTds
from core.locators import PartnerLocators, StreamLocators
from core.statistic.main_statistic_base import StatsMt


class GoToPartnerPage(BaseMt):
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


class PartnerNavBorder(BaseMt):
    def partner_settings(self):
        assert self.is_element_present(*PartnerLocators.partner_settings), 'can\'t find button settings'
        self.find_el_click(*PartnerLocators.partner_settings)

    def partner_source(self):
        assert self.is_element_present(*PartnerLocators.partner_source), 'can\'t find button source'
        self.find_el_click(*PartnerLocators.partner_source)

    def partner_stream(self):
        assert self.is_element_present(*StreamLocators.partner_stream), 'can\'t find button stream'
        self.find_el_click(*StreamLocators.partner_stream)

    def partner_tickets(self):
        assert self.is_element_present(*PartnerLocators.partner_tickets), 'can\'t find button tickets'
        self.find_el_click(*PartnerLocators.partner_tickets)


class PartnerHelpMt(StatsMt, PartnerLocators):
    def partner_id(self):
        assert self.is_element_present(*PartnerLocators.partner_id), 'can\'t find id'
        id_number = self.browser.find_element(*PartnerLocators.partner_id).text
        return print(id_number)
