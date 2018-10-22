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
        items = items + soup.select('tr.even') + soup.select('tr.odd')
        browser.find_element_by_css_selector('#s-lc-space-nick-tb_next a').click()

    convertItemsToJSON(items)
def convertItemsToJSON(items):
    json_items = []
    for iterator, item in enumerate(items):
        print(iterator)
        json_item = {}
        print(item.getText())
        ###### add JSON values to item ######
        json_item['pk'] = iterator
        json_item['model'] = model_name
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
        # split start hour and end minute into array
        clean_start_times = times[0][0:len(times[0]) - 2].split(":")
        # split end hour and end minute into array
        clean_end_times = times[1][0:len(times[1]) - 2].split(":")
        # get time period (AM/PM) for start time
        start_time_period = (times[0][len(times[0])  - 2:len(times[0])]).upper()
        # get time period (AM/PM) for end time
        end_time_period = (times[1][len(times[1])  - 2:len(times[1])]).upper()
        print(start_time_period)
        print("{}    {}".format(clean_start_times[0], clean_start_times[1]))
        # create date time object
        start_date_string = "{}-{}-{} {}:{} {}".format(date[2], month_dictionary.get(month), day, clean_start_times[0], clean_start_times[1], start_time_period)
        end_date_string = "{}-{}-{} {}:{} {}".format(date[2], month_dictionary.get(month), day, clean_end_times[0], clean_end_times[1], end_time_period)
        format = '%Y-%m-%d %I:%M %p'
        # create datetime objects for start and end time
        start_date_time = datetime.strptime(start_date_string, format)
        end_date_time = datetime.strptime(end_date_string, format)
        # search for room name in string, then extract room name from result of regex
        room_search = re.search("[0-9][0-9][0-9][0-9](.)+Info", item.getText())
        room_name = room_search.group(0)[4:len(room_search.group(0))-4]
        # create fields dictionary, add location, start and end date times to fields dictionary
        field_item = {}
        field_item["location"] = room_name
        field_item["start_date"] = str(start_date_time)
        field_item["end_date"] = str(end_date_time)
        # add day of week to fields dictionary
        field_item["day_of_week"] = date[0]
        # add fields dictionary to JSON item
        json_item["fields"] = field_item
        print("END DATE TIME IS...")
        print(end_date_time)
        print("-----------")
        json_items.append(json_item)
        print(json_item)
    with open('../table_list/fixtures/items.json', 'w') as outfile:
        outfile.write(json.dump(json_items, outfile, indent=4))
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

