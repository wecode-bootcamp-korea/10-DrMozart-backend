from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import csv
import sys
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("headless")
chrome_option.add_argument("-disable-gpu")
chrome_option.add_argument("lang-=ko_KR")
​
​
driver = webdriver.Chrome("/home/dh/Downloads/chromedriver",chrome_options=chrome_option)
driver.get('https://www.drjart.com/ko/prd/all')
​
body = driver.find_element_by_css_selector('body')
​
plus_btn = driver.find_elements_by_id('prd_more_btn')
​
data_list = []
plus_btn_count = 0
while plus_btn_count < 10:    
    try:
        plus_btn_count+=1
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)
        plus_btn = driver.find_elements_by_id('prd_more_btn')
        plus_btn[0].click()
        time.sleep(0.3)
        body.send_keys(Keys.PAGE_DOWN)
    except Exception:
        html = driver.page_source
        bs = BeautifulSoup(html, 'html.parser')
    finally:
        html = driver.page_source
        bs = BeautifulSoup(html, 'html.parser')
​
# 전체 상품 목록 가져오기 (해당 로직 복사해서 카테고리벼로 지정)
info_box = bs.find_all("div",{"class":"pdtWrap"})
for info in info_box[:-4]:
    sale = str()
    gift = str()
    best = str()
    new = str()
    title = info.find("p",{"class":"opt_tit"}).text
    tag = info.find("p",{"class":"opt_msg"}).text
    image_url = info.find("span",{"class":"opt_thumb"}).find("img")["src"]
    flags = info.find_all("div",{"class":"opt_flag"})
    for flag in flags:
        if flag.find("span",{"class":"sale"}) == None:
            sale = None
        else:
            sale = flag.find("span",{"class":"sale"}).text
        if flag.find("span",{"class":"gift"}) == None:
            gift = None
        else:
            gift = flag.find("span",{"class":"gift"}).text
        if flag.find("span",{"class":"best"}) == None:
            best = None
        else:
            best = flag.find("span",{"class":"best"}).text
        if flag.find("span",{"class":"new"}) == None:
            new = None
        else:
            new = flag.find("span",{"class":"new"}).text
    
    data_list.append({"title":title,"tag":tag,"image_url":image_url,"sale":sale,"gift":gift,"best":best,"new":new})
​
# 해당 파일을 csv파일로 만들기
print(data_list)