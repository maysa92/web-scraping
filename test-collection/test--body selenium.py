import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import io
import time
import csv
import codecs
import os
import pandas as pd
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

os.chdir('/Users/Sheryl/H1/test-collection')
df = pd.read_excel("test.xlsx", index_col = None, engine="openpyxl") 
chrome_options = Options()
chrome_options.add_argument("--headless")
results = []   
names = [] 

for row in df.itertuples(): 
    result = []
    Name = row[1]
    url = row[2]
    base_url = str(url)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_page_load_timeout(30)
    driver.get(base_url)
    content = driver.find_elements_by_xpath("//*[contains(text(), Name)]")
    print(content.getText())
    try:
        #start = 0
        print(url)
        print(Name)
        response = requests.get(url, timeout = 20, verify=False)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")
        #for elem in soup(text=re.compile(Name)):
            #print(elem.parent)
            #elem1 = elem.replace("\t", "").replace("\r", "").replace(" ", "").replace("\n\n", "/").replace("\n","")
            #print(elem1)
        #name = soup.find_all(lambda tag:tag.name=="div" and Name in tag.text)
        #for item in name:
            #if item != None:
                #item = item.getText().replace("\t", "").replace("\r", "").replace(" ", "").replace("\n\n", "/").replace("\n","")
            #if Name in item:
                #start = 1
            #if start == 1:
            #result.append(elem1)  
                     
    except requests.exceptions.Timeout:
        print("Timeout occurred")
        result.append('Timeout')
    except requests.exceptions.MissingSchema:
        print("Invalid URL")
        result.append('Invalid URL')
    results.append(result) 
df['Bio'] = results
df.to_excel("output.xlsx",engine='xlsxwriter',index=False)
    #print(results)
    #for index in range(len(Name)):
        #fp.write(str(Name[index]).encode('utf-8') + ",".encode('utf-8') + str(url[index]).encode('utf-8') + ",".encode('utf-8') +str(results[index]).encode('utf-8')+ "\n".encode('utf-8'))


