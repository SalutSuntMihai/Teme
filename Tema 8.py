from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome=webdriver.Chrome()
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/form')
sleep(3)
first_name = chrome.find_element(By.ID,"first-name")
first_name.send_keys('Merisor')
sleep(2)
last_name = chrome.find_element(By.ID,"last-name")
last_name.send_keys('Vrabie')
sleep(2)
job_title = chrome.find_element(By.ID,"job-title")
job_title.send_keys('ING')
sleep(2)
chrome.find_element(By.XPATH,'//input[@id="radio-button-1"]').click()
sleep(2)