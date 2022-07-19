'''https://www.selenium.dev/'''

from selenium import webdriver
import dumskaya_xpath
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.selenium.dev/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
d = '//a[@id="navbarDropdown"][contains(text(),"About")]'

WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', d)))
# about = driver.find_element('xpath', d)
# about.click()
about = driver.find_element('id', 'navbarDropdown')
about.click()
e = '//a[@href="/ecosystem"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', e)))
about = driver.find_element('xpath', e)
about.click()

'''https://bank.gov.ua/ua/markets/exchangerates'''
'//td[contains(text(),"MDL")]/parent::tr/td[5]'