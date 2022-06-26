import enum
import requests
import json
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from datetime import date, datetime
import re
import numpy as np

crawl_url = 'https://infogram.com/world-container-index-1h17493095xl4zj'

ua = UserAgent()
header = {'User-Agent': ua.random}
response = requests.get(crawl_url, headers=header)
soup = bs(response.text, 'html.parser')

cnt = 0 #Script 를 크롤링 하는 방법, tag에 script 를 전부 대입 하면 7번째에 나타남. json 으로 변환을 위해 slicing 진행.
for tag in soup.select('script'):
    if cnt == 7:
        json_data = json.loads(str(tag.contents[0])[23:len(tag.contents[0])-1])
    cnt += 1

data = json_data['elements'][2]['data'] #데이터 부분, 날짜와 값 둘 다 존재
name = json_data['elements'][2]['sheetnames'] #나라이름
lower_name= []

for index in range(0,len(name)) :
    lower_name.append(str.lower(name[index]))


lower_name[0] = 'composite_index'

dictionary = {"dates" : []}

for n in lower_name:
    dictionary[f'{n}'] = []



cnt = 0
for index, value in enumerate(data):
    ptr = 1
    for r, row in enumerate(value) :
        for c, col in enumerate(row) :
            #print(c)
            # c = 0 이면 날짜, c = 1이면 값
            if c == 0 and len(data[index][r][c]) > 0: # date 형식 바꿔주는 코드 부분
                if " " in data[index][r][c] :
                    data[index][r][c] = data[index][r][c].replace(" ","")
                elif len(data[index][r][c]) >= 10 :
                    data[index][r][c] = datetime.strptime(data[index][r][c], '%d-%B-%y').date()
                else: #0번째 list는 ['', 'composite'] 로 되어 있어서 예외 처리가 필요함.
                    data[index][r][c] = datetime.strptime(data[index][r][c], '%d-%b-%y').date()    
            if c == 1 : #dict 형태이면 key 값을 통해서 추출
                if isinstance(data[index][r][c], dict) :
                    data[index][r][c] = data[index][r][c]['value']

        # r = 0 이면 ['', 'composite'] 이렇게 되어 있는 형태여서 필요 없는 부분
        if  r != 0: # 따라서 r = 0이 아닐때만 비교
            #index가 변하게 해주면서 dictionary의 key값에 접근하여 value 대입.
            if index == 0 :
                dictionary["dates"].append(data[index][r][0])
                dictionary["composite_index"].append(data[index][r][1])
                #print(data[index][r][0])
                #print(data[index][r][1])
            elif index == 1 :
                dictionary["shanghai - rotterdam"].append(data[index][r][1])
            elif index == 2 :
                dictionary["rotterdam - shanghai"].append(data[index][r][1])
            elif index == 3 :
                dictionary["shanghai - los angeles"].append(data[index][r][1])
            elif index == 4 :
                while data[0][ptr][0]!=data[index][r][0]:
                        dictionary["los angeles - shanghai"].append("NULL")
                        ptr+=1
                dictionary["los angeles - shanghai"].append(data[index][r][1])
                ptr=ptr+1
            elif index == 5 :
                dictionary["shanghai - genoa"].append(data[index][r][1])
            elif index == 6 :
                dictionary["new york - rotterdam"].append(data[index][r][1])
            elif index == 7 :
                dictionary["rotterdam - new york"].append(data[index][r][1])
# data[4][r][0] index가 4일때의 날짜 부분 출력, r 값은 for 문 통해서 데이터 4의 길이만 큼 돌려야 댐 data[4]의 길이는 324
# 다만 data[0][r][0] index가 0일 때 날짜 부분 출력, 마찬가지로 r 값을 for 문 통해서 돌려야 댐 data[0]의 길이는 325
# data[4][r][0] 은 data[4]의 날짜 부분
# data[4][r][1] 은 data[4]의 value 부분
# data[4][r][0] & data[0][r][0] 을 실제로 일일이 눈으로 비교 해봤을때 22년도 2월 17일 날짜와 값이 비어있음 그래서 이값을 null 값으로 대입해야댐.