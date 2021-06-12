import requests
from bs4 import BeautifulSoup as Soup
from tqdm.notebook import tqdm #Progress bar
import json

def writeJson(data, fileName):
  with open(fileName+'.json', 'w') as f:
    for i in data:
      f.write('{"is_sarcastic": ' + str(i[2]) + ', "headline": "' + i[0] + '", "article_link": "' + i[1] +'"}\n')


data_nbc = []

month1 = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october','november','december',]

def SendRequest(year,month):
  temp = 0
  for i in range(1,3):
    if (i == 1):
      my_url = 'https://www.nbcnews.com/archive/articles/' + str(year) + '/' + month
      result = getData(my_url)
    else:
      my_url = 'https://www.nbcnews.com/archive/articles/' + str(year) + '/' + month + '/' + str(i)
      result = getData(my_url)
    temp += result
  return temp
  
def getData(my_url):
  count = 0
  uClient = requests.get(my_url)
  soupSite = Soup(uClient.text,'html.parser')
  containers = soupSite.findAll("main",{"class":"MonthPage"})
  container = containers[0].findAll("a")
  for i in range(0,len(container)):
    url = container[i].get('href')
    tilte = container[i].text
    data_nbc.append([tilte,url,0])
    count += 1
  return count
  
def crawlDataNBC():
  count = 0

  print("___ CRAWL DATA FROM NBC ___")
  for year in tqdm(range(2019, 2021), desc = 'year'):
    for m in month1:
      count += SendRequest(year,m)
  for m in range(5):
    count += SendRequest(2021,month1[m])
  
  print('Completed...')
  print("Crawled:", count , "ArticleLinks")
  
crawlDataNBC()
writeJson(data_nbc, 'NBCNews')
