import os
import time

from selenium import webdriver

# expected result ==> assertion
result = "OK. Good answer"

path_d = os.getcwd() + r'\chromedriver.exe'
url = r"https://antycaptcha.amberteam.pl:5443/exercises/exercise1?"

# go to the website
wd = webdriver.Chrome(executable_path=path_d)
wd.get(url)

# elements to check
element_1 = wd.find_element_by_xpath("/html/body/div/table/tbody/tr[2]/td[2]/code").text
element_2 = wd.find_element_by_xpath("/html/body/div/table/tbody/tr[3]/td[2]/code").text
element_3 = wd.find_element_by_xpath("/html/body/div/table/tbody/tr[4]/td[2]/code").text


# function for selecting correct button
def clickBut(element):
    if element == "B1":
        wd.find_element_by_id("btnButton1").click()
    else:
        wd.find_element_by_id("btnButton2").click()
    time.sleep(1)


# click correct button
clickBut(element_1)
clickBut(element_2)
clickBut(element_3)

# submit answer
button = wd.find_element_by_id("solution").click()

# check if correct answer
try:
    time.sleep(1)
    answer = wd.find_element_by_xpath('//*[@id="trail"]/code').text
    assert answer == result
finally:
    wd.quit()
