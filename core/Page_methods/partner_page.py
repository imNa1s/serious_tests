from selenium.webdriver.support.ui import Select

from core.core_mt import BaseMt
from core.links import LinksReqTds
from core.locators import PartnerLocators, StreamLocators, TicketLocators
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


class PartnerCreateStream(BaseMt):
    def partner_stream_create(self):
        assert self.is_element_present(*StreamLocators.create_stream), 'can\'t find button create stream'
        self.find_el_click(*StreamLocators.create_stream)

    def partner_stream_name(self):
        assert self.is_element_present(*StreamLocators.stream_name), 'can\'t find field to name'
        self.find_el_write(*StreamLocators.stream_name, 'autotest')

    def stream_source(self):
        assert self.is_element_present(*StreamLocators.stream_source), 'can\'t find field source'
        select = Select(self.browser.find_element(*StreamLocators.stream_source))
        select.select_by_value('number:714')

    def stream_traffback_url(self):
        assert self.is_element_present(*StreamLocators.traffback_url), 'can\'t find field traffback'
        self.find_el_clear(*StreamLocators.traffback_url)
        self.find_el_write(*StreamLocators.traffback_url, 'http://ya.ru')

    def stream_postback(self):
        assert self.is_element_present(*StreamLocators.postback_url), 'can\'t find field postback'
        self.find_el_write(*StreamLocators.postback_url, f'{LinksReqTds.postback}')

    def postback_actions_all(self):
        assert self.is_element_present(*StreamLocators.postback_check_sub), 'can\'t find checkbox sub'
        self.find_el_click(*StreamLocators.postback_check_sub)
        assert self.is_element_present(*StreamLocators.postback_check_rebill), 'can\'t find checkbox rebill'
        self.find_el_click(*StreamLocators.postback_check_rebill)
        assert self.is_element_present(*StreamLocators.postback_check_unsub), 'can\'t find checkbox unsub'
        self.find_el_click(*StreamLocators.postback_check_unsub)
        assert self.is_element_present(*StreamLocators.postback_check_buyout), 'can\'t find checkbox buyout'
        self.find_el_click(*StreamLocators.postback_check_buyout)

    def postback_actions_sub(self):
        assert self.is_element_present(*StreamLocators.postback_check_sub), 'can\'t find checkbox sub'
        self.find_el_click(*StreamLocators.postback_check_sub)

    def postback_actions_rebill(self):
        assert self.is_element_present(*StreamLocators.postback_check_rebill), 'can\'t find checkbox rebill'
        self.find_el_click(*StreamLocators.postback_check_rebill)

    def postback_actions_unsub(self):
        assert self.is_element_present(*StreamLocators.postback_check_unsub), 'can\'t find checkbox unsub'
        self.find_el_click(*StreamLocators.postback_check_unsub)

    def postback_actions_buyout(self):
        assert self.is_element_present(*StreamLocators.postback_check_buyout), 'can\'t find checkbox buyout'
        self.find_el_click(*StreamLocators.postback_check_buyout)

    def type_stream_redirect(self):
        assert self.is_element_present(*StreamLocators.redirect_type_simple), 'can\'t find stream redirect settings'
        self.find_el_click(*StreamLocators.redirect_type_simple)

    def payment_scheme(self):
        assert self.is_element_present(*StreamLocators.auto_buyout), 'can\'t find checkbox auto buyout'
        self.find_el_click(*StreamLocators.auto_buyout)

    def landing_page_display(self):
        assert self.is_element_present(*StreamLocators.view_land_round), 'can\'t find landing display settings'
        self.find_el_click(*StreamLocators.view_land_round)

    def ya_redirect_ban(self):
        assert self.is_element_present(*StreamLocators.ban_ya_redirect), 'can\'t find yandex ban settings'
        self.find_el_click(*StreamLocators.ban_ya_redirect)

    def landing_mts(self):
        assert self.is_element_present(*StreamLocators.landing_mts), 'can\'t find MTS'
        self.find_el_click(*StreamLocators.landing_mts)

    def choice_iplayer(self):
        assert self.is_element_present(*StreamLocators.landing_iplayer), 'can\'t find iplayer'
        self.find_el_click(*StreamLocators.landing_iplayer)

    def add_land_button(self):
        assert self.is_element_present(*StreamLocators.add_lending_btn), 'can\'t find add landing button'
        self.find_el_click(*StreamLocators.add_lending_btn)

    def stream_create_button(self):
        assert self.is_element_present(*StreamLocators.create_stream_btn), 'can\'t find button create stream'
        self.find_el_click(*StreamLocators.create_stream_btn)


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


class PartnerHelpMt(StatsMt, PartnerLocators):
    def partner_id(self):
        assert self.is_element_present(*PartnerLocators.partner_id), 'can\'t find id'
        id_number = self.browser.find_element(*PartnerLocators.partner_id).text
        return print(id_number)