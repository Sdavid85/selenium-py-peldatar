# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/todo.html oldalt.
# A feladatod, hogy kigyűjtsd az összes jelenleg aktív Todo bejegyzést.
# Ha lehet akkor ezt minnél kevesebb selenium lokátorral old meg.
# (Tökéletes megoldáshoz csak egy darab find_by hívásra van szükség).

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get('http://localhost:9999/todo.html')

active_elements = driver.find_element_by_css_selector('span.done-false')

for x in active_elements:
    print(x.text)

driver.close()
