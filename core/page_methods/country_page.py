
from core.core_mt import BaseMt
from core.locators import CountryLocators, AdmSideBarLocators


class CountryMt(BaseMt):
    def country_page_open(self):
        assert self.is_element_present(*AdmSideBarLocators.landing_menu), 'can\'t find landing'
        self.find_el_click(*AdmSideBarLocators.landing_menu)
        assert self.is_element_present(*AdmSideBarLocators.country_menu), 'can\'t find button country'
        self.find_el_click(*AdmSideBarLocators.country_menu)

    def country_create_button(self):
        assert self.is_element_present(*CountryLocators.country_add), 'can\'t find button create country'
        self.find_el_click(CountryLocators.country_add)

    def country_name(self):
        assert self.is_element_present(*CountryLocators.country_name), 'can\'t find field name'
        self.find_el_write(*CountryLocators.country_name, 'autotest')

    def country_iso(self):
        assert self.is_element_present(*CountryLocators.country_iso), 'can\'t find field ISO'
        self.find_el_write(*CountryLocators.country_iso, 'AUTO')

    def country_create_end_button(self):
        assert self.is_element_present(*CountryLocators.country_save_button), 'can\'t find button save'
        self.find_el_click(*CountryLocators.country_save_button)
