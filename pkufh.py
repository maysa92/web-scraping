import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import io
import time
import csv
import codecs

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;

names = []
data = []

with open('pkufh-data-more.csv', 'wb') as fp:
    fp.write(codecs.BOM_UTF8)
    spamwriter = csv.writer(fp,dialect='excel')
    nextlink = "https://www.pkufh.com/Html/Hospitals/Doctors/Overview0.html"
    try:
        response = requests.get(nextlink, timeout = 10)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")
        name = soup.find_all("a")
        description = soup.find_all("a")
        url = soup.find_all("a")
        time.sleep(sleeptime(0,0,5))
        #for item in name:
            #print(item.getText())
            #fp.write(item.getText().encode('utf-8')+",".encode("ascii")+item.encode('utf-8')+"\n".encode("ascii"))
        #fp.write("\n".encode("ascii"))
        for descrip in description:
            ds = descrip.find("div", class_="speac_div").select("p")
            print(ds.getText())
            fp.write(ds.getText().encode('utf-8'))
        fp.write("\n".encode("ascii"))

                
    except requests.exceptions.Timeout:
        print("Timeout occurred")




