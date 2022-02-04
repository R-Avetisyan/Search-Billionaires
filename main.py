from bs4 import BeautifulSoup
import requests
import csv

name = input('>')
name = name.title()

csv_file = open('info_csv.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','link'])

source = requests.get('https://www.celebritynetworth.com/list/top-100-richest-people-in-the-world/').text
soup = BeautifulSoup(source,'lxml')

content = soup.find('main',class_ = 'cnw_top_100')
lst = content.find_all('li')


for person in lst:
       if name != person.h2 and person.h2 == None:
            pass
        
        
       elif name in person.h2.text:
            try:
            
            
                headline = person.h2.text
                
                summary = person.find('div',class_ = 'bio').text
                    
                src_link = person.a['href']
                
                csv_writer.writerow([headline,summary,src_link])  
                
                csv_file.close()
                

                

            except Exception as e:
                pass

       

       
       