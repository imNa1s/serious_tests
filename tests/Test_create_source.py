import time
import pytest

from core.links import SiteLinks
from core.ready_function import BrowserMt


@pytest.mark.create
@pytest.mark.source
def test_create_source(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    BrowserMt.partner_redirect(browser, link)
    BrowserMt.create_source(browser, link)
