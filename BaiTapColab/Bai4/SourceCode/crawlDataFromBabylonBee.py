import requests
from bs4 import BeautifulSoup as Soup
from tqdm.notebook import tqdm

# Dùng để gửi request đến trang web với tham số là số thứ tự trang cần thu thập
def sendRequest(page):
  #Tạo đường liên kết đến trang cần thu thập dữ liệu
  url = "https://babylonbee.com/news?page=" + str(page)
  #Gửi request đến trang đó
  request = requests.get(url)
  #BeautifulSoup dùng để phân tích dữ liệu html thành dữ liệu cây để chúng ta dễ dàng thao tác sau này
  soupSite = Soup(request.text, 'html.parser')
  return soupSite
  
def getData(soupSite, data):
  count = 0
  for soup in soupSite:
    soup = str(soup)

    #check Time
    a = soup.find(':published_on=')
    b = soup.find('\'" ', a, len(soup))
    if (2019 <= int(soup[b-4:b])):
      # Lấy link
      posArticleLinkStart = soup.find(":path")
      posArticleLinkEnd = soup.find('\'" ', posArticleLinkStart, len(soup))
      ArticleLink ="https://babylonbee.com/" +  soup[posArticleLinkStart+8:posArticleLinkEnd]

      # Lấy Title
      posTitleStart = soup.find(':title=') + 8 
      posTitleEnd = soup.find('>', posTitleStart, len(soup))
      Title = soup[posTitleStart:posTitleEnd].replace("&quot;", "").replace("'","").replace('"', '')

      #Thêm phần vừa get được vào data chính
      data.append([Title, ArticleLink, 1])
      count += 1
  return count
  
def toCsv(data):
  f = open('BabylonBee.csv', mode = 'w', encoding='utf-8')
  for i in data:
    f.write('"' + i[0] + '", "' + i[1] + '", ' + str(i[2]) + "\n")
  f.close()
  
def crawlDataBabylonBee():
  data = []
  count = 0

  print("___ CRAWL DATA FROM BABYLON BEE ___")
  for page in tqdm(range(1, 355)):
    soupSite = sendRequest(page).find_all("article-card")
    count += getData(soupSite, data)
  toCsv(data)

  print('Completed...')
  print("Crawled:", count, "ArticleLinks")

crawlDataBabylonBee()
