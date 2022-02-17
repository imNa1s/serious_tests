from core.page_methods.country_page import CountryMt


class CountryReadyMt:
    def create_country(self, link):
        Page = CountryMt(self, link)
        Page.country_page_open()
        Page.country_create_button()
        Page.country_name()
        Page.country_iso()
        Page.country_create_end_button()
