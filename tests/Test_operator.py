from core.links import SiteLinks
from core.Page_methods.operator_ready_mt import OperatorReadyMt
from core.ready_page_mt import BrowserMt


def test_js(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    OperatorReadyMt.opeartor_create(browser, link)
