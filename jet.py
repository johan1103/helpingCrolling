<<<<<<< Updated upstream
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from datetime import datetime
from fake_useragent import UserAgent

def JET():
    columns = []
    CountryList = []
    bbllist = []
    MTlist = []
    gallonlist = []
    literlist = []

    ua = UserAgent()
    url = 'https://jet-a1-fuel.com/'
    headers = {'User-Agent' : ua.random}

    req  = requests.get(url, headers=headers)
    soup = bs(req.text, 'html.parser')
    table = soup.find('table',{'class' : 'table table-striped'})
    tde = table.find_all('td')

    #Dataframe의 columns
    for i in range(0,5):
        tre = table.find_all('th')[i].text
        columns.append(tre)
    print("len tde ")
    print(len(tde))
    for j in range(0,len(tde)) :
        if j%5 == 0 :
            CountryList.append(table.find_all('a')[int(j/5)].text)
        elif j%5 == 1 :
            bbllist.append(table.find_all('td')[j].text)
        elif j%5 == 2 :
            MTlist.append(table.find_all('td')[j].text)
        elif j%5 == 3 :
            gallonlist.append(table.find_all('td')[j].text)
        elif j%5 == 4 :
            literlist.append(table.find_all('td')[j].text)

    CountryDF = pd.DataFrame(CountryList)
    bblDF = pd.DataFrame(bbllist)
    MTDF = pd.DataFrame(MTlist)
    gallonDF = pd.DataFrame(gallonlist)
    literDF = pd.DataFrame(literlist)

    Contact = pd.concat([CountryDF, bblDF, MTDF, gallonDF, literDF],axis = 1)
    Contact.columns = [columns]
<<<<<<< HEAD
    Contact.to_csv(f"./{datetime.today().date().strftime('%Y-%m-%d')}_JET.csv", index=False)
<<<<<<< HEAD
=======
=======
>>>>>>> Stashed changes
>>>>>>> main
=======
    Contact.to_csv(f"./{datetime.today().date().strftime('%Y-%m-%d')}_JET.csv", index=False)
>>>>>>> main
