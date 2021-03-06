from selenium.webdriver.support.ui import Select

from core.core_mt import BaseMt
from core.links import LinksReqTds
from core.locators import StreamLocators, AdmSideBarLocators


class AdmStreamPage(BaseMt):
    def stream_page_open(self):
        assert self.is_element_present(*AdmSideBarLocators.streams_menu), 'can\'t find button streams'
        self.find_el_click(*AdmSideBarLocators.streams_menu)


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
