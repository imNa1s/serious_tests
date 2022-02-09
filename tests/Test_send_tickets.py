import pytest

from core.links import SiteLinks
from core.ready_page_mt import BrowserMt


@pytest.mark.test1
@pytest.mark.ticket
@pytest.mark.alert
def test_ticket_alert(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    BrowserMt.partner_redirect(browser, link)
    BrowserMt.create_tiket(browser, link)
