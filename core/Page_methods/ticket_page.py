import time

from core.partner_page import PartnerNavBorder, PartnerTicketsMt, GoToPartnerPage


class TicketMt():
    def create_tiket(self, link):
        Page = PartnerNavBorder(self, link)
        Page.partner_tickets()
        Page = PartnerTicketsMt(self, link)
        Page.switch_to_old_win()
        alert_icon_bef = Page.see_adm_alert()
        Page.switch_to_new_win()
        Page.ticket_create()
        Page.ticket_type()
        Page.ticket_type_message()
        Page.ticket_message()
        Page.ticket_send_btn()
        Page.switch_to_old_win()
        Page.ref()
        alert_icon_af = Page.see_adm_alert()
        assert alert_icon_bef != alert_icon_af, 'no new alerts'

    def create_adm_ticket(self, link):
        Page = GoToPartnerPage(self, link)
        Page.partner_button()
        Page.testmail_parnter()
        Page.testmail_autorization()
        Page = PartnerTicketsMt(self, link)
        alert_icon_before = Page.see_partner_alert()
        Page.switch_to_old_win()
        Page.adm_ticket_send_button()
        Page.adm_ticket_type_choice()
        Page.adm_ticket_theme()
        Page.adm_ticket_message()
        Page.adm_ticket_send_message_button()
        Page.switch_to_new_win()
        Page.ref()
        alert_icon_after = Page.see_partner_alert()
        assert alert_icon_before != alert_icon_after, 'no new alerts'
        Page.partner_alert_button()
        header = Page.partner_alert_header_text()
        print(f'\nlast alert header text - "{header}"')
        assert header == 'Создан новый тикет "autotest" с сообщением:', 'it\'s not ticket alert'

