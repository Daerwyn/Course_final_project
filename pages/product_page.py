from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_product_added_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE),\
            "There is no message indicating that the item has been added to the cart on the page"

    def should_be_basket_sum_price_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_SUM_PRICE_MESSAGE), \
            "There is no message with the cart total on the page"

    def product_name_is_the_same(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_added_to_basket_message = self.browser.find_element(*ProductPageLocators.
                                                                    PRODUCT_ADDED_TO_BASKET_MESSAGE).text
        assert product_name in product_added_to_basket_message, f"The product name in message must be " \
                                                                f"\"{product_name}\""

    def price_is_the_same(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_sum_price = self.browser.find_element(*ProductPageLocators.BASKET_SUM_PRICE).text
        assert product_price == basket_sum_price, f"The total price of the items in the cart should be " \
                                                  f"\"{product_price}\""
