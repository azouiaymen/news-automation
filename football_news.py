from importlib.resources import path
from multiprocessing.sharedctypes import Value
import pandas as pd 
from datetime import datetime
import os,sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

now = datetime.now()

web = 'https://www.thesun.co.uk/sport/football/'
path = 'C:/Users/Aymen/Desktop/personal_project/news-automation/chromedriver.exe'

options = Options()
options.headless = True 

driver_service = Service(executable_path=path)
driver = webdriver.Chrome(service=driver_service,options=options)
driver.get(web)

containers = driver.find_elements(by='xpath',value='//div[@class="teaser__copy-container"]')

title = []
sub_titles = []
link = []

for container in containers:
    title.append(container.find_element(by='xpath',value = './a/h2').text)
    sub_titles.append(container.find_element(by='xpath',value = './a/p').text)
    link.append(container.find_element(by='xpath',value = './a').get_attribute('href'))


result = {'title': title, 'sub_titles' : sub_titles, 'links': link}
df = pd.DataFrame(result)


today = now.strftime('%d%m%Y')
final_path = os.path.join('C:/Users/Aymen/Desktop/personal_project/news-automation/',f'football_news_{today}.csv')
df.to_csv(final_path)






