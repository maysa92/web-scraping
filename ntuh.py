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

with open('NTUH-Data-List13.csv', 'wb') as fp:
    fp.write(codecs.BOM_UTF8)
    spamwriter = csv.writer(fp,dialect='excel')
    spamwriter.writerow(['Source URL', 'Department', 'Name', 'Name_en','Title', 'Specialty', 'Current job', 'Education', 'Experience'])
    code = ["Med","Ped","neur","PSY","PMR","FM","onc","gene", "gero","surg","orth","obgy","ENT","OPH","urology","derm","dent","Ane","dtra","emergency","labmed","radiology","DIDT"]
    i = 0
    for v in range(2065, 2080):
        for i in range(0, 23):
            nextlink = "https://www.ntuh.gov.tw/"+str(code[i])+"/Vcard.action?q_type=-1&q_itemCode="+str(v)
            print(nextlink)
            try:
                response = requests.get(nextlink, timeout = 10)
                soup = BeautifulSoup(response.text, "html.parser")
                if soup.find("div", class_="uk-width-5-6@s uk-width-expand@m") != None:
                    names = soup.find("div", class_="uk-width-5-6@s uk-width-expand@m").find_all("span", limit = 2)
                    titl = soup.find("div", class_="uk-width-5-6@s uk-width-expand@m").find_all("span", class_="pseudo:comma_dot mr-0 pr-0", limit = 1)
                    specialty = soup.find("div", class_="uk-width-5-6@s uk-width-expand@m").find_all("span", class_="pseudo:comma_dot mr-0 pr-0")
                    if soup.find("div", class_="urlFix") != None:
                        current = soup.find("div", class_="urlFix").select_one("table", class_="uk-table uk-table-small uk-table-striped uk-first-column").find("tbody")
                        education = soup.find("ul", class_="uk-switcher uk-margin").find("li").find_next_sibling("li").select_one("table", class_="uk-table uk-table-small uk-table-striped uk-first-column").find("tbody")
                        experience = soup.find("ul", class_="uk-switcher uk-margin").find("li").find_next_sibling("li").find_next_sibling("li").select_one("table", class_="uk-table uk-table-small uk-table-striped uk-first-column").find("tbody")
                    time.sleep(sleeptime(0,0,5))
                    fp.write(nextlink+","+code[i]+",")
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
                    for ed in current:
                        if isinstance(ed, NavigableString):
                            continue
                        fp.write(ed.select_one("td").getText().encode('utf-8')+" "+ed.select_one("td").find_next_sibling("td").getText().encode('utf-8')+"/")
                        print(ed.select_one("td").getText()+" "+ed.select_one("td").find_next_sibling("td").getText())
                    fp.write(",") 
                    for ed in education:
                        if isinstance(ed, NavigableString):
                            continue
                        fp.write(ed.select_one("td").getText().encode('utf-8')+" "+ed.select_one("td").find_next_sibling("td").getText().encode('utf-8')+"/")
                        print(ed.select_one("td").getText()+" "+ed.select_one("td").find_next_sibling("td").getText())
                    fp.write(",") 
                    for ed in experience:
                        if isinstance(ed, NavigableString):
                            continue
                        fp.write(ed.select_one("td").getText().encode('utf-8')+" "+ed.select_one("td").find_next_sibling("td").getText().encode('utf-8')+"/")
                        print(ed.select_one("td").getText()+" "+ed.select_one("td").find_next_sibling("td").getText())
                    fp.write("\n")
                    break
            except requests.exceptions.Timeout:
                print("Timeout occurred")



