#!/bin/env python3

from dotenv import dotenv_values
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


opts = Options()
# uncomment if want it to be automated
# opts.headless = True
browser = Firefox(options=opts)
# login page
iti_login = "http://apps.iti.gov.eg/ManagementSystem/intlogin.aspx"
browser.get(iti_login)
# load login secrets
secrets = dotenv_values(".env.secrets")
# enter login secrets
browser.find_element(By.ID, "txtUsername").send_keys(secrets["COOL_USER"])
browser.find_element(By.ID, "txtpassword").send_keys(secrets["GREATEST_PASSWD"])
browser.find_element(By.ID, "btnlogin").click()

# focus on first selection in course evaluation
browser.find_element(By.ID, "ContentPlaceHolder1_UcCourseEval1_ddlCourseName_chzn").click()
courses = browser.find_element(By.CLASS_NAME, "chzn-results").find_elements(By.TAG_NAME, "li")
# print course index and name
for idx, course in enumerate(courses):
    print(f"{idx} : {course.text}")

# select the first course to evaluate
courses[0].click()
stars = browser.find_elements(By.CLASS_NAME, "ratingStar")
rev_stars = list(reversed(stars))
# get user rate for course
rate = int(input("Rate from 1 to 5 : "))
for s in rev_stars:
    if stars.index(s) % 5 == (rate-1):
        s.click()

# submit rating
browser.find_element(By.ID, "ContentPlaceHolder1_UcCourseEval1_btnSave").click()
browser.find_element(By.CSS_SELECTOR, ".buttonM.bBlack.formSubmit").click()
# grades page
# logout from iti
browser.find_element(By.CSS_SELECTOR, ".logout.tipN").click()
browser.implicitly_wait(5)
# close browser
browser.close()
# quit script
quit()
