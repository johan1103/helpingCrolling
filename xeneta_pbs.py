import requests
import json
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup as bs

urllist = ['asia-europe','pacific', 'trans-atlantic']
url = 'https://xsi-short.xeneta.com/xsic/chart/'




def FindCorridor() :
    cor = []
    for i in range(0,753): #Corridor range를 어디까지 해야 되는지?
        cor.append(corri)
    return cor


def FindOption(index) :
    Optvalue = []
    for j in range(0,len(index)) :
        for i in range(0,len(index[j]['rates'])):
            Optvalue.append(opt[j])
    return Optvalue

def FindDestination(index) :
    Dest = []
    for j in range(0,len(index)) :
        for i in range(0,len(index[j]['rates'])):
            Dest.append(index[j]['destination'])
    return Dest

def FindDate(index) :
    Date = [] 
    for j in range(0,len(index)) :
        for i in range(0,len(index[j]['rates'])): 
            Date.append(index[j]['rates'][i]['date'])
    return Date

def FindMean(index) :
    Mean = [] 
    for j in range(0,len(index)) :
        for i in range(0,len(index[j]['rates'])): 
            Mean.append(float(index[j]['rates'][i]['mean']))
    return Mean

Empty1 = []
Empty2 = []
Empty3 = []
Empty4 = []
Empty5 = []


# TODO req close 
for k in range(0,3) : 
    req = requests.get(url+urllist[k])
    print(url+urllist[k])
    soup = bs(req.text, 'html.parser')
    table = soup.find('canvas', {'class' : 'chart-visualization'})
    option_value = soup.find('div', {'class' : 'chart-controls'})

    lanes = eval(table.attrs['data-json'])['lanes']
    corri = eval(table.attrs['data-json'])['corridor']
    opt = option_value.select('option')


    Empty1.append(FindCorridor())
    Empty2.append(FindDestination(lanes))
    Empty3.append(FindOption(lanes))
    Empty4.append(FindDate(lanes))
    Empty5.append(FindMean(lanes))
    #     corridor = FindCorridor()
    # destination = FindDestination(lanes)
    # Ymd = FindDate(lanes)
    # rates = FindMean(lanes)
    # option = FindOption(lanes)
    # Contact = pd.concat([corridor,option,destination,Ymd,rates],axis = 1)



df1 = pd.DataFrame({'corridor' : Empty1})
df2 = pd.DataFrame({'option' : Empty3})
df3 = pd.DataFrame({'Destination' : Empty2})
df4 = pd.DataFrame({'Dates' : Empty4})
df5 = pd.DataFrame({'rate' : Empty5})
Contact = pd.concat([df1,df2,df3,df4,df5],axis = 1)
print(df2)
