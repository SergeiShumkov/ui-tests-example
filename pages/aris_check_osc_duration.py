import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements

from my_data import IP, login, password

class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or f'http://{login}:{password}@{IP}/'
            
        super().__init__(web_driver, url)

    # Main search field
    # search = WebElement(id='text1')
    

    # Search button  
    search_run_button = WebElement(id='start_osc')

    # Параметр длительность осциллограммы модуля RI   
    get_set_osc_duration = WebElement(xpath='//*[@id="tabs-1"]/table/tbody/tr[1]/td[2]/div/input')
    
    # Номер последней осциллограммы
    get_osc_number = WebElement(xpath='//*[@id="oscillograms_list"]/tbody/tr[1]/td[1]')

    # Длительность полученной осциллограммы модуля RI
    get_actual_osc_duration = WebElement(xpath='//*[@id="oscillograms_list"]/tbody/tr[1]/td[3]')


    # Параметры длительности осциллограммы модуля DM_CSWI
    get_set_osc_duration_1 = WebElement(xpath='//*[@id="tabs-1"]/table/tbody/tr[1]/td[2]/div/input')
    get_set_osc_duration_2 = WebElement(xpath='//*[@id="tabs-1"]/table/tbody/tr[2]/td[2]/div/input')

    # Длительность полученной осциллограммы модуля DM_CSWI
    # get_actual_osc_duration_6= WebElement(xpath='//*[@id="oscillograms_list"]/tbody/tr[1]/td[3]')


    # # Titles of the products in search results //*[@id="event_table"]/div[5]/div/div[18]/div[2]
    # products_titles = ManyWebElements(xpath ='//*[@id="event_table"]/div[5]/div/div')
    

    # # Button to sort products by price
    # sort_products_by_price = WebElement(css_selector='#reset_filter_btn')

    # # Prices of the products in search results
    # products_prices = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')

