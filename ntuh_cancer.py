import requests
from bs4 import BeautifulSoup
import io
import time
import csv
import codecs

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;

names = []
specialty = []
#print(soup.prettify())
#result = soup.find("h3")
#print(result)
#result = soup.find_all("h3", itemprop="headline", limit=3)
#print(result)
#tStart = time.time()
with open('Data-List.csv', 'wb+') as fp:
    fp.write(codecs.BOM_UTF8)
    spamwriter = csv.writer(fp,dialect='excel')
    spamwriter.writerow(['Source URL', 'Department', 'Name', 'Title', 'Specialty'])
    i = 1
    while (i<=10):
        nextlink = "https://www.ntucc.gov.tw/ntucc/DoctorOne.action?tid="+str(i)
        response = requests.get(nextlink)
        soup = BeautifulSoup(response.text, "html.parser")
        if soup.select('h1') != []:
            names = soup.find("h2").find_all("span")
            specialty = soup.find_all("span", class_="comma_dot mr-0 pr-0")

#print(phones)
    #time.sleep(sleeptime(0,1,0))
        for number in names:
    #item = number.get("href")
            fp.write(number.getText().encode('utf-8')+",")
            print(number.getText())
        for item in specialty:
            fp.write(item.getText().encode('utf-8')+",")
            print(item.getText())
        fp.write("\n")
        i = i + 1
#tEnd = time.time()
