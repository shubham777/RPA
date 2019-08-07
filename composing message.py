from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'shubhamaggarwal1603@gmail.com'
passwordStr = 'Iamsexyanduknowit@'

browser = webdriver.Chrome('/home/user8/Desktop/selenium project/driver/chromedriver')
browser.get(('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin'))

# fill in username and hit the next button
username = browser.find_element_by_xpath('//*[@id="identifierId"]')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
nextButton.click()
time.sleep(3) 



# password = browser.find_element_by_id('Passwd')
# wait for transition then continue to fill items
# wait = WebDriverWait(browser,5)
##password = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'whsOnd zHQkBf')))
# pas= browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('Iniohdwn10hx@')

pas= browser.find_element_by_name('password').send_keys(passwordStr)

nextButton = browser.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
nextButton.click()

time.sleep(6) 

# clicking the compose button
compose= browser.find_element_by_xpath('//*[@id=":lw"]/div/div')
compose.click()


to_email_address='manavs@audertec.com'
subject='Hey!'
text='Automation done' 
time.sleep(3)
browser.find_element_by_name('to').send_keys(to_email_address)

browser.find_element_by_name('subjectbox').send_keys(subject)
time.sleep(3) 
browser.find_element_by_xpath('//*[@id=":sr"]').send_keys(text)
time.sleep(3)

send=browser.find_element_by_xpath("//div[text()='Send']").click()
