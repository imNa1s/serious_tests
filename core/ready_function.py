import time

import requests

from core.core_mt import BaseMt
from core.links import SiteLinks
from core.login_page import LoginPage
from core.request_stf import Request_stuff, Request_urls
from core.partner_page import GoToPartnerPage, PartnerNavBorder, PartnerCreateSource, PartnerCreateStream


class BrowserMt:
    def login_pass(self, link):
        link_check = SiteLinks.login_link_test1
        Page = LoginPage(self, link)
        Page.open()
        Page.write_email_admin()
        Page.write_password_admin()
        Page.login_button()
        time.sleep(2)
        to_check = self.current_url
        assert link_check != to_check, "you didn't login"

    def partner_redirect(self, link):
        Page = GoToPartnerPage(self, link)
        Page.partner_button()
        Page.testmail_parnter()
        Page.testmail_autorization()

    def create_source(self, link):
        Page = PartnerNavBorder(self, link)
        Page.partner_source()
        Page = PartnerCreateSource(self, link)
        Page.partner_source_create()
        Page.type_source()
        Page.source_name()
        Page.source_url()
        Page.create_source_button()

    def create_stream(self, link):
        Page = PartnerNavBorder(self, link)
        Page.partner_stream()
        Page = PartnerCreateStream(self, link)
        Page.partner_stream_create()
        Page.partner_stream_name()
        Page.stream_source()
        Page.stream_traffback_url()
        Page.stream_postback()
        Page.postback_actions_all()
        Page.type_stream_redirect()
        Page.landing_page_display()
        Page.ya_redirect_ban()
        Page.landing_mts()
        Page.choice_iplayer()
        Page.add_land_button()
        Page.stream_create_button()


class SubscribeMt:
    def redirect_without_sub(self):
        request = BaseMt.just_click(self)
        assert request.status_code == requests.codes.ok, f'sub didn\'t done, status code = {request.status_code}"'

    def sub_on(self):
        click_id = Request_stuff.click_id_take(self)
        request_link = Request_urls.sub_on_request_url(click_id)
        request = BaseMt.just_click(request_link)
        assert request.status_code == requests.codes.ok, f'sub didn\'t done, status code = {request.status_code}"'

    def rebill(self):
        click_id = Request_stuff.click_id_take(self)
        request_link = Request_urls.sub_on_request_url(click_id)
        BaseMt.just_click(request_link)
        time.sleep(20)
        request_link = Request_urls.sub_rebill_request_url(click_id)
        request = BaseMt.just_click(request_link)
        assert request.status_code == requests.codes.ok, f'sub didn\'t done, status code = {request.status_code}"'

    def traffback(self):
        request = BaseMt.just_click(self)
        assert request.status_code == requests.codes.ok, f'sub didn\'t done, status code = {request.status_code}"'

    def sub_off(self):
        click_id = Request_stuff.click_id_take(self)
        request_link = Request_urls.sub_on_request_url(click_id)
        BaseMt.just_click(request_link)
        time.sleep(20)
        request_link = Request_urls.sub_off_request_url(click_id)
        request = BaseMt.just_click(request_link)
        assert request.status_code == requests.codes.ok, f'sub didn\'t done, status code = {request.status_code}"'
