from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.implicitly_wait(10)
action_chains = ActionChains(driver)
driver.get('https://guldog.ru/vigul')
slider = driver.find_element(By.CSS_SELECTOR, 'span.irs-handle.single')
action_chains.drag_and_drop_by_offset(slider, -2, 21).perform()
#driver.execute_script("document.querySelector('span.irs-handle.single').style.left = '50%';")
price = driver.find_element(By.CSS_SELECTOR, 'div.b-calculator-new__summary-value.js-summary-value.js-duplicate-value-content')
print(price.text)
#driver.close()

#calc > div > div > div.b-calculator-new__container > div.b-calculator-new__ui-area > div > div.b-calculator-new__range-block > div.b-calculator-new__range-slider > div > div > span > div:nth-child(10)