#Ignis Tech Solutions Task
#Name: Daniel E Adama
#site to scrape for "D": https://www.midwayusa.com/

#import relevant libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd


data = []

#list of urls to scrape
urls = ['https://www.midwayusa.com/product/1018227839',
        'https://www.midwayusa.com/product/1301776634',
        'https://www.midwayusa.com/product/1021313398',
        'https://www.midwayusa.com/product/1021070320?pid=806816']
#loop through each url
for url in urls:
    #obtain the html response
    response = requests.get(url)
    #create beautifulsoup object
    soup = BeautifulSoup(response.text,'lxml')
    
    #store the product title, supplier name, stock status
    #and hyperlink in data
    data.append([soup.title.get_text().strip(), 
                 soup.select_one('span[class*=only]').get_text()[:9],
                soup.select_one('span[ng-bind*=selector]').text,
                 url])

data_scrapped= pd.DataFrame(data, columns=['Product_Title',
                                           'Supplier_Name',
                                           'Stock_Status',
                                           'Hyperlink_product'])
data_scrapped
data_scrapped.to_csv('Daniel E Adama output_task.csv')
