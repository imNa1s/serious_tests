

from core.page_methods.operator_page import OperatorMT


class OperatorReadyMt:
    def operator_create(self, link):
        Page = OperatorMT(self, link)
        Page.operator_page_open()
        Page.operator_create_button()
        Page.operator_give_name()
        Page.operator_subnet()
        Page.operator_denied_devices()
        Page.operator_country()
        Page.operator_status()
        Page.operator_web()
        Page.operator_create_end_button()
