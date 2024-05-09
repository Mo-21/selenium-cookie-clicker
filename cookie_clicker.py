from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by="id", value="cookie")

timeout = time.time() + 5

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cookie.click()

    # Re-locate the elements inside the loop to avoid StaleElementReferenceException
    # upgrades
    if time.time() > timeout:
        cursor = driver.find_element(by="id", value="buyCursor")
        grandma = driver.find_element(by="id", value="buyGrandma")
        factory = driver.find_element(by="id", value="buyFactory")
        mine = driver.find_element(by="id", value="buyMine")
        shipment = driver.find_element(by="id", value="buyShipment")
        alchemy_lab = driver.find_element(by="id", value="buyAlchemy lab")

        if alchemy_lab.get_attribute("class") != "grayed":
            alchemy_lab.click()
        elif shipment.get_attribute("class") != "grayed":
            shipment.click()
        elif mine.get_attribute("class") != "grayed":
            mine.click()
        elif factory.get_attribute("class") != "grayed":
            factory.click()
        elif grandma.get_attribute("class") != "grayed":
            grandma.click()
        elif cursor.get_attribute("class") != "grayed":
            cursor.click()

        timeout = time.time() + 5
