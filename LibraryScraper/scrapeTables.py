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
import datetime
import json

opts = FirefoxOptions()
# opts.add_argument("--headless")

month_dictionary = {"January": 1,
                    "February": 2,
                    "March": 3,
                    "April": 4,
                    "May": 5,
                    "June": 6,
                    "July": 7,
                    "August": 8,
                    "September": 9,
                    "October": 10,
                    "November": 11,
                    "December": 12
                    }
model_name = "table_list.table_items"
location = "ode"
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
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # get all items in table with even class
    items = soup.select('tr.even')
    # get all items in table with odd class
    odd_items = soup.select('tr.odd')
    items = items + odd_items
    convertItemsToJSON(items, soup)
def convertItemsToJSON(items, soup):
    json_items = []
    for iterator, item in enumerate(items):
        print(iterator)
        json_item = {}
        json_item['pk'] = iterator
        json_item['model'] = model_name
        field_item = {}
        field_item["location"] = location
        clean_text = "".join(item.getText().split())
        # search for times (start and end) in clean text
        time_range = re.search("[0-9]+:[0-9apm]+-[0-9]+:[0-9apm]+", clean_text)
        # split start and end times
        times = time_range.group(0).split("-")
        # print start time and end time
        print("{}     {}".format(times[0], times[1]))
        # get [day of week,month day,year] pattern, split by commas, then split month and day
        date = re.search("(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)" +
        ",(January|February|March|April|May|June|July|August|September|October|November|December)" + 
        "[0-9]+,[0-9]+", clean_text).group(0).split(",")
        # get month from date
        month = re.search("[a-zA-Z]+", date[1]).group(0)
        # get day from date
        day = re.search("[0-9]+", date[1]).group(0)
        print("{}\n    {}\n    {}\n    {}\n".format(date[0], month_dictionary.get(month), day, date[2]))
        clean_times = times[0][0:len(times[0]) - 2].split(":")
        print("{}    {}".format(clean_times[0], clean_times[1]))
        # create date time object
        date_time = datetime.datetime(year=int(date[2]), month=month_dictionary.get(month), day=int(day), hour=int(clean_times[0]), minute=int(clean_times[1]))
        field_item["date"] = str(date_time)
        field_item["day_of_week"] = date[0]
        json_item["fields"] = field_item
        print(date_time)
        print("-----------")
        json_items.append(json_item)
        print(json_item)
    with open('../table_list/fixtures/items.json', 'w') as outfile:
        outfile.write(str(json.dump(json_items, outfile, indent=4)))
######## JSON format ########
#[
    #{
        #"model": "model name"
        #"pk": i (iterator value: 1,2,3,4....)
        #"fields": {
            # "location": ode (will be the value scraped later),
            # "date": date_time,
            # "day_of_week": date[0]
        # }
    # }
# ]
if __name__ == "__main__":
    main()

