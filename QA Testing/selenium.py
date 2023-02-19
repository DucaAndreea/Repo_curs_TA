"""from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.google.com')"""

import time

from selenium import webdriver



driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.

driver.get('http://www.google.com/')

