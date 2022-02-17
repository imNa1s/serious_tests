import pytest

from core.links import SiteLinks
from core.page_methods.category_ready_mt import CategoryReadyMt
from core.page_methods.ready_pages_mt import BrowserMt


@pytest.mark.category
@pytest.mark.create
def test_category(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    CategoryReadyMt.category_create(browser, link)

