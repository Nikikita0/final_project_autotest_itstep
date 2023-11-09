import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
from ..settings import sets


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        pass

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




