import requests
from bs4 import BeautifulSoup
import sqlite3

# URL = 'https://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1'  # >> 영국 1
# URL = 'https://www.transfermarkt.com/championship/startseite/wettbewerb/GB2'  # >> 영국 2
# URL = 'https://www.transfermarkt.com/1-bundesliga/startseite/wettbewerb/L1'  # >> 독일 1
# URL = 'https://www.transfermarkt.com/primera-division/startseite/wettbewerb/ES1'  # >> 스페인 1
# URL = 'https://www.transfermarkt.com/serie-a/startseite/wettbewerb/IT1'  # >> 이탈리아 1
# URL = 'https://www.transfermarkt.com/ligue-1/startseite/wettbewerb/FR1'  # >> 프랑스 1
# URL = 'https://www.transfermarkt.com/eredivisie/startseite/wettbewerb/NL1'  # >> 네덜란드 1


# URL = ''
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


# html = requests.get(URL, headers=headers).text
# soup = BeautifulSoup(html, 'html.parser')


'''
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
'''

# URL = 'https://www.transfermarkt.com/manchester-city/startseite/verein/281/saison_id/2019'
# URL = 'https://www.transfermarkt.com/fc-liverpool/startseite/verein/31/saison_id/2019'
# URL = 'https://www.transfermarkt.com/fc-chelsea/startseite/verein/631/saison_id/2019'
# URL = 'https://www.transfermarkt.com/tottenham-hotspur/startseite/verein/148/saison_id/2019'
# URL = 'https://www.transfermarkt.com/manchester-united/startseite/verein/985/saison_id/2019'
# URL = 'https://www.transfermarkt.com/fc-arsenal/startseite/verein/11/saison_id/2019'
# URL = 'https://www.transfermarkt.com/leicester-city/startseite/verein/1003/saison_id/2019'
# URL = 'https://www.transfermarkt.com/fc-everton/startseite/verein/29/saison_id/2019'
# URL = 'https://www.transfermarkt.com/wolverhampton-wanderers/startseite/verein/543/saison_id/2019'
# URL = 'https://www.transfermarkt.com/west-ham-united/startseite/verein/379/saison_id/2019'
# URL = 'https://www.transfermarkt.com/afc-bournemouth/startseite/verein/989/saison_id/2019'
# URL = 'https://www.transfermarkt.com/newcastle-united/startseite/verein/762/saison_id/2019'
# URL = 'https://www.transfermarkt.com/aston-villa/startseite/verein/405/saison_id/2019'
# URL = 'https://www.transfermarkt.com/brighton-amp-hove-albion/startseite/verein/1237/saison_id/2019'
# URL = 'https://www.transfermarkt.com/fc-watford/startseite/verein/1010/saison_id/2019'
# URL = 'https://www.transfermarkt.com/fc-southampton/startseite/verein/180/saison_id/2019'
# URL = 'https://www.transfermarkt.com/crystal-palace/startseite/verein/873/saison_id/2019'
# URL = 'https://www.transfermarkt.com/fc-burnley/startseite/verein/1132/saison_id/2019'
# URL = 'https://www.transfermarkt.com/norwich-city/startseite/verein/1123/saison_id/2019'
# URL = 'https://www.transfermarkt.com/sheffield-united/startseite/verein/350/saison_id/2019'
# URL=''
# URL=''
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


html = requests.get(URL, headers=headers).text
soup = BeautifulSoup(html, 'html.parser')


Team_soup = soup.find(
    "h1", {"itemprop": 'name'})
Team_name = Team_soup.text.strip()


Player_list = []
Player_soup = soup.find_all(
    "span", {"class": 'hide-for-small'})
for Player in Player_soup:
    Player_list.append(Player.text)
T = '!'.join(Player_list)
Player_list = T.split("!!")
T = '!'.join(Player_list)
Player_list = T.split("!")
if Player_list[0] == '':
    Player_list.pop(0)

Player_num_list = []
Player_num_soup = soup.find_all(
    "div", {"class": 'rn_nummer'})
for Player_num in Player_num_soup:
    Player_num_list.append(Player_num.text)
T = '-'.join(Player_num_list)
Player_num_list = T.split("--")
T = '-'.join(Player_num_list)
Player_num_list = T.split("-")

Player_soup_list1 = []
Player_pos_list = []
Player_pos_soup = soup.find_all("tr")
for Player_pos in Player_pos_soup:
    Player_soup_list1.append(Player_pos.text)
for i in range(len(Player_soup_list1)):
    if i % 6 == 4:
        Player_pos_list.append(Player_soup_list1[i])
    if i % 6 == 1:
        Player_pos_list.append(Player_soup_list1[i])
a = len(Player_list)+1
Player_pos_list = Player_pos_list[1:a]

Player_soup_list2 = []
Player_age_list = []
Player_age_soup = soup.find_all(
    "td", {"class": 'zentriert'})
for Player_age in Player_age_soup:
    Player_soup_list2.append(Player_age.text)

for i in range(len(Player_soup_list2)):
    if i % 3 == 1:
        Player_age_list.append(Player_soup_list2[i])
a = len(Player_list)
Player_age_list = Player_age_list[0:a]

Player_value_list = []
Player_value_soup = soup.find_all(
    "td", {"class": 'rechts hauptlink'})
for Player_value in Player_value_soup:
    Player_value_list.append(Player_value.text)
T = ''.join(Player_value_list)
Player_value_list = T.split("\xa0")
T = '!'.join(Player_value_list)
T = T.replace("!!!!", "!!!!!!")
Player_value_list = T.split("!!")
T = '!'.join(Player_value_list)
Player_value_list = T.split("!")
Player_value_list.pop(-1)


db = sqlite3.connect("DB/FO_datafile.db")
cursor = db.cursor()
for i in range(len(Player_list)):
    insert_query = \
        f'INSERT INTO Players VALUES("{Player_list[i]}","{Team_name}", "{Player_num_list[i]}", "{Player_pos_list[i]}","{Player_age_list[i]}", "{Player_value_list[i]}")'
    cursor.execute(insert_query)
    db.commit()
