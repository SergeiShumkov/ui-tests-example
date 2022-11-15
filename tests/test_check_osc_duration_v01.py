import time

from my_data import IP,login, password, NUMBER_RI, NUMBER_DM_CSWI, DELTA_DURATION
from pages.aris_check_osc_duration import MainPage



def test_check_osc_duration_RI(web_browser):
    """Проверка длительности осциллограммы RI (Ручной пуск)."""
    
    temp = NUMBER_RI

# Ожидаемая длительность из параметров осциллографирования (module_id= номер в крейте)
    page_osc = MainPage(web_browser, url=f"http://{login}:{password}@{IP}/oscillograms_params_set.html?module_id={temp}")
    exceed_duration = page_osc.get_set_osc_duration.get_attribute("value")

# Номер последней осциллограммы до пуска
    page_list_of_osc = MainPage(web_browser, url=f'http://{IP}/oscillograms_list_of_group.html?group_id=CR0000000{temp}&group_name=Модуль%20{temp}')
    old_osc_number = page_list_of_osc.get_osc_number.get_text()

# Нажатие кнопки "Записать осциллограмму"
    page = MainPage(web_browser, url=f'http://{IP}/measurements_module_data.html?module_id={temp}')
    page.search_run_button.click(hold_seconds=1)

# Сохранение осциллограммы
    time.sleep(30)

# Проверка, что получена новая осциллограмма
    page_list_of_osc = MainPage(web_browser, url=f'http://{IP}/oscillograms_list_of_group.html?group_id=CR0000000{temp}&group_name=Модуль%20{temp}')
    new_osc_number = page_list_of_osc.get_osc_number.get_text()
    assert int(new_osc_number) == int(old_osc_number) + 1

# Длительность полученной осциллограммы
    actual_duration = page_list_of_osc.get_actual_osc_duration.get_text()[:-2]

# Проверка соответствия длительности осциллограммы
    assert int(exceed_duration) == int(actual_duration), f"Attention!!! {exceed_duration} != {actual_duration}"
    


def test_check_osc_duration_DM_CSWI(web_browser):
    """Проверка длительности осциллограммы DM_CSWI (Ручной пуск)."""

    temp = NUMBER_DM_CSWI

# Ожидаемая длительность из параметров осциллографирования (module_id= номер в крейте)
    page_osc = MainPage(web_browser, url=f"http://{login}:{password}@{IP}/oscillograms_params_set.html?module_id={temp}")
    exceed_duration = (float(page_osc.get_set_osc_duration_1.get_attribute("value")) + float(page_osc.get_set_osc_duration_2.get_attribute("value")))*1000

# Номер последней осциллограммы до пуска
    page_list_of_osc = MainPage(web_browser, url=f'http://{IP}/oscillograms_list_of_group.html?group_id=CR0000000{temp}&group_name=Модуль%20{temp}')
    old_osc_number = page_list_of_osc.get_osc_number.get_text()

# Нажатие кнопки "Записать осциллограмму"
    page = MainPage(web_browser, url=f'http://{IP}/measurements_module_data.html?module_id={temp}')
    page.search_run_button.click(hold_seconds=1)

# Сохранение осциллограммы
    time.sleep(30)

# Проверка, что получена новая осциллограмма
    page_list_of_osc = MainPage(web_browser, url=f'http://{IP}/oscillograms_list_of_group.html?group_id=CR0000000{temp}&group_name=Модуль%20{temp}')
    new_osc_number = page_list_of_osc.get_osc_number.get_text()
    assert int(new_osc_number) == int(old_osc_number) + 1

# Длительность полученной осциллограммы
    actual_duration = page_list_of_osc.get_actual_osc_duration.get_text()[:-2]

# Проверка соответствия длительности осциллограммы(Может быть или равна, или на DELTA_DURATION мс больше)
    assert int(exceed_duration) == int(actual_duration) - DELTA_DURATION or int(exceed_duration) == int(actual_duration)
    
