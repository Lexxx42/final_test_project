''' Page Object for the basket page. '''

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_notification_about_empty_basket_if_basket_is_empty(self):
        assert self.is_element_present(
            *BasketPageLocators.NOTIFICATION_EMPTY_BASKET), \
            f'No notification about empty basket on {self.url} page, but should be'

    def should_not_be_product_list_if_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_LIST), \
            f'Product list is presented, but shouldn\'t be on {self.url} page'

    def should_be_product_list_if_basket_is_not_empty(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_LIST), f'No product list in basket on {self.url} page, but should be'
