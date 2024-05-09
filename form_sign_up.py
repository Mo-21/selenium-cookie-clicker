from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome()
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(by="name", value="fName")
last_name = driver.find_element(by="name", value="lName")
email = driver.find_element(by="name", value="email")

first_name.send_keys("Hello")
last_name.send_keys("World")
email.send_keys("hello@world.com")

submit = driver.find_element(by="css selector", value="form button")
submit.click()
