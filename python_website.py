from selenium import webdriver
# To keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# by should take element attribute
search_bar = driver.find_element(by="name", value="q")

# gets the element name
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))
print(search_bar.size)

docs_link = driver.find_element(by="css selector", value=".documentation-widget a")
print(docs_link.text)

# if none of css or element selectors work, we can use XPATH
# inspect the element => copy xpath
bug_link = driver.find_element(by="xpath", value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

driver.close()
