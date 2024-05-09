from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# maximize window size to show the input field
driver.maximize_window()

stats_number = driver.find_element(by="css selector", value="#articlecount > a:nth-child(1)")
print(stats_number.text)

# find a link by its name
free_link = driver.find_element(by="link text", value="free")
# free_link.click()

# Enter python in the search bar then press enter
search_field = driver.find_element(by="css selector", value="#searchInput")
search_field.send_keys("Python", Keys.ENTER)

driver.close()
