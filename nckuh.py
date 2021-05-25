import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import io
import time
import csv
import codecs

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;

names = []
with open('NTKUH-Data-List3.csv', 'wb') as fp:
    fp.write(codecs.BOM_UTF8)
    spamwriter = csv.writer(fp,dialect='excel')
    spamwriter.writerow(['Source URL', 'Name', 'Department', 'Education', 'Experience', 'Specialty'])
    code = ["01","02","03","04","05","06","07","08", "09","10","11","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","3101","3102","3103","3104","3105","3106","3F","3G","3J",'3H','3K','3L','3M','3N','3P','3I1','3I2','3I3','3I4','3I5','3I6','3Q','3R','3S','3T','3U','3V','3W','3X','3Y','4A','61','62','63','64','65','66','67','68','69','6A','6B','6C','6D','71','72','73','74','75','76','77','78','81','82','96','97','9X01']
    i = 1
    while (i<=973):
        nextlink = "https://service.hosp.ncku.edu.tw/WebPage/drinfo/dr_detail.jsp?id="+str(i)+"&deptno=50"
        response = requests.get(nextlink)
        soup = BeautifulSoup(response.text, "html.parser")
        names = soup.find_all("td",width="40%")
        dep = soup.find("td",width="60%")
        education = soup.find_all("td", width ="416")
        x = 0
        for number in names:
            fp.write(nextlink+",")
            N = number.select_one("font").getText().strip()
            print(N)
            fp.write(N.encode('utf-8')+',')
            fp.write(dep.select_one("font").getText().strip().encode('utf-8')+','+education[x].select_one("font").getText().replace("\r", " ").replace("\n", " ").replace(",", " ").encode('utf-8')+','+education[x+1].select_one("font").getText().replace("\r", " ").replace("\n", " ").replace(",", " ").strip().encode('utf-8')+','+education[x+2].select_one("font").getText().replace("\r", " ").replace("\n", " ").replace(",", " ").strip().encode('utf-8')+"\n")
            x = x+3
        i = i + 1
        x = 0

