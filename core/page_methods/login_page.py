from core.core_mt import BaseMt
from core.locators import LoginLocators


class LoginPage(BaseMt, LoginLocators):
    def write_email_admin(self):
        assert self.is_element_present(*LoginLocators.email_id), "can't find field email"
        self.find_el_write(*LoginLocators.email_id, 'admin.demo@wap.com')

    def write_password_admin(self):
        assert self.is_element_present(*LoginLocators.password_id), "can't find field password"
        self.find_el_write(*LoginLocators.password_id, 'admin.demo')

    def captcha_click(self):
        assert self.is_element_present(*LoginLocators.captcha_id), "can't find field captcha"
        self.find_el_click(*LoginLocators.captcha_id)

    def login_button(self):
        assert self.is_element_present(*LoginLocators.button_submit), "can't find button login"
        self.find_el_click(*LoginLocators.button_submit)
