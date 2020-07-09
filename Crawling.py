import requests
from bs4 import BeautifulSoup
import sqlite3
# URL = ''
# URL = 'https://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1'  # >> 영국 1
# URL = 'https://www.transfermarkt.com/championship/startseite/wettbewerb/GB2'  # >> 영국 2
# URL = 'https://www.transfermarkt.com/1-bundesliga/startseite/wettbewerb/L1'  # >> 독일 1
# URL = 'https://www.transfermarkt.com/primera-division/startseite/wettbewerb/ES1'  # >> 스페인 1
# URL = 'https://www.transfermarkt.com/serie-a/startseite/wettbewerb/IT1'  # >> 이탈리아 1
# URL = 'https://www.transfermarkt.com/ligue-1/startseite/wettbewerb/FR1'  # >> 프랑스 1
URL = 'https://www.transfermarkt.com/eredivisie/startseite/wettbewerb/NL1'  # >> 네덜란드 1
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


html = requests.get(URL, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')

League_soup = soup.find(
    "h1", {"class": 'spielername-profil'})
League_name = League_soup.text

Team_list = []
Team_soup = soup.find_all(
    "td", {"class": 'hauptlink no-border-links show-for-small show-for-pad'})
for Team in Team_soup:
    Team_list.append(Team.text)


Team_value_list = []
Team_value_soup = soup.find_all(
    "td", {"class": 'rechts hide-for-small hide-for-pad'})
i = 0
for Team_value in Team_value_soup[2:]:
    i = i + 1
    if i % 2 == 0:
        continue
    Team_value_list.append(Team_value.text)

Team_age_list = []
Team_age_soup = soup.find_all(
    "td", {"class": 'zentriert'})
i = 0
for Team_age in Team_age_soup[4:]:
    i = i + 1
    if i % 4 == 2:
        Team_age_list.append(Team_age.text)

db = sqlite3.connect("DB/FO_datafile.db")
cursor = db.cursor()
for i in range(len(Team_list)):
    insert_query = \
        f'INSERT INTO Teams VALUES("{League_name}", "{Team_list[i]}", "{Team_value_list[i]}", "{Team_age_list[i]}")'
    cursor.execute(insert_query)
    db.commit()
