import time

from my_data import IP,login, password
from pages.aris_check_osc_duration import MainPage


def test_check_osc_duration_RI(web_browser):
    """Проверка длительности осциллограммы RI (Ручной пуск)."""

# Ожидаемая длительность из параметров осциллографирования (module_id= номер в крейте)
    page_osc = MainPage(web_browser, url=f"http://{login}:{password}@{IP}/oscillograms_params_set.html?module_id=1")
    exceed_duration = page_osc.get_set_osc_duration.get_attribute("value")

# Номер последней осциллограммы до пуска
    page_list_of_osc = MainPage(web_browser, url=f'http://{IP}/oscillograms_list_of_group.html?group_id=CR00000001&group_name=Модуль%201')
    old_osc_number = page_list_of_osc.get_osc_number.get_text()

# Нажатие кнопки "Записать осциллограмму"
    page = MainPage(web_browser, url=f'http://{IP}/measurements_module_data.html?module_id=1')
    page.search_run_button.click(hold_seconds=1)

# Сохранение осциллограммы
    time.sleep(25)

# Проверка, что получена новая осциллограмма
    page_list_of_osc = MainPage(web_browser, url=f'http://{IP}/oscillograms_list_of_group.html?group_id=CR00000001&group_name=Модуль%201')
    new_osc_number = page_list_of_osc.get_osc_number.get_text()
    assert int(new_osc_number) == int(old_osc_number) + 1

# Длительность полученной осциллограммы
    osc_list = MainPage(web_browser, url=f"http://{IP}/oscillograms_list_of_group.html?group_id=CR00000001&group_name=%D0%9C%D0%BE%D0%B4%D1%83%D0%BB%D1%8C%201")
    actual_duration = osc_list.get_actual_osc_duration.get_text()[:-2]

# Проверка соответствия длительности осциллограммы
    assert int(exceed_duration) == int(actual_duration), f"Attention!!! {exceed_duration} != {actual_duration}"
    


def test_check_osc_duration_DM_CSWI(web_browser):
    """Проверка длительности осциллограммы DM_CSWI (Ручной пуск)."""

# Ожидаемая длительность из параметров осциллографирования (module_id= номер в крейте)
    page_osc = MainPage(web_browser, url=f"http://{login}:{password}@{IP}/oscillograms_params_set.html?module_id=6")
    exceed_duration = (float(page_osc.get_set_osc_duration_6_1.get_attribute("value")) + float(page_osc.get_set_osc_duration_6_2.get_attribute("value")))*1000

# Номер последней осциллограммы до пуска
    page_list_of_osc = MainPage(web_browser, url=f'http://{IP}/oscillograms_list_of_group.html?group_id=CR00000006&group_name=Модуль%206')
    old_osc_number = page_list_of_osc.get_osc_number.get_text()

# Нажатие кнопки "Записать осциллограмму"
    page = MainPage(web_browser, url=f"http://{IP}/measurements_module_data.html?module_id=6")
    page.search_run_button.click(hold_seconds=1)

# Сохранение осциллограммы
    time.sleep(35)

# Проверка, что получена новая осциллограмма
    page_list_of_osc = MainPage(web_browser, url=f'http://{IP}/oscillograms_list_of_group.html?group_id=CR00000006&group_name=Модуль%206')
    new_osc_number = page_list_of_osc.get_osc_number.get_text()
    assert int(new_osc_number) == int(old_osc_number) + 1

# Длительность полученной осциллограммы
    osc_list = MainPage(web_browser, url=f"http://{IP}/oscillograms_list_of_group.html?group_id=CR00000006&group_name=Модуль%206")
    actual_duration = osc_list.get_actual_osc_duration.get_text()[:-2]

# Проверка соответствия длительности осциллограммы(Может быть или равна, или на 125 мс больше)
    assert int(exceed_duration) == int(actual_duration) - 125 or int(exceed_duration) == int(actual_duration)
    

