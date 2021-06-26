# Készíts egy Python alkalmazást ami selenium-ot használ.
# Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
# A program töltse be a példatárból az http://localhost:9999/trickyelements.html oldalt.
# Használj id lokátort és keressd ki az elemenekt egyesével.
# A legelső olyan elemre ami button típusú kattints rá és ellenőrizd,
# hogy a helyes szöveg jelenik-e meg az elemek listája alatt.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver.get("http://localhost:9999/trickyelements.html")