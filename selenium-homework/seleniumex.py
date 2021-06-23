# Készíts egy Python alkalmazást ami selenium-ot használ.
# Nyisson meg egy Chrome böngészöt és töltsön be egy tetszőleges weblapot az Internetről.
# Az oldalon probáld megtalálni a <div id="nemletezik"></div> mezőt.
# A lényeg, hogy hibát dogjon a driver.find_by_id függvény hívás.
# Feladatot, hogy kezed le ezt a hibát és írj ki valami emberileg olvasható üzenetet.
# Extra feladatként készíts egy saját függvényt, ami bármilyen find_by_id lokátor hívásnál
# lekezeli a nemlétező elem tipusú hibát. A megoldáshoz használj python try except struktúrát.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("http:\\idokep.hu")
    nemletezik = driver.find_by_id("nemletezik")
except:
    print("An exception occurred")
