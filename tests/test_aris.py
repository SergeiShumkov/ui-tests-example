import pytest
from pages.aris import MainPage

def test_check_main_search(web_browser):
    """ Make sure main search works fine. """

    page = MainPage(web_browser)

    page.search = '10.2.0.21'
    page.search_run_button.click()

    # Verify that user can see the list of messages:
    # print(page.products_titles.get_text()[2])
    assert page.products_titles.count() == 49

    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = f'Wrong product in search "{title}"'
        assert 'admin' in title.lower(), msg


def q_test_check_wrong_input_in_search(web_browser):
    """ Make sure that wrong keyboard layout input works fine. """

    page = MainPage(web_browser)

    # Try to enter "смартфон" with English keyboard:
    page.search = 'cvfhnajy'
    page.search_run_button.click()

    # Verify that user can see the list of products:
    assert page.products_titles.count() == 48

    # Make sure user found the relevant products
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'смартфон' in title.lower(), msg


@pytest.mark.xfail(reason="Filter by price doesn't work")
def q_test_check_sort_by_price(web_browser):
    """ Make sure that sort by price works fine.
        Note: this test case will fail because there is a bug in
              sorting products by price.
    """

    page = MainPage(web_browser)

    page.search = 'чайник'
    page.search_run_button.click()

    # Scroll to element before click on it to make sure
    # user will see this element in real browser
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    # Get prices of the products in Search results
    all_prices = page.products_prices.get_text()

    # Convert all prices from strings to numbers
    all_prices = [float(p.replace(' ', '')) for p in all_prices]

    print(all_prices)
    print(sorted(all_prices))

    # Make sure products are sorted by price correctly:
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"