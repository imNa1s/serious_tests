from core.partner_page import PartnerNavBorder, PartnerTicketsMt, GoToPartnerPage


class TicketMt():
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
