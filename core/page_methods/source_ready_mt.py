from core.page_methods.partner_page import PartnerNavBorder
from core.page_methods.source_page import PartnerCreateSource


class SourceReadyMt:
    def create_source(self, link):
        Page = PartnerNavBorder(self, link)
        Page.partner_source()
        Page = PartnerCreateSource(self, link)
        Page.partner_source_create()
        Page.type_source()
        Page.source_name()
        Page.source_url()
        Page.create_source_button()
