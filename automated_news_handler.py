from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

application_path = 'C:/Users/Aymen/Desktop/personal_project/news-automation/'
print(application_path)

now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

print(now,'='*10,month_day_year)


web = 'https://www.thesun.co.uk/sport/football/'
path = 'C:/Users/Aymen/Desktop/personal_project/news-automation/chromedriver.exe'

options = Options() # options for our web driver
options.headless = True # headless mode

# Headless testing is simply running your Selenium tests using a headless browser. It operates as your typical browser would,
# but without a user interface, making it excellent for automated testing.


driver_service = Service(executable_path=path) 
driver = webdriver.Chrome(service=driver_service, options=options)
driver.get(web)


containers = driver.find_elements(by='xpath', value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

print(containers,"="*20)

for container in containers:
    print(container)
    title = container.find_element(by='xpath', value='./a/h2').text
    subtitle = container.find_element(by='xpath', value='./a/p').text
    link = container.find_element(by='xpath', value='./a').get_attribute('href')
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)


my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
file_name = f'football_headlines_{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)
df_headlines.to_csv(final_path)

driver.quit()