from selenium.webdriver.support.ui import Select

from core.locators import TicketLocators, PartnerLocators
from core.statistic.main_statistic_base import StatsMt


class AdmTicketsPage(StatsMt):
    def adm_ticket_send_button(self):
        assert self.is_element_present(*PartnerLocators.test_settings), 'can\'t find button "settings"'
        self.find_el_click(*PartnerLocators.test_settings)
        assert self.is_element_present(*TicketLocators.adm_send_ticket_btn), 'can\'t find button "send ticket"'
        self.find_el_click(*TicketLocators.adm_send_ticket_btn)

    def adm_ticket_type_choice(self):
        assert self.is_element_present(*TicketLocators.adm_type_ticket), 'can\'t find type'
        select = Select(self.browser.find_element(*TicketLocators.adm_type_ticket))
        select.select_by_value('1')

    def adm_ticket_theme(self):
        assert self.is_element_present(*TicketLocators.adm_message_theme), 'can\'t find field theme'
        self.find_el_write(*TicketLocators.adm_message_theme, 'autotest')

    def adm_ticket_message(self):
        assert self.is_element_present(*TicketLocators.adm_message_ticket), 'can\'t find field message'
        self.find_el_write(*TicketLocators.adm_message_ticket, 'some text for test')

    def adm_ticket_send_message_button(self):
        assert self.is_element_present(*TicketLocators.adm_send_message), 'can\'t find button to send'
        self.find_el_click(*TicketLocators.adm_send_message)

    def see_partner_alert(self):
        assert self.is_element_present(*PartnerLocators.partner_alert), 'can\'t find field alert'
        how_much = self.browser.find_element(*PartnerLocators.partner_alert)
        return how_much.text

    def partner_alert_button(self):
        assert self.is_element_present(*PartnerLocators.partner_alert_button), 'can\'t find button partner alert'
        self.find_el_click(*PartnerLocators.partner_alert_button)

    def partner_alert_header_text(self):
        assert self.is_element_present(*TicketLocators.ticket_header), 'can\'t find field alert'
        header = self.browser.find_element(*TicketLocators.ticket_header)
        return header.text


class PartnerTicketsMt(StatsMt):
    def ticket_create(self):
        assert self.is_element_present(*TicketLocators.create_button_ticket), 'can\'t find button create ticket'
        self.find_el_click(*TicketLocators.create_button_ticket)

    def ticket_type(self):
        assert self.is_element_present(*TicketLocators.ticket_type_select), 'can\'t find field source'
        select = Select(self.browser.find_element(*TicketLocators.ticket_type_select))
        select.select_by_value('1')

    def ticket_type_message(self):
        assert self.is_element_present(*TicketLocators.ticket_message_type), 'can\'t find field massage type'
        self.find_el_write(*TicketLocators.ticket_message_type, 'autotest')

    def ticket_message(self):
        assert self.is_element_present(*TicketLocators.ticket_message), 'can\'t find field massage'
        self.find_el_write(*TicketLocators.ticket_message, 'autotest')

    def ticket_send_btn(self):
        assert self.is_element_present(*TicketLocators.btn_send_ticket), 'can\'t find button send ticket'
        self.find_el_click(*TicketLocators.btn_send_ticket)

    def see_adm_alert(self):
        assert self.is_element_present(*TicketLocators.alert_adm_ticket_icon), 'no field alerts'
        how_much = self.browser.find_element(*TicketLocators.alert_adm_ticket_icon)
        return how_much.text


