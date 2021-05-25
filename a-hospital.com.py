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

with open('A-hospital-raw-data.csv', 'wb') as fp:
    fp.write(codecs.BOM_UTF8)
    spamwriter = csv.writer(fp,dialect='excel')
    spamwriter.writerow(['Name', 'Address', 'Phone','Level', 'Specialty', 'Management', 'Website'])
    code = ["%E5%8C%97%E4%BA%AC%E5%B8%82%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E9%87%8D%E5%BA%86%E5%B8%82%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E5%A4%A9%E6%B4%A5%E5%B8%82%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E6%B1%9F%E8%8B%8F%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E5%B9%BF%E4%B8%9C%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E5%B1%B1%E4%B8%9C%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E8%BE%BD%E5%AE%81%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E6%B2%B3%E5%8C%97%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E6%B2%B3%E5%8D%97%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E5%9B%9B%E5%B7%9D%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E9%BB%91%E9%BE%99%E6%B1%9F%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E5%B1%B1%E8%A5%BF%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E6%B9%96%E5%8C%97%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E6%B9%96%E5%8D%97%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E9%99%95%E8%A5%BF%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E6%B5%99%E6%B1%9F%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E4%BA%91%E5%8D%97%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E5%90%89%E6%9E%97%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E5%AE%89%E5%BE%BD%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E5%B9%BF%E8%A5%BF%E5%A3%AE%E6%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E6%B1%9F%E8%A5%BF%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E7%A6%8F%E5%BB%BA%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E6%96%B0%E7%96%86%E7%BB%B4%E5%90%BE%E5%B0%94%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E5%86%85%E8%92%99%E5%8F%A4%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E7%94%98%E8%82%83%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E8%B4%B5%E5%B7%9E%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E6%B5%B7%E5%8D%97%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E9%9D%92%E6%B5%B7%E7%9C%81%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E5%AE%81%E5%A4%8F%E5%9B%9E%E6%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E8%A5%BF%E8%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8","%E8%A5%BF%E8%97%8F%E8%87%AA%E6%B2%BB%E5%8C%BA%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8"]
    #code = ["%E5%8C%97%E4%BA%AC%E5%B8%82%E5%8C%BB%E9%99%A2%E5%88%97%E8%A1%A8"]
    i = 0
    x = 0
    for i in range(0, 31):
        nextlink = "http://www.a-hospital.com/w/"+str(code[i])
        print(nextlink)
        try:
            response = requests.get(nextlink, timeout = 10)
            soup = BeautifulSoup(response.text, "html.parser")
            data = soup.find("ul").find_all("ul")
            names = soup.find("ul").find_all("li")
            url = soup.find("ul").find_all("a", class_="external free")
            time.sleep(sleeptime(0,0,5))
            for item in names:
                    if item.find("b").find("a") != None:
                        item = item.find("b").find("a").getText()
                        detail = data[x].getText().replace("\t", ",").replace("\n", ",")
                        fp.write(item.encode('utf-8')+","+detail.encode('utf-8'))
                        print(item+detail)
                        if x < len(data)-1:
                            x+=1
                        fp.write("\n")
                    
            x = 0
            #for na in url:
                #fp.write(na.getText().encode('utf-8')+",")
                #fp.write("\n")
                #print(na.getText())
            fp.write("\n")
            
                
        except requests.exceptions.Timeout:
            print("Timeout occurred")




