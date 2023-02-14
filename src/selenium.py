from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.google.com/')

#TODO : sa incercam sa dam click pe accept si sa facem o cautare dupa si sa facem o cautare dupa politicieni din RO

driver.find_element(By.ID, 'locatorul')
search.send_keys()