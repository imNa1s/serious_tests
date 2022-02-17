from core.core_mt import BaseMt
from core.locators import AdmSideBarLocators, CategoryLocators


class CategoryMT(BaseMt):
    def category_page_open(self):
        assert self.is_element_present(*AdmSideBarLocators.landing_menu), 'can\'t find landing'
        self.find_el_click(*AdmSideBarLocators.landing_menu)
        assert self.is_element_present(*AdmSideBarLocators.category_menu), 'can\'t find button category'
        self.find_el_click(*AdmSideBarLocators.category_menu)

    def category_create(self):
        assert self.is_element_present(*CategoryLocators.category_add), 'can\'t find button create'
        self.find_el_click(*CategoryLocators.category_add)

    def category_name(self):
        assert self.is_element_present(*CategoryLocators.category_name), 'can\'t find field to name'
        self.find_el_write(*CategoryLocators.category_name, 'autotest')

    def category_status(self):
        assert self.is_element_present(*CategoryLocators.category_status), 'can\'t find checkbox status'
        self.find_el_click(*CategoryLocators.category_status)

    def category_create_end_button(self):
        assert self.is_element_present(*CategoryLocators.category_save_button), 'can\'t find button save category'
        self.find_el_click(*CategoryLocators.category_save_button)
