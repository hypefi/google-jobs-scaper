#!/usr/bin/env python
# coding: utf-8

# In[5]:


from bs4 import BeautifulSoup
import requests
import selenium
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import time
import numpy as np
import numpy
import datetime
import json


# In[6]:


def manually_get_job_data(job_name):
    job_name = job_name.replace(' ','_')
    job_url_name = job_name.replace('_','+')
    pre_url = f'https://www.google.com/search?q={job_url_name}&ibp=htl;jobs#fpstate=tldetail&htidocid='
    driver = webdriver.Chrome(executable_path='./chromedriver')
    print( 'hi' ) 
    test_url = f'https://www.google.com/search?q={job_url_name}&ibp=htl;jobs'
    driver.get(test_url)
    proceed = 0
    while proceed != 'Y':
        proceed = input('Are You Ready To Proceed? (Y/N)').upper()
    for i in [pre_url+link.attrs['id'][4:] for link in BeautifulSoup(driver.page_source, 'lxml').find_all('div',{'jsname':'x5pWN'})]:
        driver.get(i)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    jobs = soup.find_all('li')
    #print(jobs)
    job_list = []
    for job in jobs:
        if (job.find('h2',{'jsname':'SBkjJd'}) != None):
            job_dic = {}
            job_dic['title']= job.find('h2',{'jsname':'SBkjJd'}).text
            print('-------------')
            print(job_dic['title'])
            job_dic['company']=job.find('div',{'class':'nJlQNd sMzDkb'}).text
            print(job_dic['company'])
            job_dic['description']=job.find('span',{'class':'HBvzbc'}).text
            print(job_dic['description'])
            try:
                    job_dic['location']=job.find_all('div',{'class':'sMzDkb'})[1].text
            except:
                    print("Something went wrong in fetching location")
                    job_dic['location']='Remote'
                    pass
            print(job_dic['location'])
            #url 
            print(job.find('a',{'class':'pMhGee Co68jc j0vryd'}))
            at = job.find('a',{'class':'pMhGee Co68jc j0vryd'})
            print(at['href'])
            job_dic['url']= at['href']
            #contact
            #date 
            job_dic['createdAt'] = datetime.datetime.now().isoformat()
            job_dic['upDatedAt'] = datetime.datetime.now().isoformat()
            #html description
            print(type(job.find('span',{'class':'HBvzbc'})))
            job_dic['htmlDescription']=str(job.find('span',{'class':'HBvzbc'}))
            
            print('htmldescription',job_dic['htmlDescription'])
            #userid 
            job_dic['userId'] = 'qRofzWAQpCqJp9kXC'
            #jobtype
            job_dic['jobtype'] = 'Full time'
            #user
            job_dic['userName'] = 'Anas Boukharta'
        
   
            #htmlDescription
            job_list.append(job_dic)
 #   print(job_list)
    
    
    ##save to json file 
    with open('google-scraper-jobs-remote-MA.json', 'w') as outfile:
        json.dump(job_list, outfile)
    ##send to mongodb 
    

  #  full = pd.read_csv('./Jobs/full_jobs_df.csv')
  #  full.avg_salary = full.avg_salary.astype('object')
    new = pd.DataFrame(job_list)
   # try:
   #     new.salary = new.salary.astype('object')
   #     full = pd.merge(full,new,how='outer')
   #     full.drop_duplicates(inplace=True)
   #     full.body = full.body.str.lower()
   #     full.to_csv('./Jobs/full_jobs_df.csv',index=False)
   # except:
   #     pass

    driver.quit()
   # print(f'We now have {full.shape[0]} jobs')
   # print(f'{full.avg_salary.notnull().sum()} of these jobs have a salary')
    return 


# In[7]:


word = input("Enter Job Title")
manually_get_job_data(word)


# In[ ]:





# In[ ]:




