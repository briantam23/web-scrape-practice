#!/usr/local/opt/python@3.8/bin/python3

import requests
from bs4 import BeautifulSoup
import pandas as pd


website_url = requests.get('https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area').text
soup = BeautifulSoup(website_url,'lxml')

My_table = soup.find('table',{'class':'wikitable sortable'})
links = My_table.findAll('a')

Countries = []
for link in links:
    Countries.append(link.get('title'))
    
df = pd.DataFrame()
df['Country'] = Countries

print(df)