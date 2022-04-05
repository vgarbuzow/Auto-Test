from selenium.webdriver import Keys

from BaseApp import BasePage
from selenium.webdriver.common.by import By


class GuldogLocators:
    LOCATOR_GULDOG_WALKING_PRICE = (By.CSS_SELECTOR, "div.b-calculator-new__summary-value.js-summary-value.js"
                                                     "-duplicate-value-content")
    LOCATOR_GULDOG_SWITCH_WALKER = (By.CLASS_NAME, "b-input-switcher__switcher-walker")
    LOCATOR_GULDOG_EMAIL_FIELD = (By.NAME, "walking_mail")
    LOCATOR_GULDOG_TELNUMBER_FIELD = (By.NAME, "walking_phone")
    LOCATOR_GULDOG_SEND_BUTTON = (By.CSS_SELECTOR, "#walking-calculator-preloader")
    LOCATOR_GULDOG_DOG_COUNT = [(By.XPATH, '//*[@id="calc"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div['
                                           '2]/div/div/label[1]/span'),
                                (By.XPATH, '//*[@id="calc"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div['
                                           '2]/div/div/label[2]/span'),
                                (By.XPATH, '//*[@id="calc"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div['
                                           '2]/div/div/label[3]/span'),
                                (By.XPATH, '//*[@id="calc"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div['
                                           '2]/div/div/label[4]/span')]
    LOCATOR_GULDOG_TIME_WALKER = (By.CLASS_NAME, "b-calculator-new__text")
    LOCATOR_GULDOG_TELNUMBER_ERROR = (By.XPATH, '//*[@id="calc"]/div/form/div/div[1]/div[1]/div[1]/div/div/div/span')
    LOCATOR_GULDOG_EMAIL_ERROR = (By.XPATH, '//*[@id="calc"]/div/form/div/div[1]/div[1]/div[2]/div/div/div/div/span')
    LOCATOR_GULDOG_BONUS_PROGRAM = (By.XPATH, '//*[@id="calc"]/div/div/div[2]/div[3]/a')
    LOCATOR_GULDOG_USER_AGREEMENT = (By.XPATH, '//*[@id="calc"]/div/form/div/div[1]/div[2]/div/div/label/span[2]/a')


class GuldogConstants:
    GULDOG_PRICE_DOG_COUNT = ['645', '895', '1 145', '1 395']
    GULDOG_FIRST_WALKER_TIME = 'Длительность прогулки - 25 минут'
    GULDOG_WALKER_TIME = 'Длительность прогулки - 1 час'
    GULDOG_FIRST_WALKER_PRICE = '190'
    GULDOG_TELNUMBER_ERROR_TEXT = 'Укажите телефон'
    GULDOG_EMAIL_EMPTY_ERROR_TEXT = 'Укажите e-mail для отчета'
    GULDOG_EMAIL_INCORRECT_ERROR_TEXT = 'Укажите корректный e-mail адрес'
    GULDOG_TELNUMBER_MASK = '+7(___) ___-__-__'

class GuldogWalkingCostHelper(BasePage):

    def enter_word_to_field(self, word, field):
        field = self.find_element(field)
        field.click()
        field.send_keys(Keys.HOME)
        field.send_keys(word)
        return field

    def get_current_price(self):
        return self.find_element(GuldogLocators.LOCATOR_GULDOG_WALKING_PRICE, time=5).text

    def click_on_the_dog_count(self, dog_count):
        return self.find_element(GuldogLocators.LOCATOR_GULDOG_DOG_COUNT[dog_count], time=5).click()

    def click_on_the_send_button(self):
        return self.find_element(GuldogLocators.LOCATOR_GULDOG_SEND_BUTTON, time=5).click()

    def click_on_the_switch_walker(self):
        return self.find_element(GuldogLocators.LOCATOR_GULDOG_SWITCH_WALKER, time=5).click()

    def get_current_walker_time(self):
        return self.find_element(GuldogLocators.LOCATOR_GULDOG_TIME_WALKER, time=5).text

    def get_email_error_text(self):
        return self.find_element(GuldogLocators.LOCATOR_GULDOG_EMAIL_ERROR, time=5).text

    def get_tel_number_error_text(self):
        return self.find_element(GuldogLocators.LOCATOR_GULDOG_TELNUMBER_ERROR, time=5).text

    def get_tel_number_text(self):
        return self.find_element(GuldogLocators.LOCATOR_GULDOG_TELNUMBER_FIELD, time=5).get_attribute('value')

    def click_on_link_bonus_program(self):
        url = self.find_element(GuldogLocators.LOCATOR_GULDOG_BONUS_PROGRAM, time=5).get_attribute('href')
        return self.go_to_url(url)

    def click_on_link_user_agreement(self):
        url = self.find_element(GuldogLocators.LOCATOR_GULDOG_USER_AGREEMENT, time=5).get_attribute('href')
        return self.go_to_url(url)

