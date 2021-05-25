import requests
from bs4 import BeautifulSoup
import io
import time

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
fp = io.open("NCKUH_Op_Data-List.txt", "ab+")
i = 19351
while (i<=19357):
    nextlink = "http://ophth.med.ncku.edu.tw/p/412-1123-"+str(i)+".php?Lang=zh-tw"
    response = requests.get(nextlink)
    soup = BeautifulSoup(response.text, "html.parser")
    names = soup.find_all("span", style="font-size:1em;")

#print(phones)
    #time.sleep(sleeptime(0,1,0))
    for number in names:
    #item = number.get("href")
        print(number.getText())
        fp.write(number.getText().encode('utf-8')+",")
        #print(number.select_one("span").getText())
    fp.write("\n")
    i = i + 1
#tEnd = time.time()
fp.close()
