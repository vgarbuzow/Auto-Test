from BaseApp import BasePage
from selenium.webdriver.common.by import By


class GuldogLocators:
    LOCATOR_GULDOG_WALKING_PRICE = (By.CSS_SELECTOR, "div.b-calculator-new__summary-value.js-summary-value.js"
                                                     "-duplicate-value-content")
    LOCATOR_GULDOG_SWITCH_WALKER = (By.CLASS_NAME, "b-input-switcher__switcher-walker")
    LOCATOR_GULDOG_EMAIL_FIELD = (By.NAME, "walking_mail")
    LOCATOR_GULDOG_TELNUMBER_FIELD = (By.NAME, "walking_phone")
    LOCATOR_GULDOG_SEND_BUTTON = (By.CSS_SELECTOR, "#walking-calculator-preloader")
    LOCATOR_GULDOG_DOG_COUNT = [(By.XPATH, '//*[@id="calc"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/label[1]/span'),
                                (By.XPATH, '//*[@id="calc"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/label[2]/span'),
                                (By.XPATH, '//*[@id="calc"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/label[3]/span'),
                                (By.XPATH, '//*[@id="calc"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/div/label[4]/span')]
    LOCATOR_GULDOG_TIME_WALKER = (By.CLASS_NAME, "b-calculator-new__text")


class GuldogConstants:
    GULDOG_PRICE_DOG_COUNT = ['645', '895', '1 145', '1 395']
    GULDOG_FIRST_WALKER_TIME = 'Длительность прогулки - 25 минут'
    GULDOG_WALKER_TIME = 'Длительность прогулки - 1 час'
    GULDOG_FIRST_WALKER_PRICE = '190'


class GuldogWalkingCostHelper(BasePage):

    def enter_word_to_field(self, word, field):
        search_field = self.find_element(field)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def get_current_price(self):
        return self.find_element(GuldogLocators.LOCATOR_GULDOG_WALKING_PRICE, time=2).text

    def click_on_the_dog_count(self, dog_count):
        return self.find_element(GuldogLocators.LOCATOR_GULDOG_DOG_COUNT[dog_count], time=4).click()

    def click_on_the_send_button(self):
        return self.find_element(GuldogLocators.LOCATOR_GULDOG_SEND_BUTTON, time=2).click()

    def click_on_the_switch_walker(self):
        return self.find_element(GuldogLocators.LOCATOR_GULDOG_SWITCH_WALKER, time=2).click()

    def get_current_walker_time(self):
        return self.find_element(GuldogLocators.LOCATOR_GULDOG_TIME_WALKER, time=2).text

