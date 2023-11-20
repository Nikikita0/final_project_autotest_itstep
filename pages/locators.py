from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_SIGNUP = (By.XPATH, "//div[@class='top_bar_user']/a[@href='user/login']")

    DETAILS = (By.XPATH, '//ul[@class="standard_dropdown top_bar_dropdown"]')
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
    HITS = (By.XPATH, "//span[text()='Хиты']")
    SALES = (By.XPATH, "//span[text()='Скидки']")
    NEW = (By.XPATH, "//span[text()='Новинки']")

    SAMSUNG_CAT = (By.XPATH, "//div[@class='search-by-level-1' and text()='Samsung']")
    SAMSUNG_J701 = (By.XPATH, '//a[text()="Samsung J701"]')

    SUBSCRIBE_BTN = (By.XPATH, '//button[text()="Подписаться!"]')
    EMAIL_TO_SUBSCRIBE = (By.XPATH, '//input[@class="newsletter_input"]')

    LOGO_FOOTER = (By.XPATH, '//img[@src="images/logo-footer.png"]')

    ALERT_SUCCESS = (By.XPATH, '//div[@id="alert-success"]')
    ALERT_ERROR = (By.XPATH, "//div[@id = 'alert-error']")

    LOGOUT = (By.XPATH, "//div[@class='top_bar_user']//a[@href = 'user/logout']")




class MainPageLocators:
    SCREEN_SLIDER = (By.XPATH, "//div[@class = 'screen_slider']")

    MAIN_CAT = (By.XPATH, '//a[@href="category/zaryadki"]')
    MAIN_SUBCAT = (By.XPATH, '//a[@href="category/Besprovodnye-BZU"]')
    RETURN_ITEM = (By.XPATH, '//div[@class="row"]/div[1]/div[@class="char_item d-flex flex-row align-items-center justify-content-start"]')
    DELIVERY_ITEM = (By.XPATH, '//div[@class="row"]/div[2]/div[@class="char_item d-flex flex-row align-items-center justify-content-start"]')
    PAYMENT_ITEM = (By.XPATH, '//div[@class="row"]/div[3]/div[@class="char_item d-flex flex-row align-items-center justify-content-start"]')
    SUPPORT_ITEM = (By.XPATH, '//div[@class="row"]/div[4]/div[@class="char_item d-flex flex-row align-items-center justify-content-start"]')

    SHOW_ALL_NEW = (By.XPATH, '//a[text()="Показать все" and @href="main/showNew"]')
    SHOW_NEXT_NEW = (By.XPATH, '//div[@class="arrivals_nav arrivals_next"]')
    SHOW_PREV_NEW = (By.XPATH, '//div[@class="arrivals_nav arrivals_prev"]')
    NEW_PRODUCT_PANEL = (By.XPATH, '//div[@class="product_panel panel active"]')
    NEW_PRODUCT = (By.XPATH, '//div[@data-slick-index="2"]/div[2]//div[@class="product_item is_new d-flex flex-column align-items-center justify-content-center text-center"]')

    SHOW_ALL_HITS = (By.XPATH, '//a[text()="Показать все" and @href="main/showHit"]')
    SHOW_NEXT_HITS = (By.XPATH, '//div[@class="best_next best_nav"]')
    SHOW_PREV_HITS = (By.XPATH, '//div[@class="best_prev best_nav"]')
    HITS_PRODUCT_PANEL = (By.XPATH, '//div[@class="bestsellers_panel panel active"]')
    HITS_PRODUCT = (By.XPATH, '//div[@class="bestsellers_panel panel active"]//div[@data-slick-index="4"]/div[2]/div[@class="bestsellers_item"]')

    SHOW_NEXT_TRENDS = (By.XPATH, '//div[@class="trends_next trends_nav slick-arrow"]')
    SHOW_PREV_TRENDS = (By.XPATH, '//div[@class="trends_prev trends_nav slick-arrow"]')
    TREND_PRODUCT = (By.XPATH, '//img[@src="content_images/6a2acee6946baaf0709990b1a544e9a8.jpg"]/ancestor::div[@style="height: 415px;"]')  # У меня таких элементов 3 находит я не знаю как тут найти уникальный


class SignupLoginPageLocators:
    GO_TO_SIGNUP = (By.XPATH, "//a[@href = 'user/signup']")
    H1_SIGNUP = (By.XPATH, "//h1[text() = 'Регистрация']")
    INPUT_EMAIL = (By.XPATH, "//input[@name = 'email']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name = 'password']")
    BUTTON_SIGNUP = (By.XPATH, "//button[text() = 'Зарегистрироваться']")
    H1_VHOD = (By.XPATH, "//h1[text() = 'Вход']")
    BUTTON_LOGIN = (By.XPATH, "//button[text() = 'Войти']")


class OrderPageLocators:
    FIRST_PRODUCT = (By.XPATH, "//div[@class = 'new_arrivals']//div[@class = 'slick-list draggable']/div/div[1]/div[1]")
    BUTTON_ADD_FIRST_PRODUCT = (By.XPATH, "//div[@class = 'new_arrivals']//div[@class = 'slick-list draggable']/div/div[1]/div[1]//button[text() = 'В корзину!']")
    PRICE_FIRST_PRODUCT = (By.XPATH, "//div[@class = 'new_arrivals']//div[@class = 'slick-list draggable']/div/div[1]/div[1]//div[@class = 'product_price']")
    BTN_CONTINUE_SHOP_POPUP = (By.XPATH, "//button[text() = 'Продолжить покупки']")
    SECOND_PRODUCT_INPUT_NUMBER_QTY = (By.XPATH, "//div[@class = 'shop_content']//div[@id = 'product']/div[1]//input[@type = 'number']")
    PRICE_SECOND_PRODUCT = (By.XPATH, "//div[@class = 'shop_content']//div[@id = 'product']/div[1]//div[@class = 'product_price']")
    BUTTON_ADD_SECOND_PRODUCT = (By.XPATH, "//div[@class = 'shop_content']//div[@id = 'product']/div[1]//button")
    TOTAL_PRICE = (By.XPATH, "//tr[@class = 'cart-cena']/td[2]")
    QTY = (By.XPATH, "//tr[@class = 'cart-itogo']/td[2]")
    CHECKOUT_BTN_POPUP = (By.XPATH, "//a[@href = 'cart/view']")
    CART_REG_FORM = (By.XPATH, "//div[@class = 'cart-reg']")
    INPUT_EMAIL = (By.XPATH, "//input[@name = 'email']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name = 'password']")
    INPUT_NOTE = (By.XPATH, "//textarea[@name= 'note']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[@class = 'btn green']")


class CabinetPageLocators:
    pass


class CategoryPageLocators:
    pass


class SearchPageLocators:
    pass
