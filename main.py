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
list_of_events_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu li time")
list_of_events_titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu li a")

shaped_dates_list = []
for _ in list_of_events_dates:
    shaped_dates_list.append(_.text)

shaped_names_list = []
for _ in list_of_events_titles:
    shaped_names_list.append(_.text)

full_list_dict = dict(zip(shaped_names_list, shaped_dates_list))

print(full_list_dict)
# closes particular tab
# driver.close()
#
# closes all tabs
# driver.quit()
