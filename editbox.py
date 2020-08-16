import os
import time

from selenium import webdriver

# expected result ==> assertion
result = "OK. Good answer"

path_d = os.getcwd() + r'\chromedriver.exe'
url = r"https://antycaptcha.amberteam.pl:5443/exercises/exercise2"

# go to the website
wd = webdriver.Chrome(executable_path=path_d)
wd.get(url)

# text to fill in
text_to_fill = wd.find_element_by_xpath("/html/body/div/table/tbody/tr[2]/td[2]/code[1]").text


textbox = wd.find_element_by_xpath('//*[@id="t14"]')
textbox.clear()
textbox.send_keys(text_to_fill)
time.sleep(1)

button = wd.find_element_by_xpath('//*[@id="btnButton1"]').click()
time.sleep(1)
solution_button = wd.find_element_by_xpath('//*[@id="solution"]').click()

try:
    time.sleep(1)
    answer = wd.find_element_by_xpath('//*[@id="trail"]/code').text
    assert answer == result
finally:
    wd.quit()
