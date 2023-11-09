from ..pages import base_page, locators
import inspect


class MainPage(base_page.BasePage):
    def is_button_login(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGIN_SIGNUP), \
            "Button login is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_feedback(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотруднечества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.FEEDBACK), \
            "Button feedback is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_delivery(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Доставка' is not present"
        assert self.is_element_present(*locators.BasePageLocators.DELIVERY), \
            "Button delivery is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_warranty(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Гарантия' is not present"
        assert self.is_element_present(*locators.BasePageLocators.WARRANTY), \
            "Button warranty is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_phone_number(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE), \
            "Element 'Phone number' is not present or not correct"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_currency(self):
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY_MENU), \
            "Element 'currency' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_uah_currency(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY_MENU), \
            "Element 'currency' is not present or not intractable"
        assert self.is_element_present(*locators.BasePageLocators.UAH_OPTION), \
            "Element 'uah currency' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_eur_currency(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY_MENU), \
            "Element 'currency' is not present or not intractable"
        assert self.is_element_present(*locators.BasePageLocators.EUR_OPTION), \
            "Element 'eur currency' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_usd_currency(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY_MENU), \
            "Element 'currency' is not present or not intractable"
        assert self.is_element_present(*locators.BasePageLocators.USD_OPTION), \
            "Element 'usd currency' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_search_field(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_FIELD), \
            "Element 'search field' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_search(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_BUTTON), \
            "Element 'search button' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_cart(self):
        assert self.is_element_present(*locators.BasePageLocators.CART), \
            "Element 'cart' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_favorite(self):
        assert self.is_element_present(*locators.BasePageLocators.FAVORITE), \
            "Element 'search button' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO), \
            "Element 'Logo' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_hits(self):
        assert self.is_element_present(*locators.BasePageLocators.HITS), \
            "Element 'hits' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_sales(self):
        assert self.is_element_present(*locators.BasePageLocators.SALES), \
            "Element 'sales' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_new(self):
        assert self.is_element_present(*locators.BasePageLocators.NEW), \
            "Element 'new' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_cat_samsung(self):
        assert self.is_element_present(*locators.BasePageLocators.SAMSUNG_CAT), \
            "Element 'samsung category' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_subcat_samsung_j701(self):
        assert self.hover_action(*locators.BasePageLocators.SAMSUNG_CAT), \
            "Element 'samsung category' is not present"
        assert self.is_element_present(*locators.BasePageLocators.SAMSUNG_J701), \
            "Element 'samsung_j701 subcategory' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_main_slider(self):
        assert self.is_element_present(*locators.MainPageLocators.SCREEN_SLIDER), \
            "Element 'main slider' is not present"
        print(f"\n{inspect.currentframe().f_code.co_name} - Ok")

    def is_main_cat(self):
        assert self.is_element_present(*locators.MainPageLocators.MAIN_CAT), \
            "Element 'main category' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_main_subcat(self):
        assert self.hover_action(*locators.MainPageLocators.MAIN_CAT), \
            "Element 'main category' is not present"
        assert self.is_element_present(*locators.MainPageLocators.MAIN_SUBCAT), \
            "Element 'main subcategory' is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_refund(self):
        assert self.is_element_present(*locators.MainPageLocators.RETURN_ITEM), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_delivery(self):
        assert self.is_element_present(*locators.MainPageLocators.DELIVERY_ITEM), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_otsrochka(self):
        assert self.is_element_present(*locators.MainPageLocators.PAYMENT_ITEM), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_info_block_support(self):
        assert self.is_element_present(*locators.MainPageLocators.SUPPORT_ITEM), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_show_all_new_products(self):
        assert self.is_element_present(*locators.MainPageLocators.SHOW_ALL_NEW), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_show_next_new_products(self):
        assert self.is_element_present(*locators.MainPageLocators.SHOW_NEXT_NEW), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_show_prev_new_products(self):
        assert self.is_element_present(*locators.MainPageLocators.SHOW_PREV_NEW), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_section_new_products(self):
        assert self.is_element_present(*locators.MainPageLocators.NEW_PRODUCT_PANEL), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_new_product_8(self):
        assert self.is_element_present(*locators.MainPageLocators.NEW_PRODUCT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_show_all_hits_products(self):
        assert self.is_element_present(*locators.MainPageLocators.SHOW_ALL_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_show_next_hits_products(self):
        assert self.is_element_present(*locators.MainPageLocators.SHOW_NEXT_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_show_prev_hits_products(self):
        assert self.is_element_present(*locators.MainPageLocators.SHOW_PREV_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_section_hits_products(self):
        assert self.is_element_present(*locators.MainPageLocators.HITS_PRODUCT_PANEL), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_hit_product(self):
        assert self.is_element_present(*locators.MainPageLocators.HITS_PRODUCT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_show_next_trend_products(self):
        assert self.is_element_present(*locators.MainPageLocators.SHOW_NEXT_TRENDS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_show_prev_trend_products(self):
        assert self.is_element_present(*locators.MainPageLocators.SHOW_PREV_TRENDS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_trend_product(self):
        assert self.is_element_present(*locators.MainPageLocators.TREND_PRODUCT), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_subscribe_btn(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBE_BTN), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_subscribe_input(self):
        assert self.is_element_present(*locators.BasePageLocators.EMAIL_TO_SUBSCRIBE), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_footer_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO_FOOTER), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def subscribe_action(self, email):
        assert self.input_data(*locators.BasePageLocators.EMAIL_TO_SUBSCRIBE, email), \
            "The element is not inserted"
        assert self.click_element(*locators.BasePageLocators.SUBSCRIBE_BTN), \
            "The element is not clickable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_alert_success_after_subscribe(self):
        assert self.is_element_appears_after_while(*locators.BasePageLocators.ALERT_SUCCESS, timeout=5), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

