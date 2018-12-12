import requests
from bs4 import BeautifulSoup
url = 'https://www.transfermarkt.com/stoke-city/startseite/verein/512/saison_id/2018'
res  = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
print(res.status_code)
soup = BeautifulSoup(res.content, 'lxml')

print(soup.select_one('html'))