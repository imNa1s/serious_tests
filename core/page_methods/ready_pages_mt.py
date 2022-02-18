import time

from core.links import SiteLinks
from core.page_methods.login_page import LoginPage
from core.page_methods.partner_page import GoToPartnerPage, AdmPartnerPage


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
        Page = AdmPartnerPage(self, link)
        Page.partner_page_open()
        Page = GoToPartnerPage(self, link)
        Page.testmail_parnter()
        Page.testmail_autorization()
