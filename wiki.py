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


the_path = "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[3]/div/table/tbody/tr[1]/td/span/a/img"

article_images = driver.find_element(By.XPATH, the_path).get_attribute("a")

print(article_images)

