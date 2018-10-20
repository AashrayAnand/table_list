from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from drive_constants import username, pass_
import time
from bs4 import BeautifulSoup

# login to drive account
def login(browser):
    browser.find_element_by_class_name('go-to-drive').click()
    time.sleep(5)
    username = browser.find_element_by_name('identifier')
    username.send_keys('uwpaphi@uw.edu')
    username.send_keys(Keys.ENTER)
    time.sleep(5)
    browser.find_element_by_id('weblogin_netid').send_keys('uwpaphi')
    password = browser.find_element_by_id('weblogin_password')
    password.send_keys('xitillwedie2004')
    password.send_keys(Keys.ENTER)
    time.sleep(10)

# search for an enter test bank directory
def enter_directory(browser):
    browser.get('https://drive.google.com/drive/folders/0B8ivQejRBN5YYmFGNXhUQ1dEeEE')
    time.sleep(5)
    

def getURL(browser):
    browser.get("https://drive.google.com")
    time.sleep(5)

def main():
    browser = webdriver.Firefox()
    getURL(browser)
    try:
        login(browser)
        enter_directory(browser)
    except Exception as e:
        print(e)
    browser.quit()
main()