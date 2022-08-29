'''
Created by: Bohuslav Juráš
Contact: Bohuslav.juras@seznam.cz
For: Singh Neeraj / Accenture
Applying for position: Test Automation Engineer
Second task - "Shopping automation"
This program is a work in progress and used as a study case for Selenium learning. More information is being sent in
separate email with screenshots.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)


driver.get("https://www.florbal.com/")
driver.maximize_window()
link = driver.find_element(By.LINK_TEXT, 'Florbalové hole')
link.click()

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Od nejdražšího")))
    element.click()

    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul[@id='products-list']")))
    for i in range(1,5):
        print(i)
        element = driver.find_element(By.XPATH, f"(//li[contains(@class,'col-xs-12 col-sm-4 col-xl-3')])[{i}]")
        element.click()
        time.sleep(3)
        driver.back()
        time.sleep(5)

finally:
    time.sleep(1)


