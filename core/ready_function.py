import time

import requests

from core.core_mt import BaseMt
from core.links import SiteLinks, LinksReqTds
from core.login_page import LoginPage
from core.request_stf import Request_stuff, Request_urls
from core.statistc_base import StatsMt


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


def transition(browser, link):
    Page = StatsMt(browser, link)
    Page.go_to_statistic()
    stats = Page.save_stats()
    stats_pars1 = Page.transition_take(stats)
    sub_on()
    time.sleep(20)
    Page.ref()
    stats = Page.save_stats()
    stats_pars2 = Page.transition_take(stats)
    print(f'transition before request {stats_pars1}, after request {stats_pars2}')
    assert stats_pars1 != stats_pars2, "they equal"


def sub_on():
    click_id = Request_stuff.click_id_take(LinksReqTds.tds_click_test)
    request_link = Request_urls.sub_on_request_url(click_id)
    request = BaseMt.just_click(request_link)
    assert request.status_code == requests.codes.ok, f'sub didn\'t done, status code = {request.status_code}"'