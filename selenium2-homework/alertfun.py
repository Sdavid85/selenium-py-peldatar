# Készíts egy Python alkalmazást ami selenium-ot használ. Indítsd el lokálisan a
# selenium-py-peldatar alkalmazást. A program töltse be a példatárból az
# http://localhost:9999/alert_playground.html oldalt.
# A tanultak alapján az összes alert funkcióra írj selenium kódot.
# A prompt-nál teszteld le a be, hogy a beírt érték megjelenik-e egy
# paragraf tagben, miután eltűnt az alert.

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

try:
    driver.get("http://localhost:9999/alert_playground.html")

    alert_button = driver.find_element_by_name("alert")
    alert_button.click()
    text1 = "I am alert"
    alert1 = driver.switch_to.alert
    assert (alert1.text == text1)
    print(alert1.text)
    time.sleep(1)
    alert1.accept()

    conf_button = driver.find_element_by_name("confirmation")
    conf_button.click()
    text2 = "I am confirm"
    alert2 = driver.switch_to.alert
    assert (alert2.text == text2)
    print(alert2.text)
    time.sleep(1)
    alert2.accept()

    prompt_button = driver.find_element_by_name("prompt")
    prompt_button.click()
    text3 = "I am prompt"
    alert3 = driver.switch_to.alert
    assert (alert3.text == text3)
    print(alert3.text)
    time.sleep(1)
    alert3.accept()

    dc_button = driver.find_element_by_id("double-click")
    ac = ActionChains(driver)
    ac.double_click(dc_button).perform()
    text4 = "You double clicked me!!!, You got to be kidding me"
    alert4 = driver.switch_to.alert
    assert (alert4.text == text4)
    print(alert4.text)
    time.sleep(1)
    alert4.accept()

finally:
    driver.close()
