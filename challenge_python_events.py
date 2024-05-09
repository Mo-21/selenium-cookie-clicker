from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome()
driver.get("https://www.python.org")

events_items = driver.find_elements(
    by="css selector",
    value="#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li"
)

upcoming_events = {
    n: {
        "time": event_item.text.split('\n')[0],
        "name": event_item.text.split('\n')[1]
    }
    for n, event_item in enumerate(events_items)
}

print(upcoming_events)

driver.close()
