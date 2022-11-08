import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements

from my_data import IP, login, password

class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or f'http://{login}:{password}@{IP}/events_system_list_full.html'
            # url = os.getenv("MAIN_URL") or 'https://market.yandex.ru/'

        super().__init__(web_driver, url)

    # Main search field

    search = WebElement(id='text1')
    # search = WebElement(id='header-search')

    # Search button  
    search_run_button = WebElement(xpath='//*[@id="apply_filter_btn"]')
    # search_run_button = WebElement(id='apply_filter_btn')
    # search_run_button = WebElement(xpath='//button[@type="submit"]')

    # Titles of the products in search results //*[@id="event_table"]/div[5]/div/div[18]/div[2]
    products_titles = ManyWebElements(xpath ='//*[@id="event_table"]/div[5]/div/div')
    # products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Button to sort products by price
    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Prices of the products in search results
    products_prices = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')

