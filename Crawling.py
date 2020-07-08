import requests
from bs4 import BeautifulSoup

URL = 'https://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


html = requests.get(URL, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')
Team_Table = soup.find_all("table", {"class": 'items'})
print(Team_list)
