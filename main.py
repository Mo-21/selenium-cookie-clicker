from selenium import webdriver

# To keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.mohammad-malaeb.com")

# closes a specific tab when it finishes loading
# driver.close()

# shuts down the whole browser when it finishes loading
# driver.quit()
