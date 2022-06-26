import requests
import json
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup as bs

urllist = ['asia-europe','pacific', 'trans-atlantic']
url = 'https://xsi-short.xeneta.com/xsic/chart/'

def FindCorridor() :
    for j in range(0,len(lanes)) :
        for i in range(0,len(lanes[j]['rates'])): #Corridor range를 어디까지 해야 되는지?
            Corridor.append(corri)     
    return Corridor


def FindOption(index) :
    for j in range(0,len(index)) :
        for i in range(0,len(index[j]['rates'])):
            Option.append(opt[j].text)
    return Option

def FindDestination(index) :
    for j in range(0,len(index)) :
        for i in range(0,len(index[j]['rates'])):
            Destination.append(index[j]['destination'])
    return Destination

def FindDate(index) :
    for j in range(0,len(index)) :
        for i in range(0,len(index[j]['rates'])): 
            Date.append(index[j]['rates'][i]['date'])
    return Date

def FindMean(index) :
    for j in range(0,len(index)) :
        for i in range(0,len(index[j]['rates'])): 
            Mean.append(float(index[j]['rates'][i]['mean']))
    return Mean

Corridor = []
Option = []
Destination = []
Date = []
Mean = []


# TODO req close 
for k in range(0,3) : 
    req = requests.get(url+urllist[k])
    soup = bs(req.text, 'html.parser')
    table = soup.find('canvas', {'class' : 'chart-visualization'})
    option_value = soup.find('div', {'class' : 'chart-controls'})

    lanes = eval(table.attrs['data-json'])['lanes']
    corri = eval(table.attrs['data-json'])['corridor']
    opt = option_value.select('option')


    Corridor.append(FindCorridor())
    Option.append(FindOption(lanes))
    Destination.append(FindDestination(lanes))
    Date.append(FindDate(lanes))
    Mean.append(FindMean(lanes))


df1 = pd.DataFrame({'corridor' : Corridor})
df2 = pd.DataFrame({'option' : Option})
df3 = pd.DataFrame({'Destination' : Destination})
df4 = pd.DataFrame({'Dates' : Date})
df5 = pd.DataFrame({'rate' : Mean})
Contact = pd.concat([df1,df2,df3,df4,df5],axis = 1)
print(Corridor)
# Contact.to_csv('D:\python'+'xenata.csv')