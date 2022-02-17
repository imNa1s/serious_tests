from core.links import SiteLinks
from core.page_methods.operator_ready_mt import OperatorReadyMt
from core.page_methods.ready_pages_mt import BrowserMt


def test_js(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    OperatorReadyMt.operator_create(browser, link)
