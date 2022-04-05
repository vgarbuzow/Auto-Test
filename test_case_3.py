from GuldogPages import GuldogWalkingCostHelper


def test_run(browser):
    guldog_main_page = GuldogWalkingCostHelper(browser)
    guldog_main_page.go_to_site()
    guldog_main_page.click_on_link_bonus_program()
    assert guldog_main_page.get_current_url() == 'https://guldog.ru/bonus_program'
    guldog_main_page.go_to_site()
    guldog_main_page.click_on_link_user_agreement()
    assert guldog_main_page.get_current_url() == 'https://guldog.ru/termsofuse'
