import pytest
from .pages.product_page import ProductPage

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


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
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_disappeared_button_add_to_basket()
    page.should_be_correct_work_of_basket()


@pytest.mark.xfail
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


@pytest.mark.xfail
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


@pytest.mark.adv_inheritance
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()

# pytest -v -s -rx --tb=line --language=en test_product_page.py
# negative tests only: pytest -v -s -rx -m negative --tb=line --language=en test_product_page.py
# inheritance advantages tests: pytest -v -s -rx -m adv_inheritance --tb=line --language=en test_product_page.py
