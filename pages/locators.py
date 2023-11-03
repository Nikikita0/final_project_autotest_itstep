from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_SIGNUP = (By.XPATH, "//div[@class='top_bar_user']/a[@href='user/login']")
    FEEDBACK = (By.XPATH, '//a[text()="Обратная связь"]')
    DELIVERY = (By.XPATH, '//a[text()="Доставка"]')
    WARRANTY = (By.XPATH, '//a[text()="Гарантия"]')
    PHONE = (By.XPATH, '//div[text()="+38 098 911 95 22"]')
    CURRENCY_MENU = (By.XPATH, '//select[@id = "currency"]')
    USD_OPTION = (By.XPATH, '//option[@value="USD"]')
    UAH_OPTION = (By.XPATH, '//option[@value=""]')
    EUR_OPTION = (By.XPATH, '//option[@value="EUR"]')
    SEARCH_FIELD = (By.XPATH, '//input[@id="typeahead"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@class="header_search_button trans_300"]')
    CART = (By.XPATH, '//a[@href="cart/show"]')
    FAVORITE = (By.XPATH, '//a[@href="wish/show"]')
    LOGO = (By.XPATH, '//img[@src="images/logo.png"]')
    HITS = (By.XPATH, '//a[@href="main/showHit]"')
    SALES = (By.XPATH, '//a[@href="main/showSale"]"')
    NEW = (By.XPATH, '//a[@href="main/showNew"]"')
    SAMSUNG_CAT = (By.XPATH, '//div[text()="Samsung"]')
    SAMSUNG_J701 = (By.XPATH, '//a[text()="Samsung J701"]')
    SUBSCRIBE_BTN =(By.XPATH, '//button[text()="Подписаться!"]')
    EMAIL_TO_SUBSCRIBE = (By.XPATH, '//input[@class="newsletter_input"]')
    LOGO_FOOTER = (By.XPATH, '//img[@src="images/logo-footer.png"]')


