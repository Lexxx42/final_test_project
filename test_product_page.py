from .pages.product_page import ProductPage
import pytest


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
    page.add_to_basket()

# pytest -v -s -rx --tb=line --language=en test_product_page.py
