import pytest

from core.links import SiteLinks
from core.page_methods.ticket_ready_mt import TicketMt
from core.page_methods.ready_pages_mt import BrowserMt


@pytest.mark.test1
@pytest.mark.ticket
@pytest.mark.partner
def test_ticket_alert_admin(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    BrowserMt.partner_redirect(browser, link)
    TicketMt.create_tiket(browser, link)


@pytest.mark.test1
@pytest.mark.ticket
@pytest.mark.admin
def test_ticket_alert_partner(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    TicketMt.create_adm_ticket(browser, link)
