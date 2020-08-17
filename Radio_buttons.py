import os
import time

from selenium import webdriver

result = "OK. Good answer"

path_d = os.getcwd() + r'\chromedriver.exe'
url = r"https://antycaptcha.amberteam.pl:5443/exercises/exercise4?"

# go to the website
wd = webdriver.Chrome(executable_path=path_d)
wd.get(url)

# radiobuttons
dict = {"Beluga Brown": 1,
        "Mango Orange": 2,
        "Verdoro Green": 3,
        "Freudian Gilt": 4,
        "Pink Kong": 5,
        "Duck Egg Blue": 6,
        "Anti - Establishment Mint": 7,
        "Amberlite Firemist": 8}

# group 0 radio button
group0 = wd.find_element_by_xpath('/html/body/div/table/tbody/tr[2]/td[2]/code').text

#select radio button - group 0
group0_click = wd.find_element_by_xpath('/html/body/div/div[1]/input[' + str(dict.get(group0)) + ']').click()
time.sleep(1)

# group 1 radio button
group1 = wd.find_element_by_xpath('/html/body/div/table/tbody/tr[3]/td[2]/code').text

#select radio button - group 1
group1_click = wd.find_element_by_xpath('/html/body/div/div[2]/input[' + str(dict.get(group1)) + ']').click()
time.sleep(1)

# group 2 radio button
group2 = wd.find_element_by_xpath('/html/body/div/table/tbody/tr[4]/td[2]/code').text

#select radio button - group 2
group2_click = wd.find_element_by_xpath('/html/body/div/div[3]/input[' + str(dict.get(group2)) + ']').click()
time.sleep(1)

# group 3 radio button
group3 = wd.find_element_by_xpath('/html/body/div/table/tbody/tr[5]/td[2]/code').text

#select radio button - group 3
group3_click = wd.find_element_by_xpath('/html/body/div/div[4]/input[' + str(dict.get(group3)) + ']').click()
time.sleep(1)

# click solution button
solution_button = wd.find_element_by_xpath('//*[@id="solution"]').click()

# chceck the solution
try:
    time.sleep(1)
    answer = wd.find_element_by_xpath('//*[@id="trail"]/code').text
    assert answer == result
finally:
    wd.quit()
