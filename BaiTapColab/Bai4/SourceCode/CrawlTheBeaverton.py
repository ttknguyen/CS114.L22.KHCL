import requests
from bs4 import BeautifulSoup
def get_articles(year, page):
    url = 'https://www.thebeaverton.com/' + str(year) + '/page/' + str(page) + '/'
    request = requests.get(url)
    soupSite = BeautifulSoup(request.text, 'lxml')
    for article in soupSite.find_all('header', class_='post-title entry-header'):
        try:
            news = {
                "is_sarcastic": 1,
                "headline": article.h3.text,
                "article_link": article.h3.a.get("href")
            }
            articles.append(news)
        except:
            pass
articles = []
for year in range(2019, 2022):
    if year == 2019:
        for page in range(1,85):
            get_articles(year, page)
    elif year == 2020:
        for page in range(1,105):
            get_articles(year, page)
    elif year == 2021:
        for page in range(1, 48):
            get_articles(year, page)
print(len(articles))
for news in articles:
    print(news)
    
# xuất ra file json
file = 'TheBeaverton.json'
with open(file, "a") as f:
  for news in articles:
    f.write(str(news)+'\n')
f.close
