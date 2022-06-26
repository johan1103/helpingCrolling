from email.mime import base
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from urllib.request import Request
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('C:\Windows\chromedriver', chrome_options=chrome_options)

driver.implicitly_wait(30)
driver.get('https://fbx.freightos.com/user/login')
login_x_path = '/html/body/div[17]/div/div/div[2]/form/input[2]'
driver.find_element_by_name('email').send_keys('<samuel.oh@simplogis.com>')
driver.find_element_by_name('password').send_keys('<SIMPlogis2018@1>')

url = 'https://datastudio.google.com/embed/batchedDataV2?appVersion=20220517_00020039'

ua = UserAgent()
header = {
    'User-Agent' : ua.random,
    'referer' : 'https://datastudio.google.com/embed/reporting/0af48630-1525-4260-a83f-326113065bca/page/p_p9kkzbpync',
    'content-type' : 'application/json',        
    'origin' : 'https://datastudio.google.com',
    'Accept' : 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br'
}

response = requests.post(url, headers=header)
print(response.status_code)