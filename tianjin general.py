import os
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup, NavigableString, Tag
import csv
import codecs
import io
from selenium.common.exceptions import TimeoutException


links = ["http://www.tjmugh.com.cn/lcks/xynk/ysjs/index.shtml"]
y = 0
chrome_options = Options()
chrome_options.add_argument("--headless")

    #ㄦ外科


with open('tianjin2.csv', 'wb') as fp:
    fp.write(codecs.BOM_UTF8)
    spamwriter = csv.writer(fp,dialect='excel')
    for y in range(0,1):
        base_url = str(links[y])
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.set_page_load_timeout(7)
        driver.get(base_url)
        x = 0
        tmp = 'document.getElementsByTagName("a")'
        for x in range(67,73):
            print("x: ", x)
            if x%3 == 0:
                if (x < 100):
                    js = 'document.getElementsByTagName("a")['+str(x)+'].click()'#先确认你的标签绑定了点击事件
                    driver.execute_script(js)
                    time.sleep(1)
                    try:
                        tabs = driver.window_handles
                        driver.switch_to.window(tabs[1])
                        url = driver.current_url
                        fp.write(url.encode('utf-8')+','.encode('utf-8'))
                        print(url)
                    except TimeoutException as e:
                        print("Page load Timeout Occured. Quiting !!!")
                    
                    try:
                        response = requests.get(str(url), timeout = 20)
                        response.encoding = "gbk"
                        soup = BeautifulSoup(response.text, 'html.parser')
                        if soup.find("title") != None:
                            name = soup.find_all("div", class_="container")
                            intro = soup.find_all("div", class_="container")
                            if(len(name)>=3):
                                item = name[3].find("a")
                                fp.write(item.getText().encode('utf-8')+','.encode('utf-8'))
                                print("name: ",item.getText())
                                if intro[3].find("div", class_ = "span9") != None:
                                    item = intro[3].find("div", class_ = "span9").find("p")
                                    ID = item.getText()
                                    ID = ID.replace("\t", "").replace("\r", "").replace("\n", "").replace(",", " ") 
                                    fp.write(ID.encode('utf-8'))
                                    print("intro: ",ID)
                                    fp.write("\n".encode('utf-8'))
                        driver.close();
                        driver.switch_to.window(tabs[0]);
                    except requests.exceptions.Timeout:
                        print("Timeout occurred")
                    print("back")
            time.sleep(1)
    driver.close()

end_time=time.time()
print('this is end_time ',end_time)