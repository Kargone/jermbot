# Selenium Tutorial #1
# https://sites.google.com/a/chromium.org/chromedriver/downloads
# vote for dayspring

# importing time and webdriver libraries
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

options = Options()

# true is close page, false is leave page open
options.add_experimental_option("detach", True)

# create the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

# open the website with mike morton pre authenicated
driver.get(r"http://robertsoncountyconnection.secondstreetapp.com/api/organization_user_email_verifications?token=0vll52jnspk&opid=985719&lrt=h1qeel5o1nd&bf=56d4d613277aa5831a19f34521695dbd&ip=71.142.229.196&redirect=https%3a%2f%2frobertsoncountyconnection.secondstreetapp.com%2f2023-Robertson-County-Main-Street-Awards%2f%23%2flogin%2fxqx0vzrb2r1%2f-SS-gallery-SS--QQ-group-EE-457030&smqid=128780112")

# maximize window
driver.maximize_window()

# wait 2 seconds for the page to load
time.sleep(2.00)

# switch the driver to the iframe path, so that it finds the elements inside the iframe instead of the outer html document
driver.switch_to.frame(driver.find_element("xpath", "//iframe"))

# find the vote button according to the text to the left of it, in this case 'Air2Art Studio' 
buttons = driver.find_elements("xpath", "//div/div/a/span[text()='Air2Art Studio']/../../../div/div/div/button")

# buttons[0].click()


# down here i am working on scrolling down
# as the whole page is not loaded at once
# and the other vote elements are down there

# trying to find how far to scoll down (prob window - 3500)
body = driver.find_element(By.TAG_NAME, "body")
print(body)

# this will preform the scroll action
# ActionChains(driver)\
#     .scroll_by_amount(0, delta_y)\
#     .perform()

# documentation: https://www.selenium.dev/documentation/webdriver/actions_api/wheel/