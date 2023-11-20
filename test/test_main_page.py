import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
from ..settings import sets
import random


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        hash_name = "%032x" % random.getrandbits(128)
        self.email_for_subscribe = f"{hash_name}@mail.com"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_main_page_header(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_login()
        page.is_button_feedback()
        page.is_button_delivery()
        page.is_button_warranty()
        page.is_phone_number()
        page.is_button_currency()
        page.is_uah_currency()
        page.is_eur_currency()
        page.is_usd_currency()
        page.is_search_field()
        page.is_button_search()
        page.is_button_cart()
        page.is_button_favorite()
        page.is_logo()
        page.is_button_hits()
        page.is_button_sales()
        page.is_button_new()
        page.is_cat_samsung()
        page.is_subcat_samsung_j701()

    def test_main_page_content(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_main_slider()
        page.is_main_cat()
        page.is_main_subcat()
        page.is_info_block_refund()
        page.is_info_block_delivery()
        page.is_info_block_otsrochka()
        page.is_info_block_support()
        page.is_show_all_new_products()
        page.is_show_next_new_products()
        page.is_show_prev_new_products()
        page.is_section_new_products()
        page.is_new_product_8()
        page.is_show_all_hits_products()
        page.is_show_next_hits_products()
        page.is_show_prev_hits_products()
        page.is_section_hits_products()
        page.is_hit_product()
        page.is_show_next_trend_products()
        page.is_show_prev_trend_products()
        page.is_trend_product()

    def test_main_page_footer(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_subscribe_btn()
        page.is_subscribe_input()
        page.is_footer_logo()

    def test_main_page_subscribe_action(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.subscribe_action(self.email_for_subscribe)
        page.is_alert_success_after_subscribe()




