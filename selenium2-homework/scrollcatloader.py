# A program töltse be a példatárból az http://localhost:9999/scrolltoload.html oldalt.
# Mentsd le az első 20 macskás képet az oldalról. A fájlokat egy külön cats könyvtárba mentsd le.
# A fájlneve legyen a következő {sorszam}_{cat_id} ahol a sorszám alatt azt értjük,
# hogy hanyadiknak lett megjelenítve és cat_id meg az azonosító amit szolgáltató ad.
# A {} jelek ne legyenek benne a fájlnévben. (ez a feladat majdnem ugyan az, mint az előző feladat,
# csakhogy nincs load more gomb.)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://localhost:9999/scrolltoload.html")
time.sleep(3)
from selenium.webdriver.common.keys import Keys
html = driver.find_element_by_tag_name("html")
html.send_keys(Keys.END)
time.sleep(3)
cats = driver.find_elements_by_tag_name("img")
print(cats)
for index, cat in enumerate(cats[0:21]):
    url_str = cat.get_attribute("src")
    cat_id = cat.find_element_by_xpath("../p").text.replace("Cat id: ", "")
    cat_file_name = f"cats/{index}_{cat_id}"
    r = requests.get(url_str)
    if r.status_code == 200:
        with open(cat_file_name, 'wb') as f:
            f.write(r.content)
print()
print(len(cats))

driver.close()
