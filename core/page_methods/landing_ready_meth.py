import time

from core.page_methods.landing_page import AdmLandingPage


class LandingReadyMeth:
    def landing_create(self, link):
        Page = AdmLandingPage(self, link)
        Page.lp_page_open()
        Page.create_landing()
        Page.create_landing_name()
        Page.create_landing_provider()
        Page.create_landing_url()
        Page.create_landing_operator()
        Page.create_landing_category()
        Page.create_landing_type()
        Page.create_landing_static_pays()
        Page.create_landing_write_off()
        Page.create_landing_static_write_off()
        Page.create_landing_partners_payments()
        time.sleep(30)
