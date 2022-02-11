import time

from core.links import SiteLinks
from core.login_page import LoginPage
from core.partner_page import GoToPartnerPage, PartnerNavBorder, PartnerCreateSource, PartnerCreateStream, PartnerTicketsMt


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

    def create_source(self, link):
        Page = PartnerNavBorder(self, link)
        Page.partner_source()
        Page = PartnerCreateSource(self, link)
        Page.partner_source_create()
        Page.type_source()
        Page.source_name()
        Page.source_url()
        Page.create_source_button()

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

    def create_tiket(self, link):
        Page = PartnerNavBorder(self, link)
        Page.partner_tickets()
        Page = PartnerTicketsMt(self, link)
        Page.switch_to_old_win()
        alert_icon_bef = Page.see_alert()
        Page.switch_to_new_win()
        Page.ticket_create()
        Page.ticket_type()
        Page.ticket_type_message()
        Page.ticket_message()
        Page.ticket_send_btn()
        Page.switch_to_old_win()
        Page.ref()
        alert_icon_af = Page.see_alert()
        assert alert_icon_bef != alert_icon_af, 'no new alerts'
