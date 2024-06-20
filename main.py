from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome opem after program finishes
site = "https://www.amazon.co.uk/Microsoft-Surface-Laptop-Super-Thin-Touchscreen/dp/B0B9NZJJ1J/ref=sr_1_1?dib=eyJ2IjoiMSJ9.UY9YZlwF_sfzygWZUMbhDzFTL4WnGXH7CDhK7NqvzFawFUwHi_3cfmjAYiuCoeZp93-dFxUReXm305kd5dsb9NExPUpnxdXLhLlGkscoqcgOB8UebCTPPwA7TK_SNbQXVQVqMjVx9Ia7cOiAfbdnuDrRlvR-i4i4AiWumYr3huBRgemYycCAI8QNj44vXU-hwXz5aEmG9vyQ_lVLnz--OQ.oWMNxZkjmJlsp-8ZVXEGYDtmKV5__rxIzayFHe8rLME&dib_tag=se&psc=1&qid=1718881819&refinements=p_n_style_browse-bin%3A182752031%2Cp_72%3A419153031%2Cp_n_feature_three_browse-bin%3A65990421031&rnid=65990412031&s=computers&sr=1-1"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome()
driver.get(site)

price = driver.find_element(By.CLASS_NAME, "a-price-whole").text
title = driver.title
print(price)


# closes particular tab
# driver.close()
#
# closes all tabs
# driver.quit()
