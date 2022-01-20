import time

import requests

from core.core_mt import BaseMt
from core.links import SiteLinks, LinksReqTds
from core.login_page import LoginPage
from core.request_stf import Request_stuff, Request_urls


def login_pass(browser, link):
    link_check = SiteLinks.login_link_test1
    Page = LoginPage(browser, link)
    Page.open()
    Page.write_email_admin()
    Page.write_password_admin()
    Page.login_button()
    time.sleep(2)
    to_check = browser.current_url
    assert link_check != to_check, "you did't login"


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
