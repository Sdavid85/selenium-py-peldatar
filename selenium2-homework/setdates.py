# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/forms.html oldalt.
# Koncentrálj a dátum mezőkre.
# A célod, hogy a következő képen látható dátum és idő értékekete pontosan beállítsd
# az alkalmazásba selenium segítségével: assets/dates.png

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("http://localhost:9999/forms.html")

date1 = datetime(2021, 6, 5)
set1 = date1.strftime('00%Y-%m-%d')
date_field = driver.find_element_by_id('example-input-date')
print(set1)
date_field.send_keys(set1)

date2 = datetime(2012, 5, 5, 5, 5, 5, 555)
set2 = date2.strftime('%Y-%m-%d %H:%M:%S:%f')
datetime_field = driver.find_element_by_id('example-input-date-time')
print(set2)
datetime_field.send_keys(set2)

date3 = datetime(2000, 12, 5, 12, 1)
set3 = date3.strftime('00%Y-%m-%dT%I:%M %p\t')
date_time_local_field = driver.find_element_by_id('example-input-date-time-local')
print(set3)
date_time_local_field.send_keys(set3)

date4 = datetime(1995, 12, 1)
set4 = date4.strftime('%Y\t%m')
month_field = driver.find_element_by_id('example-input-month')
print(set4)
month_field.send_keys(set4)

date5 = datetime(2015, 12, 28)
set5 = date5.strftime('%W\n%Y\t')
week_field = driver.find_element_by_id('example-input-week')
print(set5)
week_field.send_keys(set5)

date6 = datetime(2021, 7, 8, 12, 25)
set6 = date6.strftime('%H:%M')
time_field = driver.find_element_by_id('example-input-time')
print(set6)
time_field.send_keys(set6)

driver.close()
