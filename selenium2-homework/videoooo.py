# A program töltse be a példatárból az http://localhost:9999/videos.html oldalt.
# Az oldalon találhotó összes beágyazott videót indítsa el és állítsa meg.

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("http://localhost:9999/videos.html")
    html5videos = driver.find_element_by_id("html5video")
    html5videos.click()
    html5videos.send_keys(Keys.SPACE)
    time.sleep(5)
    html5videos.send_keys(Keys.SPACE)

    bunny_play_button = driver.find_element_by_xpath("/html/body/div/button[1]")
    bunny_play_button.click()
    time.sleep(5)
    bunny_play_button.click()

    muppet = driver.find_element_by_xpath("//iframe[@src='https://www.youtube.com/embed/tgbNymZ7vqY']")
    driver.switch_to.frame(muppet)
    driver.find_element_by_xpath("//button[@aria-label='Lejátszás']").click()
    time.sleep(5)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='movie_player']"))).send_keys(Keys.SPACE)

finally:
    driver.close()
