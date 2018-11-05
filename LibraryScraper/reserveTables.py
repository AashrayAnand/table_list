from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from constants import name, time_range
import time
from bs4 import BeautifulSoup

from selenium.webdriver import FirefoxOptions
import re
from datetime import datetime
import json

opts = FirefoxOptions()
# opts.add_argument("--headless")

# use selenium web driver to get library calendar page
def getURL(browser):
    browser.get("http://uw.libcal.com/spaces/bookings?lid=1454&gid=0")

def main():
    try:
        browser = webdriver.Firefox(firefox_options=opts)
        getURL(browser)
        
        # get booking name input in form, and replace with name value
        booking_name = browser.find_element_by_name('q')
        booking_name.send_keys(name)

        # get booking time range dropdown, and set to selected time range
        booking_time_range = Select(browser.find_element_by_name('d'))
        booking_time_range.select_by_value(time_range)
        # after filling form parameters, search for listings
        search_button = browser.find_element_by_id('s-lc-eq-n-searchbtn')
        search_button.send_keys(Keys.ENTER)
        time.sleep(10)
        getTimesFromPage(browser)
    except Exception as e:
        print(e)
        browser.quit()
    browser.quit()

def getTimesFromPage(browser):
    items = []
    #while len(browser.find_elements_by_css_selector('#s-lc-space-nick-tb_next a')) > 0:
    for i in range(len(browser.find_elements_by_class_name('paginate_button')) - 2):
        time.sleep(5)
        soup = BeautifulSoup(browser.page_source, 'html.parser')
        # get all items in table with even class
        #items = items + soup.select('tr.even') + soup.select('tr.odd')
        items = items + soup.select('#s-lc-space-nick-tb tbody tr')
        print(len(items))
        browser.find_element_by_css_selector('#s-lc-space-nick-tb_next a').click()

    convertItemsToJSON(items)
def convertItemsToJSON(items):
    json_items = []
    for iterator, item in enumerate(items):
        print(iterator)
        json_item = {}
        print(item.getText())
        
if __name__ == "__main__":
    main()

