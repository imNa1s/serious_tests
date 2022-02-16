import pytest

from core.page_methods.source_ready_mt import SourceReadyMt
from core.links import SiteLinks
from core.page_methods.ready_pages_mt import BrowserMt


@pytest.mark.create
@pytest.mark.source
def test_create_source(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    BrowserMt.partner_redirect(browser, link)
    SourceReadyMt.create_source(browser, link)
