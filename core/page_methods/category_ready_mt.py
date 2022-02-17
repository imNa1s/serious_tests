from core.page_methods.category_page import CategoryMT


class CategoryReadyMt:
    def category_create(self, link):
        Page = CategoryMT(self, link)
        Page.category_page_open()
        Page.category_create()
        Page.category_name()
        Page.category_status()
        Page.category_create_end_button()
