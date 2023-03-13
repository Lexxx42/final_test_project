from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON), f'No Add to basket button on {self.url} page'

    def add_to_basket(self):
        self.should_be_add_to_basket_button()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_correct_work_of_basket(self):
        self.should_be_match_of_product_name_and_basket_in_message()
        self.should_be_match_of_product_cost_and_basket_in_message()

    def should_be_match_of_product_name_and_basket_in_message(self):
        """ Сообщение о том, что товар добавлен в корзину.
        Название товара в сообщении должно совпадать с тем товаром,
        который вы действительно добавили."""
        self.should_be_message_of_added_product()
        self.should_be_product_name_message_match_product_name_card()

    def should_be_message_of_added_product(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_WITH_PRODUCT_NAME), f'No message of added product on {self.url} page'

    def should_be_product_name_message_match_product_name_card(self):
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        product_name_in_card = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CARD)
        assert product_name_in_message.text == product_name_in_card.text, \
            'Product name added to the basket not match product name on the product card.' \
            f'{product_name_in_message.text} should match {product_name_in_card.text}'

    def should_be_match_of_product_cost_and_basket_in_message(self):
        """ Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара."""
        self.should_be_message_of_basket_total()
        self.should_be_equal_basket_price_in_message_and_product_prise()

    def should_be_message_of_basket_total(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_OF_BASKET_COST), f'No message of basket total on {self.url} page'

    def should_be_equal_basket_price_in_message_and_product_prise(self):
        basket_price_in_message = self.browser.find_element(*ProductPageLocators.BASKET_COST_IN_MESSAGE)
        product_price_in_card = self.browser.find_element(*ProductPageLocators.COST_OF_PRODUCT)
        assert basket_price_in_message.text == product_price_in_card.text, \
            'Product cost on the card should be equal basket cost.' \
            f'{basket_price_in_message.text} should match {product_price_in_card.text}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_WITH_PRODUCT_NAME), \
            'Success message is presented, but should not be'

    def should_not_be_disappeared_button_add_to_basket(self):
        assert not (self.is_disappeared(*ProductPageLocators.ADD_TO_BASKET_BUTTON)), \
            'Button Add to basket disappeared, but should not be'

    def should_be_disappeared_success_message(self):
        assert (self.is_disappeared(*ProductPageLocators.MESSAGE_WITH_PRODUCT_NAME)), \
            'Success message should be disappeared, but still present'
