import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import io
import time
import csv
import codecs

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;

names = []
specialty = []

with open('bj_friendship.csv', 'wb') as fp:
    fp.write(codecs.BOM_UTF8)
    spamwriter = csv.writer(fp,dialect='excel')
    for v in range(174, 1141):
        nextlink = "http://www.bfh.com.cn/Html/Doctors/Main/Index_"+str(v)+".html"
        print(nextlink)
        try:
            response = requests.get(nextlink, timeout = 60)
            soup = BeautifulSoup(response.text, "html.parser")
            if soup.find("div", class_="doct_con") != None:
                names = soup.find("div", class_="doct_con").find_all("p", limit = 1)
                titl = soup.find("div", class_="doct_con").find_all("span",limit = 2)
                specialty = soup.find("div", class_="tab_box").find_all("p")
                time.sleep(sleeptime(0,0,5))
                fp.write(nextlink+",")
                for number in names:
                    fp.write(number.getText().encode('utf-8')+",")
                    print(number.getText())
                for tl in titl: 
                    ID = tl.getText()
                    ID = ID.replace("\t", "").replace("\r", "").replace("\n", "").replace(",", " ") 
                    fp.write(ID.encode('utf-8'))
                    print(tl.getText())
                fp.write(",")  
                for item in specialty[1:]: 
                    ID = item.getText()
                    ID = ID.replace("\t", "").replace("\r", "").replace("\n", "").replace(",", " ") 
                    fp.write(ID.encode('utf-8')+" ")
                    print(item.getText())
                fp.write(",")   
                break
        except requests.exceptions.Timeout:
            print("Timeout occurred")



