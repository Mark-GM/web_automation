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
browser.find_element(
    By.ID, "ContentPlaceHolder1_UcCourseEval1_ddlCourseName_chzn"
).click()
courses = browser.find_element(By.CLASS_NAME, "chzn-results").find_elements(
    By.TAG_NAME, "li"
)
# print course index and name
for idx, course in enumerate(courses):
    print(f"{idx} : {course.text}")

# select the first course to evaluate
courses[0].click()
# se
stars = browser.find_elements(By.CLASS_NAME, "ratingStar")
rate = 4  # form 0 to 4 is the index of stars from 1 to 5
# for each line of stars click on 5th star that are on 4th index of each line of stars (takes a while)
for idx, star in enumerate(stars):
    # n = 4 for n in [0,1,2,3,4] where 0 will be 1 star only
    if idx % 5 == rate:
        star.click()

# submit rating
# browser.find_element(By.ID, "ContentPlaceHolder1_UcCourseEval1_btnSave").click()
# grades page
# logout from iti
browser.find_element(By.CSS_SELECTOR, ".logout.tipN").click()
browser.implicitly_wait(5)
# close browser
browser.close()
# quit script
quit()
