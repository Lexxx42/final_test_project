''' Page Object for the login page. '''

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.should_be_valid_registration_form()
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)
        paswd_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASWD)
        paswd_field.send_keys(password)
        paswd_confirm_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASWD)
        paswd_confirm_field.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_register.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/', \
            'Current URL should be http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), f'There is no login form on {self.url} page.'

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_FORM), f'There is no registration form on {self.url} page.'

    def should_be_valid_registration_form(self):
        self.should_be_register_form()
        self.should_be_field_email_address_in_register_form()
        self.should_be_field_password_in_register_form()
        self.should_be_field_confirm_password_in_register_form()
        self.should_be_button_register_in_register_form()

    def should_be_field_email_address_in_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_EMAIL), f'There is no Email address field on {self.url} page.'

    def should_be_field_password_in_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASWD), f'There is no Password field on {self.url} page.'

    def should_be_field_confirm_password_in_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_CONFIRM_PASWD), f'There is no Confirm password field on {self.url} page.'

    def should_be_button_register_in_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.BUTTON_REGISTER), f'There is no Register button on {self.url} page.'
