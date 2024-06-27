from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome opem after program finishes
site = "https://en.wikipedia.org/wiki/Main_Page"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.get(site)

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a").text
print(article_count)
