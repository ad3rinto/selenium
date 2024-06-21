from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome opem after program finishes
site = "https://python.org"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.get(site)

# price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
title = driver.title
# print(title)
list_of_events = driver.find_elements(By.CSS_SELECTOR, ".menu li")
print(list_of_events)

# closes particular tab
# driver.close()
#
# closes all tabs
# driver.quit()
