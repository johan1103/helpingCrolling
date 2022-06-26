from asyncio.windows_events import NULL
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import pandas as pd
import json
from selenium import webdriver

    #for문을 Simple이란 함수로 정의 하여 모든 data를 dataframe으로 가공
def Simple(Country):
    value = [] #value 값을 넣어줄 빈 value 배열 선언
    for j in range(1, len(Country)):
        if isinstance(Country[j][1], dict): #만약 dictionary 형태이면 value 값만 추출해서 value라는 배열에 append
            value.append(Country[j][1]['value'])
            continue
        value.append(Country[j][1]) #만약 dictionary 형태가 아니고 (int형이면) 그냥 그 값 그대로 value 라는 배열에 append
    df = pd.DataFrame({'value': value}) #datafrmae 생성 value 가 key 값
    return df


#for문을 통해 날짜값을 하나만 넣어주기로 선언
def findDate(Country):
        date = [] #날짜값을 넣어줄 빈 date 배열 선언
        for i in range(1,len(Country)):
            date.append(Country[i][0])
        df = pd.DataFrame({'Date' : date}) #datafrmae 생성 date 가 key 값

        return df


def wci() :
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",["enable-logging"])
    browser= webdriver.Chrome(options=options)
    browser.get('https://infogram.com/world-container-index-1h17493095xl4zj')

    #data 0 ~ 7까지를 전부 all_composit이란 변수에 대입
    all_composite = browser.execute_script('return window.infographicData.elements[2].data;')

    #Name 이라는 변수에 나라 이름 대입
    Name = browser.execute_script('return window.infographicData.elements[2].sheetnames;')
    #dataframe의 1열의 값은 날짜 이므로 0번째 인덱스에 Date라는 이름을 집어넣고 나머지는 한칸 씩 뒤로 미룬다.
    Name.insert(0,'Date')

    Contact = findDate(all_composite[0]) #모든 date는 같으므로 data[0]에 있는 date만 집어넣어서 출력 할 예정.

    #all_composite 만큼 for문을 돌려서 value 값을 column 기준으로 병합 시킴
    for cps in all_composite :
        Contact = pd.concat([Contact,Simple(cps)],axis=1)

    #dataframe columns 재설정
    Contact.columns = [Name]
    Contact.to_csv('./' +'wci.csv', index=False)

