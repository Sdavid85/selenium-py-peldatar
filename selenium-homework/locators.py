# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/kitchensink.html oldalt.
# Gyakorlás képpen keress ki elemekt a képernyőről az alábbi kritériumoknak megfelelően:
# ID alapján
# NAME alapján
# XPath kifejezéssel Minden megtalált elemnek irassd ki a text értékét, vagy egy attribútum értékét.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("http://localhost:9999/kitchensink.html")

try:
    driver.find_element_by_name("courses")
    driver.find_element_by_id("hondaradio")
    driver.find_element_by_xpath('//*[@id="openwindow"]')

    print('Sikeresen lefutott')

except:
    print('Nincs találat')
finally:
    driver.close()
