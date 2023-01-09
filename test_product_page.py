# -*- coding: utf-8 -*-
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_product_added_to_basket_message()
    page.should_be_basket_sum_price_message()
    page.product_name_is_the_same()
    page.price_is_the_same()