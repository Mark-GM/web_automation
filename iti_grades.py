#!/bin/env python3

from dotenv import dotenv_values
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = Options()
opts.headless = True
browser = Firefox(options=opts)
wait = WebDriverWait(browser, 15)
# login page
iti_login = "http://apps.iti.gov.eg/ManagementSystem/intlogin.aspx"
browser.get(iti_login)

try:
    wait.until(EC.presence_of_element_located((By.ID, "txtUsername")))
except:
    print("the login page is taking too much to load, please try again!")
    quit()
# load login secrets
secrets = dotenv_values(".env.secrets")
# enter login secrets
browser.find_element(By.ID, "txtUsername").send_keys(secrets["COOL_USER"])
browser.find_element(By.ID, "txtpassword").send_keys(secrets["GREATEST_PASSWD"])
browser.find_element(By.ID, "btnlogin").click()

iti_grades = "http://apps.iti.gov.eg/ManagementSystem/Student/StudentGrade.aspx"
browser.get(iti_grades)
browser.implicitly_wait(10)

# get username
username = browser.find_element(By.CSS_SELECTOR, "#lblusername").text
# save grades screenshot
browser.save_full_page_screenshot(f"{username}_grades.png")
# logout from iti
browser.find_element(By.CSS_SELECTOR, ".logout.tipN").click()
browser.implicitly_wait(5)
# close browser
browser.close()
# quit script
quit()
