# Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a
# selenium-py-peldatar alkalmazást. A program töltse be a példatárból az
# http://localhost:9999 oldalt. Lokátorral keresd ki az összes linket az oldalról.
# Tárold a memóriában egy listában az összes linket. A list tartalmát írd ki egy fájlba.
# Minden link egy új sorba kerüljön. A kimenetre írd ki hány linket találtál.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get('http://localhost:9999')

    links = driver.find_elements_by_xpath('//a')

    number = 0

    with open("links.txt", "w") as link_collection:
        for link in links:
            link_collection.write(link.get_attribute("href") + "\n")
            number += 1

    print(f"{number} a talált linkek száma")

finally:
    driver.close()
