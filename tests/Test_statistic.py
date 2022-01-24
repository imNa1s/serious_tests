import time
import pytest

from core.links import SiteLinks
from core.ready_function import login_pass
from core.take_all_stats import StatisticsMt
from tr import StatisticsMt1


@pytest.mark.stats
@pytest.mark.date
def test_statistic_date(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    StatisticsMt.stats_date(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.stats
@pytest.mark.transition
def test_transitions(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    StatisticsMt.transition(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.stats
@pytest.mark.unic
def test_unic(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    StatisticsMt.unic_request(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.stats
@pytest.mark.traffback
def test_traffback(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    StatisticsMt.traffback_request(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.stats
@pytest.mark.subscribe
def test_subscribe(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    StatisticsMt.subscribe(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.stats
@pytest.mark.conversion
def test_conversion(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    StatisticsMt.conversion(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.stats
@pytest.mark.unsub
def test_unsub(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    StatisticsMt.unsub(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.stats
@pytest.mark.rebill
def test_rebill(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    StatisticsMt.make_rebill(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.stats
@pytest.mark.buyout
def test_buyout(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    StatisticsMt.buyout(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.stats
@pytest.mark.nk
def test_nk(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    StatisticsMt.NK(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.stats
@pytest.mark.epc
def test_epc(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    StatisticsMt.EPC(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.stats
@pytest.mark.partner
def test_partner(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    StatisticsMt.partner(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.stats
@pytest.mark.system_pay
def test_system_pay(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    StatisticsMt.system_pay(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.stats
@pytest.mark.all_pay
def test_all_pay(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    StatisticsMt.all_pay(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.stats
@pytest.mark.complaints
def test_complaints(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    StatisticsMt.complaints(browser, browser.current_url)
    time.sleep(1)


# @pytest.mark.stats
# @pytest.mark.complaints
# def test_complaints(browser):
#     link = SiteLinks.login_link_test1
#     login_pass(browser, link)
#     StatisticsMt1.all_statistic_in_one(browser, browser.current_url)
#     time.sleep(1)
