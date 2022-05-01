import requests
import json
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup as bs

mainUrl = "https://xsi.xeneta.com/"
mainReq = requests.get(mainUrl)
mainSoup = bs(mainReq.text,'html.parser')
mainTable = mainSoup.find_all('iframe')
for i in range(1,len(mainTable)-1):
    print(mainTable[i]['src'])

url = 'https://xsi-short.xeneta.com/xsic/chart/pacific'

req = requests.get(url)
soup = bs(req.text, 'html.parser')
table = soup.find('canvas',{'class' : 'chart-visualization'})
option_value = soup.find('div', {'class' : 'chart-controls'})

lanes = eval(table.attrs['data-json'])['lanes']
corri = eval(table.attrs['data-json'])['corridor']
dest = eval(table.attrs['data-json'])['lanes'][0]['destination']
opt = option_value.select('option')[0].text

def FindCorridor(index) :
    cor = []
    for i in range(0,len(index[0]['rates'])):
        cor.append(corri)
        df = pd.DataFrame({'corridor' : cor})
    return df

def FindOption(index) :
    Optvalue = []
    for i in range(0,len(index[0]['rates'])):
        Optvalue.append(opt)
        df = pd.DataFrame({'option' : Optvalue})
    return df

def FindDestination(index) :
    Dest = []
    for i in range(0,len(index[0]['rates'])):
        Dest.append(dest)
        df = pd.DataFrame({'Destination' : Dest})
    return df

def FindDate(index) :
    Date = [] 
    for i in range(0,len(index[0]['rates'])): 
        Date.append(index[0]['rates'][i]['date'])
        df = pd.DataFrame({'Dates' : Date})
    return df

def FindMean(index) :
    Mean = [] 
    for i in range(0,len(index[0]['rates'])): 
        Mean.append(float(index[0]['rates'][i]['mean']))
        df = pd.DataFrame({'rate' : Mean})
    return df

corridor = FindCorridor(lanes)
destination = FindDestination(lanes)
Ymd = FindDate(lanes)
rates = FindMean(lanes)
option = FindOption(lanes)
Contact = pd.concat([corridor,option,destination,Ymd,rates],axis = 1)

print(Contact)