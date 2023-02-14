import json
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

allProductLinks=[]

websiteList=[
    'https://www.chewy.com/b/wet-food-293/'
]

# driver=webdriver.Chrome('chromedriver.exe')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

website=websiteList[0]

driver.get(website)
res=driver.page_source
soup1=BeautifulSoup(res,'lxml')

res3=driver.page_source
soup3=BeautifulSoup(res3,'lxml')
containers=soup3.find_all(attrs={"data-list":"browse"})
driver.close()

v = 1
for v in range(3):
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    vall = v + 1
    websiteList = "https://www.chewy.com/b/wet-food_c293_p"+str(vall)
    browser.get(websiteList)
    print("new page")
    print(vall)
    print(websiteList)

    for x in containers:
        name=x.find('div',class_='kib-product-title__text').text
        print(name)
        url=x.find('h2',class_='ProductListing_plpProductCardTitleWrapper__YehIF').a["href"]
        print(url)
        product={
            'productName':name,
            'url':url,
        }
        allProductLinks.append(product)



f=open('links.json','w')
f.write(json.dumps(allProductLinks, indent=4))

# os.system('wet-food-293.py')

