# -*- coding: utf-8 -*-
"""colab+drive.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ATKz6wcn2Hssg6YHxlDWvXqEp2DTl5V9
"""

import bs4
import requests
import re
import pandas as pd
import datetime
from bs4 import BeautifulSoup

def scraper(s):
    r = requests.get(s)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    
    title = soup.find("h1", {"class": "brkword lheight28"})
    if title is not None:
      title = title.text
      title = title.strip()

    para = soup.find("p", {"class":"pding10 lheight20 large"})
    if para is not None:
      para = para.text
      para = para.strip()
    
    location = soup.find("strong", {"class": "c2b small"})
    if location is not None:
      location = location.text
      location = location.strip()
    
    ad_id = soup.find("span", {"class": "rel inlblk"})
    if ad_id is not None:
      ad_id = ad_id.text
      ad_id = ad_id.strip()
    
    name = soup.find("span", {"class": "block color-5 brkword xx-large"})
    if name is not None:
      name = name.text
      name = name.strip()
    
    date = soup.find("span", {"class": "pdingleft10 brlefte5"})
    if date is not None:
      date = date.text
      date = date.strip()
      
    price = soup.find("strong", {"class": "xxxx-large margintop7 inlblk not-arranged"})
    if price is not None:
      price = price.text.strip()
    
    
#       regex = "\d\d:\d\d"
#       if re.findall(regex, date)!=[]:
#         date = datetime.date.today()
        
    return ad_id, date, name, location, price, title, para

def tablescraper(s):
    links = []
    count = 0
    r = requests.get(s)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    class_name = "marginright5 link linkWithHash detailsLink"
    links = soup.findAll("a", {"class":class_name})
    
    data2 = []

    for i in links:
        a, b, c, d, e, f, g = scraper(i["href"])
        data2.append([a, b, c, d, e, f, g])
        count = count + 1
        print(count)
        
    return data2

def check_phno(data):
    regex = '\d[0-9\.\s\,O=\-\:\;\_]+'
    phno = []


    for i in data:
        temp = re.findall(regex, repr(i))
        if temp!=[]:
            phno.append(temp)

    real_phno = set()
    for i in phno:
        for j in i:
            if(len(j)>=10):
                real_phno.add(j)
        
    real_phno = list(real_phno)


    final_phno = []
    for i in real_phno:
        num_count = 0
        temp = ''
        for j in i:
            if j.isdigit() == True or j == 'O':
                num_count = num_count + 1
                if j == 'O':
                    temp = temp + '0'
                else:
                    temp = temp + j
        if num_count == 10:
            final_phno.append(temp)

    print(final_phno)

s = "https://www.olx.in/sale/"

data2 = []
urls = []
for i in range (1, 500):
    temp = s + "?page=" + str(i)
    print(temp)
    urls.append(temp)
    data = tablescraper(s)
    data2.append(data)

data3 = []
headers = ['Id', 'Date', 'Name', 'Location', 'Price', 'Title', 'Description']
data3.append(headers)

for i in data2:
  for j in i:
    data3.append(j)

import csv

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(data3)