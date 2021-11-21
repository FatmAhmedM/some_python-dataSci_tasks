#!/usr/bin/env python
# coding: utf-8

#  # new things I have learned zip longest and for loop feature

# In[62]:


from bs4 import BeautifulSoup
import requests
import csv
from itertools import zip_longest
url = requests.get("http://coreyms.com").text
soup = BeautifulSoup(url , "lxml")


titles = soup.find_all("a" , {"class" : "entry-title-link"})
summary = soup.find('div', class_ = "entry-content").p.text
x=[]
y=[]
for i in range(len(titles)):
    x.append(titles[i].text)   
    y.append(summary[i])
    
filelist = [x, y]

unpacking = zip_longest(*filelist)

fiile= open("thiiiiiiiiis.csv", 'w', encoding= 'utf-8')
letswrite= csv.writer(fiile)
letswrite.writerow(["titles" , "summary"])
letswrite.writerows(unpacking)


# In[ ]:




