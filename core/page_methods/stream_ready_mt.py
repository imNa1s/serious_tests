import time

from core.page_methods.partner_page import PartnerNavBorder
from core.page_methods.stream_page import PartnerCreateStream


class StreamReadyMt:
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
