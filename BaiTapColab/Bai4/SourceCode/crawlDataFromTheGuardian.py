import requests
from bs4 import BeautifulSoup

def sendRequestTG(year, month, date):
  url = "https://www.theguardian.com/tone/editorials/" + str(year) + "/" + str(month) + "/" + str(date) + "/all"
  rq = requests.get(url)
  soupSite = BeautifulSoup(rq.text, 'html.parser')
  return soupSite
  
def getDataTG(soupSite, data):
  count = 0
  for soup in soupSite:
    ArticleLink = soup.get('href')
    Title = soup.text.replace('\n', "")
    data.append([Title, ArticleLink, 0])
    count += 1
  return count
  
def toCsvTG(data):
  f = open('TheGuardian.csv', mode = 'w', encoding='utf-8')
  for i in data:
    f.write('"' + i[0] + '", "' + i[1] + '", ' + str(i[2]) + "\n")
  f.close()
  
month = {
    'jan': 31,
    'feb': 28,
    'mar': 31,
    'apr': 30,
    'may': 31,
    'jun': 30,
    'jul': 31,
    'aug': 31,
    'sep': 30,
    'oct': 31,
    'nov': 30,
    'dec': 31
}

from tqdm.notebook import tqdm

def crawlDataTheGuardian():
  dataTG = []
  count = 0

  print("___ CRAWL DATA FROM THE GUARDIAN ___")

  for year in tqdm(range(2019, 2021), desc = 'year'):
    for m in month:
      for d in tqdm(range(month[m]), desc='Crawl month  ' + m):
        soupSite = sendRequestTG(year, m, d)
        count += getDataTG(soupSite.find_all("a", class_="fc-item__link" ), dataTG)

  toCsv(data)
  print('Completed...')
  print("Crawled:", count, "ArticleLinks")
  
crawlDataTheGuardian()
