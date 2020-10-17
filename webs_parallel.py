

import bs4
import time
import requests
import re
import pandas as pd
import datetime
from bs4 import BeautifulSoup 
from multiprocessing import Pool
import csv

def scraper(s):
    print(s)
    while True:
      try:
        r = requests.get(s, timeout = 100000)
        break
      except requests.exceptions.RequestException:
        time.sleep(1)

    print(r.status_code)
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
        
    return ad_id, date, name, location, price, title, para

def tablescraper(s):
    links = []

    while True:
      try:
        r = requests.get(s, timeout = 100000)
        break
      except requests.exceptions.RequestException:
        time.sleep(1)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")
    class_name = "marginright5 link linkWithHash detailsLink"
    links = soup.findAll("a", {"class":class_name})
    
    data2 = []

    for i in links:
        a, b, c, d, e, f, g = scraper(i["href"])
        data2.append([[a], [b], [c], [d], [e], [f], [g]])

        
    return data2

def urlgen(site, state, category, maxi):
  s = site + '/' + state + '/' + category + '/'
  urls = []
  for i in range (1, maxi + 1):
    temp = s + "?page=" + str(maxi + 1 - i)
    urls.append(temp)
  
  print(urls)
    
  with Pool(100) as p:
    data = p.map(tablescraper, urls)
    
  data3 = []
  headers = ['Id', 'Date', 'Name', 'Location', 'Price', 'Title', 'Description']
  data3.append(headers)

  for i in data:
    for j in i:
      a = j[0][0]
      b = j[1][0]
      c = j[2][0]
      d = j[3][0]
      e = j[4][0]
      f = j[5][0]
      g = j[6][0]
      data3.append([a, b, c, d, e, f, g])
  output_file_name = "dataset_" + state + "_" + category + ".csv"
  with open(output_file_name, "w") as f:
    writer = csv.writer(f)
    writer.writerows(data3)

def findMax(url):
  r = requests.get(url)
  data = r.text
  soup = BeautifulSoup(data, "html.parser")
  num = soup.findAll("a", {"class": "block br3 brc8 large tdnone lheight24"})
  final = []

  for i in num:
    a = i.text
    final.append(a.strip())
  if final!=[]:
    return int(final[-1])
  else:
    return 1

# categories = ['real-estate', 'vehicles', 'furniture', 'jobs', 'electronics-appliances', 'mobiles', 'bikes', 'books-sports-hobbies', 'fashion-beauty', 'pets', 'services']
categories = ['real-estate', 'vehicles', 'furniture', 'jobs', 'electronics-appliances', 'mobiles', 'bikes', 'books-sports-hobbies', 'fashion-beauty', 'pets', 'services']


# states = ['andamannicobar', 'andhrapradesh', 'arunachalpradesh', 'assam', 'bihar', 'chandigarhcity', 'chhattisgarh', 'stateofdelhi', 'goa', 'gujarat', 'haryana', 'himachalpradesh', 'jammukashmir', 'jharkhand', 'karnataka', 'kerala', 'madhyapradesh', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'orissa', 'sikkim', 'pondicherry', 'punjab', 'tamilnadu', 'telangana', 'tripura', 'uttarpradesh', 'westbengal']
site = "https://www.olx.in"
states = ['westbengal']

for i in states:
  for j in categories:
    site2 = site + "/" + i + "/" + j + "/"
    maxi = findMax(site2)
    urlgen(site, i, j, maxi)