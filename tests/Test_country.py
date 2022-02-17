from core.links import SiteLinks
from core.page_methods.country_ready_mt import CountryReadyMt
from core.page_methods.ready_pages_mt import BrowserMt


def test_country(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    CountryReadyMt.create_country(browser, link)
