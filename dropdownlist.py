import os
import time

from selenium import webdriver

# expected result ==> assertion
from selenium.webdriver.support.select import Select

result = "OK. Good answer"

path_d = os.getcwd() + r'\chromedriver.exe'
url = r"https://antycaptcha.amberteam.pl:5443/exercises/exercise3?"

# go to the website
wd = webdriver.Chrome(executable_path=path_d)
wd.get(url)

# text to fill in
text_to_select = wd.find_element_by_xpath("/html/body/div/table/tbody/tr[2]/td[2]/code").text


# select proper option
dropdown = wd.find_element_by_xpath('//*[@id="s13"]')
dropdown_select = Select(dropdown)
dropdown_select.select_by_visible_text(text_to_select)
time.sleep(1)

# click: 'check solution'
button = wd.find_element_by_id("solution").click()

# chceck the answer and quit browser
try:
    time.sleep(1)
    answer = wd.find_element_by_xpath('//*[@id="trail"]/code').text
    assert answer == result
finally:
    wd.quit()