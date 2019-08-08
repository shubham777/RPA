from selenium import webdriver
import bs4
import pandas as pd
import re
import time
import requests

from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('/home/user8/Desktop/chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

Sign_in_button = driver.find_element_by_class_name('nav__button-secondary')

# .click() to mimic button click
Sign_in_button.click()

# locate email form by_class_name
username = driver.find_element_by_id('username')

# send_keys() to simulate key strokes
username.send_keys('ABSHXBASBXJSANXJKSANXJS')

# locate password form by_class_name
password = driver.find_element_by_id('password')

# send_keys() to simulate key strokes
password.send_keys('Linke11dad23e')

# locate submit button by_class_name
sign_in_button = driver.find_element_by_class_name('login__form_action_container')

# .click() to mimic button click
sign_in_button.click()
