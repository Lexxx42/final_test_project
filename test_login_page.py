''' Tests for login page.
\nCode for all tests: pytest -v --tb=line --language=en test_login_page.py
'''

from .pages.login_page import LoginPage

LINK = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'


def test_should_be_correct_url(browser):
    page = LoginPage(browser, LINK)
    page.open()
    page.should_be_login_url()


def test_should_be_login_form_on_login_page(browser):
    page = LoginPage(browser, LINK)
    page.open()
    page.should_be_login_form()


def test_should_be_registartion_form_on_login_page(browser):
    page = LoginPage(browser, LINK)
    page.open()
    page.should_be_register_form()
