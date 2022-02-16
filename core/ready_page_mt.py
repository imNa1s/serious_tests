import time

from core.links import SiteLinks
from core.Page_methods.login_page import LoginPage
from core.Page_methods.partner_page import GoToPartnerPage


class BrowserMt:
    def login_pass(self, link):
        link_check = SiteLinks.login_link_test1
        Page = LoginPage(self, link)
        Page.open()
        Page.write_email_admin()
        Page.write_password_admin()
        Page.login_button()
        time.sleep(2)
        to_check = self.current_url
        assert link_check != to_check, "you didn't login"

    def partner_redirect(self, link):
        Page = GoToPartnerPage(self, link)
        Page.partner_button()
        Page.testmail_parnter()
        Page.testmail_autorization()
