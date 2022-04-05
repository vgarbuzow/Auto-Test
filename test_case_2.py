import time

from GuldogPages import GuldogWalkingCostHelper
from GuldogPages import GuldogConstants
from GuldogPages import GuldogLocators


def test_run(browser):
    guldog_main_page = GuldogWalkingCostHelper(browser)
    guldog_main_page.go_to_site()
    guldog_main_page.click_on_the_send_button()
    time.sleep(1)
    assert GuldogConstants.GULDOG_EMAIL_EMPTY_ERROR_TEXT in guldog_main_page.get_email_error_text()
    assert GuldogConstants.GULDOG_TELNUMBER_ERROR_TEXT in guldog_main_page.get_tel_number_error_text()
    guldog_main_page.enter_word_to_field('@!$%^:asdf', GuldogLocators.LOCATOR_GULDOG_TELNUMBER_FIELD)
    assert GuldogConstants.GULDOG_TELNUMBER_MASK in guldog_main_page.get_tel_number_text()
    guldog_main_page.enter_word_to_field('1234', GuldogLocators.LOCATOR_GULDOG_TELNUMBER_FIELD)
    guldog_main_page.click_on_the_send_button()
    assert GuldogConstants.GULDOG_TELNUMBER_MASK in guldog_main_page.get_tel_number_text()
    assert GuldogConstants.GULDOG_EMAIL_EMPTY_ERROR_TEXT in guldog_main_page.get_email_error_text()
    assert GuldogConstants.GULDOG_TELNUMBER_ERROR_TEXT in guldog_main_page.get_tel_number_error_text()
    guldog_main_page.enter_word_to_field('9091211122', GuldogLocators.LOCATOR_GULDOG_TELNUMBER_FIELD)
    guldog_main_page.click_on_the_send_button()
    assert GuldogConstants.GULDOG_EMAIL_EMPTY_ERROR_TEXT in guldog_main_page.get_email_error_text()
    assert guldog_main_page.get_tel_number_error_text() == ''
    guldog_main_page.enter_word_to_field('@123@', GuldogLocators.LOCATOR_GULDOG_EMAIL_FIELD)
    assert GuldogConstants.GULDOG_EMAIL_INCORRECT_ERROR_TEXT in guldog_main_page.get_email_error_text()
