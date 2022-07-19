# '''https://dumskaya.net/'''
# from selenium import webdriver
# import dumskaya_xpath
# import time
#
# url = "https://dumskaya.net/"
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get(url)
# time.sleep(3)
#
# email = 'aqwejvldeglmefbvlnlerv@gmail.com'
# nick = 'aqwejvldeglmefbvlnlerv'
# password = 'ASqwe874895!'
# time.sleep(3)
# main_button_enter = driver.find_element('xpath',dumskaya_xpath.main_button_enter)
# main_button_enter.click()
# time.sleep(3)
# main_button_registration = driver.find_element('xpath',dumskaya_xpath.main_button_registration)
# main_button_registration.click()
# time.sleep(3)
# reg_entry_email = driver.find_element('xpath',dumskaya_xpath.reg_entry_email)
# reg_entry_email.send_keys(email)
# time.sleep(3)
# reg_entry_nick = driver.find_element('xpath',dumskaya_xpath.reg_entry_nick)
# reg_entry_nick.send_keys(nick)
# time.sleep(3)
# reg_entry_password = driver.find_element('xpath',dumskaya_xpath.reg_entry_password)
# reg_entry_password.send_keys(password)
# time.sleep(3)
# reg_entry_rep_password = driver.find_element('xpath',dumskaya_xpath.reg_entry_rep_password)
# reg_entry_rep_password.send_keys(password)
# time.sleep(3)
# reg_radio_male = driver.find_element('xpath',dumskaya_xpath.reg_radio_male)
# reg_radio_male.click()
# time.sleep(3)
# reg_button_finish = driver.find_element('xpath',dumskaya_xpath.reg_button_finish)
# reg_button_finish.click()

'''https://dumskaya.net/'''
from selenium import webdriver
import dumskaya_xpath
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://dumskaya.net/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

#DATA
email = 'aqwejvldeglmefbvlnlerv1@gmail.com'
nick = 'aqwejvldeglmefbvlnlerv1'
password = 'ASqwe874895!'

WebDriverWait(driver,30).until(EC.presence_of_element_located(('xpath',dumskaya_xpath.main_button_enter)))
import time
main_button_enter = driver.find_element('xpath',dumskaya_xpath.main_button_enter)
main_button_enter.click()

WebDriverWait(driver,30).until(EC.presence_of_element_located(('xpath',dumskaya_xpath.main_button_registration)))
main_button_registration = driver.find_element('xpath',dumskaya_xpath.main_button_registration)
main_button_registration.click()

WebDriverWait(driver,30).until(EC.presence_of_element_located(('xpath',dumskaya_xpath.reg_entry_email)))

reg_entry_email = driver.find_element('xpath',dumskaya_xpath.reg_entry_email)
reg_entry_email.send_keys(email)

WebDriverWait(driver,30).until(EC.presence_of_element_located(('xpath',dumskaya_xpath.reg_entry_nick)))

reg_entry_nick = driver.find_element('xpath',dumskaya_xpath.reg_entry_nick)
reg_entry_nick.send_keys(nick)

WebDriverWait(driver,30).until(EC.presence_of_element_located(('xpath',dumskaya_xpath.reg_entry_password)))

reg_entry_password = driver.find_element('xpath',dumskaya_xpath.reg_entry_password)
reg_entry_password.send_keys(password)

WebDriverWait(driver,30).until(EC.presence_of_element_located(('xpath',dumskaya_xpath.reg_entry_rep_password)))

reg_entry_rep_password = driver.find_element('xpath',dumskaya_xpath.reg_entry_rep_password)
reg_entry_rep_password.send_keys(password)

WebDriverWait(driver,30).until(EC.presence_of_element_located(('xpath',dumskaya_xpath.reg_radio_male)))

reg_radio_male = driver.find_element('xpath',dumskaya_xpath.reg_radio_male)
reg_radio_male.click()

WebDriverWait(driver,30).until(EC.presence_of_element_located(('xpath',dumskaya_xpath.reg_button_finish)))

reg_button_finish = driver.find_element('xpath',dumskaya_xpath.reg_button_finish)
reg_button_finish.click()
