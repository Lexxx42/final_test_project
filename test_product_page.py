''' Tests for product page.
\nCode for all tests: pytest -v -s -rx --tb=line --language=en test_product_page.py
\nNegative tests only: pytest -v -s -rx -m negative --tb=line --language=en test_product_page.py
\nInheritance advantages tests: pytest -v -s -rx -m adv_inheritance --tb=line --language=en test_product_page.py
\nBasket tests: pytest -v -s -rx -m basket --tb=line --language=en test_product_page.py
\nUser test: pytest -v -s -rx -m user_tests_with_registartion --tb=line --language=en test_product_page.py
\nReview tests: pytest -v --tb=line --language=en -m need_review
'''

import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


@pytest.mark.need_review
@pytest.mark.params
@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6',
                                  pytest.param(
                                      'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7',
                                      marks=pytest.mark.xfail(
                                          reason='Product name added to the basket not match product name on the product card.')),
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8',
                                  'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_disappeared_button_add_to_basket()
    page.should_be_correct_work_of_basket()


@pytest.mark.xfail(reason='Negative check 1')
@pytest.mark.negative
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK, timeout=0)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.negative
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, LINK, timeout=0)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail(reason='Negative check 3')
@pytest.mark.negative
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, LINK, timeout=0)
    page.open()
    page.add_to_basket()
    page.should_be_disappeared_success_message()


@pytest.mark.adv_inheritance
def test_guest_should_see_login_link_on_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
@pytest.mark.adv_inheritance
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()


@pytest.mark.need_review
@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_list_if_basket_is_empty()
    basket_page.should_be_notification_about_empty_basket_if_basket_is_empty()


@pytest.mark.user_tests_with_registartion
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = ProductPage(browser, link)
        new_user_email = str(time.time()) + "@fakemail.org"
        new_user_paswd = 'strong_pass1'
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(new_user_email, new_user_paswd)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = ProductPage(browser, link, timeout=0)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_not_be_disappeared_button_add_to_basket()
        page.should_be_correct_work_of_basket()
