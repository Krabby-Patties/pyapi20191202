#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driverpath = r'C:\Users\Pinad\Downloads\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driverpath)
driver.get("https://dominos.com/en/")

time.sleep(8)

## order carryout
click_delivery = driver.find_element_by_xpath('//*[@id="homeWrapper"]/main/section[1]/div/div[2]/a[2]')
click_delivery.click()

## entering zip code
time.sleep(3)
driver.find_element_by_xpath('//*[@id="Postal_Code_Sep"]').click()
# fill in the field with our zipcode and press RETURN
driver.find_element_by_xpath('//*[@id="Postal_Code_Sep"]').send_keys('98499' + Keys.RETURN)
time.sleep(3)

## select store for carryout
time.sleep(3)
driver.find_element_by_xpath('//*[@id="locationsResultsPage"]/div/div[2]/div[1]/div[2]/div/div[2]/div/a').click()

## choose and 2 or more for $5.99
time.sleep(3)
driver.find_element_by_xpath('//*[@id="entreesPage"]/div[2]/div[2]/div/div/a/div/div[3]/button').click()

## add items to this coupon menu <adding pizzas>
time.sleep(2)
driver.find_element_by_xpath('//*[@id="genericOverlay"]/section/div/div[5]/div[2]/div[1]/h2').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="genericOverlay"]/section/div/div[5]/div[2]/div[2]/div/div[1]/a/div').click()
## cheese and sauce selections
time.sleep(1)
driver.find_element_by_xpath('//*[@id="pizzaBuilderPage"]/div[3]/div[5]/div[1]/div[2]/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="pizzaBuilderPage"]/div[3]/div[5]/div[1]/div[2]/button').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="stepUpsell"]/div/button[1]').click()
## adding jalepenos
time.sleep(1)
driver.find_element_by_xpath('//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[2]/label/input').click()
driver.find_element_by_xpath('//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[2]/div[2]/label/input').click()
## quantity select 2
driver.find_element_by_xpath('//*[@id="pizzaSummaryInColumn"]/div[1]/div[2]/p/select/').click()
# add to order
driver.find_element_by_xpath('//*[@id="pizzaSummaryInColumn"]/div[1]/div[2]/div[2]/button').click()
driver.find_element_by_xpath('//*[@id="pizzaSummaryInColumn"]/div[1]/div[2]/div[2]/button').click()

