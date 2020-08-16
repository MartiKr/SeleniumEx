import os
import time

from selenium import webdriver

# expected result ==> assertion
result = "OK. Good answer"

path_d = os.getcwd() + r'\chromedriver.exe'
url = r"https://antycaptcha.amberteam.pl:5443/exercises/exercise3?"

# go to the website
wd = webdriver.Chrome(executable_path=path_d)
wd.get(url)

# text to fill in
text_to_fill = wd.find_element_by_xpath("/html/body/div/table/tbody/tr[2]/td[2]/code").text
