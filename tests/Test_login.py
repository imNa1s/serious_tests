import time
import pytest

from core.links import SiteLinks
from core.login_page import LoginPage


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


@pytest.mark.login_fail
@pytest.mark.admin
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