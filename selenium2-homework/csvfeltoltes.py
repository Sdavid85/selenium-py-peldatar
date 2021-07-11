# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/another_form.html oldalt.
# A program segítségével olvassd be a csv tartalmat. A feladatod, hogy az oldalon
# található formanyomtatvány segítségével feltöltsd a táblázatot.
# Használd a Python CSV könyvtárát. A feltöltött táblázatot ellenőrizheted ha a
# probramod letölti a táblázat alatti gomb segítségével az aktuális tartalmat.
# Hasonlítsd össze python kódból a kapott file-t, hogy identikus-e az eredetivel.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

import csv

try:
    driver.get("http://localhost:9999/another_form.html")


    def finder(id):
        element = driver.find_element_by_id(id)
        element.clear()
        return element


    submit_button = driver.find_element_by_id("submit")

    with open('table_in.csv', encoding='UTF-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            print(row)
            finder("fullname").send_keys(row[0])
            finder("email").send_keys(row[1])
            finder("dob").send_keys(row[2])
            finder("phone").send_keys(row[3])
            submit_button.click()

    result_rows = driver.find_elements_by_xpath("//table[@id='detailsTable']/tbody/tr")

    for row in result_rows:
        cells = row.find_elements_by_tag_name("td")
        print(cells[0].text, cells[1].text, cells[2].text, cells[3].text)

finally:
    driver.close()
