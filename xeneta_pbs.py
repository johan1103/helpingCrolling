import requests
import json
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup as bs


url = 'https://xsi-short.xeneta.com/xsic/chart/trans-atlantic'

# TODO req close 
req = requests.get(url)
soup = bs(req.text, 'html.parser')
table = soup.find('canvas', {'class' : 'chart-visualization'})
option_value = soup.find('div', {'class' : 'chart-controls'})

lanes = eval(table.attrs['data-json'])['lanes']
corri = eval(table.attrs['data-json'])['corridor']
opt = option_value.select('option')


def FindCorridor() :
    cor = []
    for i in range(0,753): #Corridor range를 어디까지 해야 되는지?
        cor.append(corri)
        df = pd.DataFrame({'corridor' : cor})
    return df


def FindOption(index) :
    Optvalue = []
    for j in range(0,len(index)) :
        for i in range(0,len(index[j]['rates'])):
            Optvalue.append(opt[j])
            df = pd.DataFrame({'option' : Optvalue})
    return df

def FindDestination(index) :
    Dest = []
    for j in range(0,len(index)) :
        for i in range(0,len(index[j]['rates'])):
            Dest.append(index[j]['destination'])
            df = pd.DataFrame({'Destination' : Dest})
    return df

def FindDate(index) :
    Date = [] 
    for j in range(0,len(index)) :
        for i in range(0,len(index[j]['rates'])): 
            Date.append(index[j]['rates'][i]['date'])
            df = pd.DataFrame({'Dates' : Date})
    return df

def FindMean(index) :
    Mean = [] 
    for j in range(0,len(index)) :
        for i in range(0,len(index[j]['rates'])): 
            Mean.append(float(index[j]['rates'][i]['mean']))
            df = pd.DataFrame({'rate' : Mean})
    return df

corridor = FindCorridor()
destination = FindDestination(lanes)
Ymd = FindDate(lanes)
rates = FindMean(lanes)
option = FindOption(lanes)
Contact = pd.concat([corridor,option,destination,Ymd,rates],axis = 1)

print(Contact)

