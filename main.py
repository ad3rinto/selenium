from selenium import webdriver

# Keep Chrome opem after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.aaderinto.com")

# closes particular tab
# driver.close()
#
# closes all tabs
# driver.quit()
