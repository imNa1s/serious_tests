import pytest

from core.links import SiteLinks, LinksToCheck
from core.ready_function import BrowserMt


@pytest.mark.create
@pytest.mark.stream
def test_create_stream(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    BrowserMt.partner_redirect(browser, link)
    BrowserMt.create_stream(browser, link)
    check = browser.current_url
    assert check != LinksToCheck.create_stream_link, 'stream not created'
