import time

from core.links import SiteLinks
from core.Page_methods.login_page import LoginPage
from core.Page_methods.partner_page import GoToPartnerPage, PartnerNavBorder, PartnerCreateStream


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

    def create_stream(self, link):
        Page = PartnerNavBorder(self, link)
        Page.partner_stream()
        Page = PartnerCreateStream(self, link)
        Page.partner_stream_create()
        Page.partner_stream_name()
        Page.stream_source()
        Page.stream_traffback_url()
        Page.stream_postback()
        Page.postback_actions_all()
        Page.type_stream_redirect()
        Page.landing_page_display()
        Page.ya_redirect_ban()
        Page.landing_mts()
        Page.choice_iplayer()
        Page.add_land_button()
        Page.stream_create_button()
        time.sleep(2)
