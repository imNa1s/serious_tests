import time
import pytest

from core.links import SiteLinks
from core.page_methods.login_page import LoginPage
from core.page_methods.partner_page import GoToPartnerPage, AdmSideNavBorder
from core.page_methods.ready_pages_mt import BrowserMt


@pytest.mark.login
@pytest.mark.admin
def test_login(browser):
    link = SiteLinks.login_link_test1
    link_check = SiteLinks.login_link_test1
    Page = LoginPage(browser, link)
    Page.open()
    Page.write_email_admin()
    Page.write_password_admin()
    Page.login_button()
    time.sleep(4)
    to_check = browser.current_url
    assert link_check != to_check, "you did't login"


@pytest.mark.login
@pytest.mark.admin_fail
def test_login_fail(browser):
    link = SiteLinks.login_link_test1
    link_check = SiteLinks.login_link_test1
    Page = LoginPage(browser, link)
    Page.open()
    Page.write_email_admin()
    Page.write_password_admin()
    Page.login_button()
    time.sleep(4)
    to_check = browser.current_url
    assert link_check != to_check, "you login"


@pytest.mark.login
@pytest.mark.admin_partner
def test_login_as_partner(browser):
    link = SiteLinks.login_link_test1
    BrowserMt.login_pass(browser, link)
    Page = AdmSideNavBorder(browser, link)
    Page.partner_page_open()
    Page = GoToPartnerPage(browser, link)
    Page.testmail_parnter()
    check_link = browser.current_url
    Page.testmail_autorization()
    to_check = browser.current_url
    assert check_link != to_check, "you didn't login as partner"
