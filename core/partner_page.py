import time

from selenium.webdriver.support.ui import Select

from core.core_mt import BaseMt
from core.links import LinksReqTds
from core.locators import PartnerLocators
from core.statistc_base import StatsMt


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

    def partner_source(self):
        assert self.is_element_present(*PartnerLocators.partner_source), 'can\'t find button source'
        self.find_el_click(*PartnerLocators.partner_source)

    def partner_stream(self):
        assert self.is_element_present(*PartnerLocators.partner_stream), 'can\'t find button stream'
        self.find_el_click(*PartnerLocators.partner_stream)


class PartnerCreateSource(BaseMt, PartnerLocators):
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


class PartnerCreateStream(BaseMt, PartnerLocators):
    def partner_stream_create(self):
        assert self.is_element_present(*PartnerLocators.create_stream), 'can\'t find button create stream'
        self.find_el_click(*PartnerLocators.create_stream)

    def partner_stream_name(self):
        assert self.is_element_present(*PartnerLocators.stream_name), 'can\'t find field to name'
        self.find_el_write(*PartnerLocators.stream_name, 'autotest')

    def stream_source(self):
        assert self.is_element_present(*PartnerLocators.stream_source), 'can\'t find field source'
        select = Select(self.browser.find_element(*PartnerLocators.stream_source))
        select.select_by_value('number:714')

    def stream_traffback_url(self):
        assert self.is_element_present(*PartnerLocators.traffback_url), 'can\'t find field traffback'
        self.find_el_clear(*PartnerLocators.traffback_url)
        self.find_el_write(*PartnerLocators.traffback_url, 'http://ya.ru')

    def stream_postback(self):
        assert self.is_element_present(*PartnerLocators.postback_url), 'can\'t find field postback'
        self.find_el_write(*PartnerLocators.postback_url, f'{LinksReqTds.postback}')

    def postback_actions_all(self):
        assert self.is_element_present(*PartnerLocators.postback_check_sub), 'can\'t find checkbox sub'
        self.find_el_click(*PartnerLocators.postback_check_sub)
        assert self.is_element_present(*PartnerLocators.postback_check_rebill), 'can\'t find checkbox rebill'
        self.find_el_click(*PartnerLocators.postback_check_rebill)
        assert self.is_element_present(*PartnerLocators.postback_check_unsub), 'can\'t find checkbox unsub'
        self.find_el_click(*PartnerLocators.postback_check_unsub)
        assert self.is_element_present(*PartnerLocators.postback_check_buyout), 'can\'t find checkbox buyout'
        self.find_el_click(*PartnerLocators.postback_check_buyout)

    def postback_actions_sub(self):
        assert self.is_element_present(*PartnerLocators.postback_check_sub), 'can\'t find checkbox sub'
        self.find_el_click(*PartnerLocators.postback_check_sub)

    def postback_actions_rebill(self):
        assert self.is_element_present(*PartnerLocators.postback_check_rebill), 'can\'t find checkbox rebill'
        self.find_el_click(*PartnerLocators.postback_check_rebill)

    def postback_actions_unsub(self):
        assert self.is_element_present(*PartnerLocators.postback_check_unsub), 'can\'t find checkbox unsub'
        self.find_el_click(*PartnerLocators.postback_check_unsub)

    def postback_actions_buyout(self):
        assert self.is_element_present(*PartnerLocators.postback_check_buyout), 'can\'t find checkbox buyout'
        self.find_el_click(*PartnerLocators.postback_check_buyout)

    def type_stream_redirect(self):
        assert self.is_element_present(*PartnerLocators.redirect_type_simple), 'can\'t find stream redirect settings'
        self.find_el_click(*PartnerLocators.redirect_type_simple)

    def payment_scheme(self):
        assert self.is_element_present(*PartnerLocators.auto_buyout), 'can\'t find checkbox auto buyout'
        self.find_el_click(*PartnerLocators.auto_buyout)

    def landing_page_display(self):
        assert self.is_element_present(*PartnerLocators.view_land_round), 'can\'t find landing display settings'
        self.find_el_click(*PartnerLocators.view_land_round)

    def ya_redirect_ban(self):
        assert self.is_element_present(*PartnerLocators.ban_ya_redirect), 'can\'t find yandex ban settings'
        self.find_el_click(*PartnerLocators.ban_ya_redirect)

    def landing_mts(self):
        assert self.is_element_present(*PartnerLocators.landing_mts), 'can\'t find MTS'
        self.find_el_click(*PartnerLocators.landing_mts)

    def choice_iplayer(self):
        assert self.is_element_present(*PartnerLocators.landing_iplayer), 'can\'t find iplayer'
        self.find_el_click(*PartnerLocators.landing_iplayer)

    def add_land_button(self):
        assert self.is_element_present(*PartnerLocators.add_lending_btn), 'can\'t find add landing button'
        self.find_el_click(*PartnerLocators.add_lending_btn)

    def stream_create_button(self):
        assert self.is_element_present(*PartnerLocators.create_stream_btn), 'can\'t find button create stream'
        self.find_el_click(*PartnerLocators.create_stream_btn)


class PartnerHelpMt(StatsMt, PartnerLocators):
    def partner_id(self):
        assert self.is_element_present(*PartnerLocators.partner_id), 'can\'t find id'
        id_number = self.browser.find_element(*PartnerLocators.partner_id).text
        return print(id_number)
