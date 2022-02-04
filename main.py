from bs4 import BeautifulSoup
import requests
import csv

name = input('>')
name = name.title()

source = requests.get('https://www.celebritynetworth.com/list/top-100-richest-people-in-the-world/').text
soup = BeautifulSoup(source,'lxml')

content = soup.find('main',class_ = 'cnw_top_100')
lst = content.find_all('li')


for person in lst:
       try:
            if name in person.h2.text:
            
                headline = person.h2.text
                
                summary = person.find('div',class_ = 'bio').text
                    
                src_link = person.a['href']
       except Exception as e:
           pass

       
       