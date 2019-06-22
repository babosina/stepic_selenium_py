import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestMainPage:

    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_guest_can_login1(self, browser):
        assert True

    @pytest.mark.regression
    def test_guest_can_add_book_from_catalog_to_basket2(self, browser):
        assert True


class TestBasket:

    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_guest_can_go_to_payment_page3(self, browser):
        assert True

    @pytest.mark.smoke
    def test_guest_can_see_total_price4(self, browser):
        assert True


@pytest.mark.skip
class TestBookPage:

    @pytest.mark.smoke
    def test_guest_can_add_book_to_basket5(self, browser):
        assert True

    @pytest.mark.regression
    def test_guest_can_see_book_price6(self, browser):
        assert True


@pytest.mark.beta_users
@pytest.mark.smoke
def test_guest_can_open_gadget_catalogue7(browser):
    assert True
