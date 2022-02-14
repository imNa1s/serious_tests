import time

import pytest

from core.links import SiteLinks
from core.ready_page_mt import BrowserMt
from core.statistic.take_sub_stats import SubStatisticsMt


@pytest.mark.sub_stats
@pytest.mark.date
def test_statistic_date(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    SubStatisticsMt.sub_stats_date(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.sub_stats
@pytest.mark.subscribe
def test_subscribe(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    SubStatisticsMt.sub_stats_date(browser, browser.current_url)
    SubStatisticsMt.sub_stats_sub(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.sub_stats
@pytest.mark.subscribe_active
def test_active_subscribe(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    SubStatisticsMt.sub_stats_date(browser, browser.current_url)
    SubStatisticsMt.sub_stats_active(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.sub_stats
@pytest.mark.unsub
def test_unsub(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    SubStatisticsMt.sub_stats_date(browser, browser.current_url)
    SubStatisticsMt.sub_stats_unsub(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.sub_stats
@pytest.mark.unsub_1st
def test_unsub_1st(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    SubStatisticsMt.sub_stats_date(browser, browser.current_url)
    SubStatisticsMt.sub_stats_unsub_1st(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.sub_stats
@pytest.mark.rebill
def test_rebill(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    SubStatisticsMt.sub_stats_date(browser, browser.current_url)
    SubStatisticsMt.sub_stats_rebill(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.sub_stats
@pytest.mark.rebill_abonent
def test_rebill_abonent(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    SubStatisticsMt.sub_stats_date(browser, browser.current_url)
    SubStatisticsMt.sub_stats_rebill_abonent(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.sub_stats
@pytest.mark.price
def test_price(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    SubStatisticsMt.sub_stats_date(browser, browser.current_url)
    SubStatisticsMt.sub_stats_price(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.sub_stats
@pytest.mark.buyout
def test_buyout(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    SubStatisticsMt.sub_stats_date(browser, browser.current_url)
    SubStatisticsMt.sub_stats_buyout(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.sub_stats
@pytest.mark.rebill_buyout
def test_rebill_buyout(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    SubStatisticsMt.sub_stats_date(browser, browser.current_url)
    SubStatisticsMt.sub_stats_rebill_buyout(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.sub_stats
@pytest.mark.partner
def test_partner(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    SubStatisticsMt.sub_stats_date(browser, browser.current_url)
    SubStatisticsMt.sub_stats_partner(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.sub_stats
@pytest.mark.system
def test_system(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    SubStatisticsMt.sub_stats_date(browser, browser.current_url)
    SubStatisticsMt.sub_stats_system(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.sub_stats
@pytest.mark.all_pay
def test_all_pay(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    SubStatisticsMt.sub_stats_date(browser, browser.current_url)
    SubStatisticsMt.sub_stats_all_pay(browser, browser.current_url)
    time.sleep(1)
