from GuldogPages import GuldogWalkingCostHelper
from GuldogPages import GuldogConstants


def test_run(browser):
    guldog_main_page = GuldogWalkingCostHelper(browser)
    guldog_main_page.go_to_site()
    for i in range(4):
        guldog_main_page.click_on_the_dog_count(i)
        assert guldog_main_page.get_current_price() == GuldogConstants.GULDOG_PRICE_DOG_COUNT[i]
    guldog_main_page.click_on_the_switch_walker()
    assert guldog_main_page.get_current_walker_time() == GuldogConstants.GULDOG_FIRST_WALKER_TIME
    assert guldog_main_page.get_current_price() == GuldogConstants.GULDOG_FIRST_WALKER_PRICE
    guldog_main_page.click_on_the_switch_walker()
    assert guldog_main_page.get_current_price() == GuldogConstants.GULDOG_PRICE_DOG_COUNT[3]
    assert guldog_main_page.get_current_walker_time() == GuldogConstants.GULDOG_WALKER_TIME

