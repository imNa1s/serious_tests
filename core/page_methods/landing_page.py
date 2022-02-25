from selenium.webdriver.support.ui import Select

from core.core_mt import BaseMt
from core.locators import AdmSideBarLocators, LandingLocators


class AdmLandingPage(BaseMt):
    def lp_page_open(self):
        assert self.is_element_present(*AdmSideBarLocators.landing_menu), 'can\'t find button "landing"'
        self.find_el_click(*AdmSideBarLocators.landing_menu)
        assert self.is_element_present(*AdmSideBarLocators.lp_menu), 'can\'t find button "lp"'
        self.find_el_click(*AdmSideBarLocators.lp_menu)

    def create_landing(self):
        assert self.is_element_present(*LandingLocators.landing_add), 'can\'t find button "add landing"'
        self.find_el_click(*LandingLocators.landing_add)

    def create_landing_name(self):
        assert self.is_element_present(*LandingLocators.landing_add_name), 'can\'t find field for name'
        self.find_el_write(*LandingLocators.landing_add_name, 'autotest')

    def create_landing_provider(self):
        assert self.is_element_present(*LandingLocators.landing_add_provider), 'can\'t find selector provider'
        select = Select(self.browser.find_element(*LandingLocators.landing_add_provider))
        select.select_by_value("Mobbilling")

    def create_landing_url(self):
        assert self.is_element_present(*LandingLocators.landing_add_url), 'can\'t find field for url'
        self.find_el_write(*LandingLocators.landing_add_url, 'http://google.com')

    def create_landing_operator(self):
        assert self.is_element_present(*LandingLocators.landing_add_operator), 'can\'t find select operator'
        select = Select(self.browser.find_element(*LandingLocators.landing_add_operator))
        select.select_by_value("26")

    def create_landing_category(self):
        assert self.is_element_present(*LandingLocators.landing_add_category), 'can\'t find selector category'
        select = Select(self.browser.find_element(*LandingLocators.landing_add_category))
        select.select_by_value("8")

    def create_landing_type(self):
        assert self.is_element_present(*LandingLocators.landing_add_type), 'can\'t find selector type'
        select = Select(self.browser.find_element(*LandingLocators.landing_add_category))
        select.select_by_value("1")

    def create_landing_static_pays(self):
        assert self.is_element_present(*LandingLocators.landing_add_static_pays), 'can\'t find checkbox static pays'
        self.find_el_click(*LandingLocators.landing_add_static_pays)

    def create_landing_write_off(self):
        assert self.is_element_present(*LandingLocators.landing_add_write_off), 'can\'t find field to write-off'
        self.find_el_write(*LandingLocators.landing_add_write_off, "100")

    def create_landing_static_write_off(self):
        assert self.is_element_present(*LandingLocators.landing_add_static_write_off), 'can\'t find static write-off'
        self.find_el_write(*LandingLocators.landing_add_static_write_off, "25")

    def create_landing_partners_payments(self):
        assert self.is_element_present(*LandingLocators.landing_add_partner_payments), 'can\'t find partner_payments'
        self.find_el_write(*LandingLocators.landing_add_partner_payments, "25")

    def create_landing_cpa(self):
        assert self.is_element_present(*LandingLocators.landing_add_price), 'can\'t find checkbox only CPA'
        self.find_el_click(*LandingLocators.landing_add_price)

    def create_landing_save(self):
        assert self.is_element_present(*LandingLocators.landing_add_save)
        self.find_el_click(*LandingLocators.landing_add_save)
