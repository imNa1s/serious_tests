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


def sub_on():
    click_id = Request_stuff.click_id_take(LinksReqTds.tds_click_test)
    request_link = Request_urls.sub_on_request_url(click_id)
    request = BaseMt.just_click(request_link)
    assert request.status_code == requests.codes.ok, f'sub didn\'t done, status code = {request.status_code}"'


def traffback():
    request = BaseMt.just_click(LinksReqTds.tds_click_test_traffback)
    assert request.status_code == requests.codes.ok, f'sub didn\'t done, status code = {request.status_code}"'