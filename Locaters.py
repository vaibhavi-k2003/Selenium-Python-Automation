import time
from selenium import webdriver
# This line is crucial for finding elements!
from selenium.webdriver.common.by import By

# 1. Start Chrome automatically (No manual file path needed!)
driver = webdriver.Chrome()

# 2. Open the practice website
driver.get('https://rahulshettyacademy.com/angularpractice/')

# 3. Maximize the window so you can see everything clearly
driver.maximize_window()
time.sleep(2)

# 4. Automate filling out the form
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# 5. Hold it open for 4 seconds to watch it work, then close cleanly
time.sleep(4)
driver.quit()