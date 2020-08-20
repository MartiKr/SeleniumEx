import json
import os
import time
import csv

from selenium import webdriver

path = os.getcwd() + '\\chromedriver.exe'
url = r'https://cinkciarz.pl/wymiana-walut/kursy-walut'

# go to the website
wd = webdriver.Chrome(executable_path=path)
wd.get(url)

time.sleep(1)

# click cookies info
cookie = wd.find_element_by_xpath('//*[@id="cookies-modal"]/div/div/div/div[1]/div/button[2]').click()

time.sleep(1)

# add currencies to the table
currencies = wd.find_elements_by_xpath('//*[@id="currencies-rates"]/table/tbody/tr/td/a/strong')

currency = [ ]
for c in currencies:
    currency.append(c.text)

# add buy prices to the table
buy_v = wd.find_elements_by_xpath('//*[@id="currencies-rates"]/table/tbody/tr/td[4]/a/span/span')

buy = [ ]
for b in buy_v:
    buy.append(b.text)

# add sell prices to the table
sell_v = wd.find_elements_by_xpath('//*[@id="currencies-rates"]/table/tbody/tr/td[5]/a/span/span')

sell = [ ]
for s in sell_v:
    sell.append(s.text)

# prepare data for csv file
csv_list = [ ]
csv_list.append([ 'Country', 'Buy price', 'Sell price' ])
for i in range(len(currency)):
    list = [ ]
    list.append(currency [ i ])
    list.append(str(buy [ i ]))
    list.append(str(sell [ i ]))
    csv_list.append(list)

# create csv file
with open('currencies.csv', 'w') as csv_file:
    for i in csv_list:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(csv_list)

# prepare data for json file
dict = {}
for i in range(len(currency)):
    dict [ currency [ i ] ] = {'buy': buy [ i ], 'sell': sell [ i ]}

# create json file
with open('currency.json', 'w') as json_file:
    data = json.dumps(dict,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    json_file.write(data)

# quit browser
wd.quit()
