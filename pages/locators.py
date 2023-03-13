from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//form[@class="add-to-basket"]/button')

    MESSAGE_WITH_PRODUCT_NAME = (By.CSS_SELECTOR, 'div.alert:nth-child(1)')
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    PRODUCT_NAME_IN_CARD = (By.CSS_SELECTOR, '.product_main h1')

    MESSAGE_OF_BASKET_COST = (By.CSS_SELECTOR, 'div.alert:nth-child(3)')
    BASKET_COST_IN_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner p strong')
    COST_OF_PRODUCT = (By.CSS_SELECTOR, '.price_color:nth-child(2)')
