import time
import pytest

from core.links import SiteLinks
from core.ready_function import login_pass
from core.take_all_stats import StatisticsMt


@pytest.mark.stats
@pytest.mark.date
def test_statistic_date(browser):
    link = SiteLinks.login_link_test1
    login_pass(browser, link)
    StatisticsMt.stats_date(browser, browser.current_url)
    time.sleep(1)


@pytest.mark.stats
@pytest.mark.transition
# def test_transitions(browser):
#     link = SiteLinks.login_link_test1
#     login_pass(browser, link)
#     StatisticsMt.transition(browser, browser.current_url)
#     time.sleep(1)


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