import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import io
import time
import csv
import codecs
import os
import pandas as pd
import re
#10:51

os.chdir('/Users/Sheryl/H1/test-collection')
df = pd.read_excel("test.xlsx", index_col = None, engine="openpyxl") 
results = []   
names = [] 

for row in df.itertuples(): 
    result = []
    Name = row[1]
    url = row[2]
    try:
        print(url)
        print(Name)
        response = requests.get(url, timeout = 30, verify=False)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")
        
        #capture bio
        #search with name
        for elem in soup(text=re.compile(Name)):
            elem1 = elem.parent.parent.getText().replace("\t", "").replace("\r", "").replace(" ", "").replace("\n", ";").replace('\u3000',' ')
            elem1 = elem1.replace(';;;',';').replace('\xa0',' ')
            if len(elem.parent.parent.getText()) > 10 and not(re.search('科室导航', elem.parent.parent.getText()))and not(re.search('服务对象', elem.parent.parent.getText())): #likely bio, avoid menu
                result.append(elem1)  
                print(elem1)
        #search section title
        for elem in soup(text=re.compile('简介')):
            elem1 = elem.parent.parent.getText().replace("\t", "").replace("\r", "").replace(" ", "").replace("\n", ";").replace('\u3000',' ')
            elem1 = elem1.replace(';;;',';').replace('\xa0',' ')
            if elem.parent.parent.getText() != '医院简介'and not(re.search('科室导航', elem.parent.parent.getText()))and not(re.search('服务对象', elem.parent.parent.getText())): #avoid menu
                result.append(elem1)  
                print(elem1)
            
        for el in soup(text=re.compile('经历')):
            elem1 = el.parent.parent.parent.getText().replace("\t", "").replace("\r", "").replace(" ", "").replace("\n", ";").replace('\u3000',' ')
            elem1 = elem1.replace(';;;',';').replace('\xa0',' ')
            result.append(elem1)  
            print(elem1)               

        for elem in soup(text=re.compile('介绍')):
            elem1 = elem.parent.parent.getText().replace("\t", "").replace("\r", "").replace(" ", "").replace("\n", ";").replace('\u3000',' ')
            elem1 = elem1.replace(';;;',';').replace('\xa0',' ')
            if elem.parent.parent.getText() != '医院介绍' and not(re.search('科室导航', elem.parent.parent.getText()))and not(re.search('服务对象', elem.parent.parent.getText())): #avoid menu
                result.append(elem1)  
                print(elem1)
              
        #search keyword in bio
        for elem in soup(text=re.compile('学会')):
            elem1 = elem.parent.parent.getText().replace("\t", "").replace("\r", "").replace(" ", "").replace("\n", ";").replace('\u3000',' ')
            elem1 = elem1.replace(';;;',';').replace('\xa0',' ')
            if len(elem.parent.parent.getText()) > 5:
                result.append(elem1)  
                print(elem1)
            continue #if found, skip this round
        
        for el in soup(text=re.compile('协会')):
            elem1 = el.parent.parent.getText().replace("\t", "").replace("\r", "").replace(" ", "").replace("\n", ";").replace('\u3000',' ')
            elem1 = elem1.replace(';;;',';').replace('\xa0',' ')
            if len(el.parent.parent.getText()) > 5:
                result.append(elem1)  
                print(elem1)                     
            continue #if found, skip this round       
                    
        for elem in soup(text=re.compile('特长')):
            elem1 = elem.parent.parent.getText().replace("\t", "").replace("\r", "").replace(" ", "").replace("\n", ";").replace('\u3000',' ')
            elem1 = elem1.replace(';;;',';').replace('\xa0',' ')
            if len(elem.parent.parent.getText()) > 5:
                result.append(elem1)  
                print(elem1) 
            continue #if found, skip this round              
                            
        for ele in soup(text=re.compile('专长')):
            elem1 = ele.parent.parent.getText().replace("\t", "").replace("\r", "").replace(" ", "").replace("\n", ";").replace('\u3000',' ')
            elem1 = elem1.replace(';;;',';')
            if len(ele.parent.parent.getText()) > 5:
                result.append(elem1)  
                print(elem1)                        
            continue #if found, skip this round                          
        
        for elem in soup(text=re.compile('研究')):
            elem1 = elem.parent.parent.getText().replace("\t", "").replace("\r", "").replace(" ", "").replace("\n", ";").replace('\u3000',' ')
            elem1 = elem1.replace(';;;',';').replace('\xa0',' ')
            if len(elem.parent.parent.getText()) > 5 and not(re.search('科室导航', elem.parent.parent.getText()))and not(re.search('服务对象', elem.parent.parent.getText())):
                result.append(elem1)  
                print(elem1)
            continue #if found, skip this round

    #catch errors                       
    except requests.exceptions.Timeout:
        print("Timeout occurred")
        result.append('Timeout')
    except requests.exceptions.MissingSchema:
        print("Invalid URL")
        result.append('Invalid URL')
    except requests.exceptions.InvalidURL:
        print("Invalid URL")
        result.append('Invalid URL')
    except requests.exceptions.ConnectionError:
        print("Connection Aborted")
        result.append('Connection Aborted')
    results.append(result) 
df['Bio'] = results
df.to_excel("output.xlsx",engine='xlsxwriter',index=False)
#11:51