from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):

    def basket_has_no_items(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_ITEMS), \
            "There are items in the basket"

    def basket_is_empty_text(self):
        basket_empty_text = self.browser.find_element(*BasePageLocators.BASKET_IS_EMPTY_TEXT).text
        assert "Your basket is empty." in basket_empty_text, \
            f"There is no \"Your basket is empty.\" text"
