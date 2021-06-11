import requests
from   bs4 import BeautifulSoup as Soup
from tqdm.notebook import tqdm

def sendRequestTS(page):
  url = 'https://www.thesun.co.uk/news/uknews//page/' + str(page)
  headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
  request = requests.get(url, headers = headers)
  soupSite = Soup(request.text, 'html')
  return soupSite
  
def getDataTS(soupSite, data):
  count = 0
  for s in soupSite:
    ArticleLink = s.a['href']
    Title = s.p.text.replace('\n', "").replace('\t', "")
    data.append([Title, ArticleLink, 0])
    count += 1
  return count
  
def crawlDataTheSun():
  dataTS = []
  count = 0

  print("___ CRAWL DATA FROM THE SUN ___")
  for page in tqdm(range(1, 1500)):
    soupSite = sendRequestTS(page).find_all("div", class_="teaser__copy-container")
    count += getDataTS(soupSite, dataTS)
  toCsv(dataTS, 'TheSun.csv')

  print('Completed...')
  print("Crawled:", count, "ArticleLinks")	

crawlDataTheSun()
