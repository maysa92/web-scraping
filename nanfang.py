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

with open('Nanfang.csv', 'wb') as fp:
    fp.write(codecs.BOM_UTF8)
    spamwriter = csv.writer(fp,dialect='excel')
    #spamwriter.writerow(['Source URL', 'Department', 'Name', 'Name_en','Title', 'Specialty', 'Current job', 'Education', 'Experience'])
    code = ["zk/jkglzx","zk/hqk","nk/xxgnk","nk/hxnk","nk/snk","nk/xyk","nk/zlk","zk/zyk", "nk/fsbk","wk/gdwk","wk/csgk","wk/xgwk","wk/jzgbk","wk/gjgbwk","wk/mnwk","wk/syzk","wk/sjwk","wk/xxxgwk","zk/ssk","zk/mrzx","zk/mzttk","zk/ek","zk/xsek","zk/grnk","zk/fck","nk/sjnk","zk/rxzx","zk/jzk","zk/zzyxk","zk/fsk","wk/jrzlk","zk/kfyxk","zk/xlmz","zk/kqk","zk/yk","zk/pfk","zk/ebhk","zk/gck"]
    page = ['/DoctorList.html','/DoctorList_2.html','/DoctorList_3.html']
    i = 0
    v = 0
    for i in range(0, 39):
        for v in range(0,3):
            nextlink = "http://www.nfyy.com/ks/"+str(code[i])+str(page[v])
            print(nextlink)
            try:
                response = requests.get(nextlink, timeout = 20)
                soup = BeautifulSoup(response.text, "html.parser")

                names = soup.find_all("div", class_="cont cont2 clearfix")
                titl = soup.find_all("div", class_="cont cont2 clearfix")
                if soup.find("div", class_="list_box") != None:
                    specialty = soup.find("div", class_="list_box").find_all("h2")
                bio = soup.find_all("div", class_="cont cont2 clearfix")
                time.sleep(sleeptime(0,0,5))
                fp.write(nextlink.encode('utf-8')+",".encode('utf-8'))
                x = 0
                for x in range(0, len(names)):
                    if soup.find("div", class_="list_box") != None:
                        fp.write(nextlink.encode('utf-8')+",".encode('utf-8'))
                        name = names[x].find("a")
                        fp.write(name.getText().encode('utf-8')+",".encode('utf-8'))
                        print("names ",name.getText())
                        fp.write(",".encode('utf-8'))  
                        tit = titl[x].find("span")
                        ID = tit.getText()
                        ID = ID.replace("\t", "").replace("\r", "").replace("\n", "").replace(",", " ") 
                        fp.write(ID.encode('utf-8'))
                        print("title ",tit.getText())
                        fp.write(",".encode('utf-8'))  
                        sp = specialty[0].getText()
                        sp = sp.replace("\t", "").replace("\r", "").replace("\n", "").replace(",", " ") 
                        fp.write(sp.encode('utf-8'))
                        print("specialty ",sp)
                        fp.write(",".encode('utf-8'))  
                        it = bio[x].find("p")
                        it = it.getText()
                        it = it.replace("\t", "").replace("\r", "").replace("\n", "").replace(",", " ") 
                        fp.write(it.encode('utf-8'))
                        print("bio ",it)
                        fp.write(",".encode('utf-8'))  
                        fp.write("\n".encode('utf-8'))
            except requests.exceptions.Timeout:
                print("Timeout occurred")



