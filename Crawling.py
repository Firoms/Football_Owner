import requests
from bs4 import BeautifulSoup
import sqlite3
###########################################################################################################
# 리그 가져오기
###########################################################################################################


def Get_Leauge():
    Base_URLs = []
    Con_URLs = []
    Country = []
    Country_list = []
    League_list = []
    Clubs_list = []
    League_value_list = []

    continents = ['europa', 'europa/wettbewerbe?ajax=yw1&page=2', 'europa/wettbewerbe?ajax=yw1&page=3', 'europa/wettbewerbe?ajax=yw1&page=4',
                  'asien', 'asienn/wettbewerbe?ajax=yw1&page=2', 'amerika', 'afrika']
    for continent in continents:
        Con_URLs.append(
            f'https://www.transfermarkt.com/wettbewerbe/{continent}')

    URLs = []
    First_URL = 'https://www.transfermarkt.com'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    for Con_URL in Con_URLs:
        Con_html = requests.get(Con_URL, headers=headers).text
        Con_soup = BeautifulSoup(Con_html, 'html.parser')
        for href in Con_soup.find_all("table", {"class": 'inline-table'}):
            Team_URL = href.find_all("a")[1]["href"]
            if Team_URL == "/nedbank-cup/startseite/wettbewerb/NEDC":
                break
            if Team_URL == "/campeonato-brasileiro-serie-b/startseite/wettbewerb/BRA2":
                break
            if Team_URL == "/k3-league/startseite/wettbewerb/K3L":
                break
            if Team_URL == "/3-liga/startseite/wettbewerb/L3":
                break
            Base_URLs.append(First_URL+Team_URL)
            print(Team_URL)
    i = 0
    for Con_URL2 in Con_URLs:
        Con_html2 = requests.get(Con_URL2, headers=headers).text
        Con_soup2 = BeautifulSoup(Con_html2, 'html.parser')
        for alt in Con_soup2.find_all("td", {"class": 'zentriert'}):
            i = i + 1
            if i % 6 == 1:
                find_country = alt.find("img")["title"]
                Country_list.append(find_country)
                print(find_country)
            if i % 6 == 2:
                Clubs_list.append(alt.text)
                print(alt.text)
            if i % 6 == 0:
                League_value_list.append(alt.text)

    for Base_URL in Base_URLs:
        Base_html = requests.get(Base_URL, headers=headers).text
        Base_soup = BeautifulSoup(Base_html, 'html.parser')

        League_soup = Base_soup.find(
            "h1", {"class": 'spielername-profil'})
        try:
            League_list.append(League_soup.text)
            print(League_soup.text)
        except:
            pass

    print("DB")
    db = sqlite3.connect("DB/FO_datafile.db")
    cursor = db.cursor()
    print(len(League_list), len(Country_list),
          len(Clubs_list), len(League_value_list))
    print(Country_list, Clubs_list, League_value_list)
    for i in range(len(League_list)):
        insert_query = \
            f'INSERT INTO Leagues VALUES("{League_list[i]}", "{Country_list[i]}", "{Clubs_list[i]}","{League_value_list[i]}")'
        cursor.execute(insert_query)
        db.commit()

###########################################################################################################
# 팀 가져오기
###########################################################################################################


def Get_Team():
    Base_URLs = []
    Con_URLs = []
    Country = []
    Country_list = []
    Leauge_list = []

    continents = ['europa', 'europa/wettbewerbe?ajax=yw1&page=2', 'europa/wettbewerbe?ajax=yw1&page=3', 'europa/wettbewerbe?ajax=yw1&page=4',
                  'asien', 'asienn/wettbewerbe?ajax=yw1&page=2', 'amerika', 'afrika']
    for continent in continents:
        Con_URLs.append(
            f'https://www.transfermarkt.com/wettbewerbe/{continent}')

    URLs = []
    First_URL = 'https://www.transfermarkt.com'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    print("1")
    for Con_URL1 in Con_URLs:
        Con_html1 = requests.get(Con_URL1, headers=headers).text
        Con_soup1 = BeautifulSoup(Con_html1, 'html.parser')
        for href in Con_soup1.find_all("table", {"class": 'inline-table'}):
            Team_URL = href.find_all("a")[1]["href"]
            if Team_URL == "/nedbank-cup/startseite/wettbewerb/NEDC":
                break
            if Team_URL == "/campeonato-brasileiro-serie-b/startseite/wettbewerb/BRA2":
                break
            if Team_URL == "/k3-league/startseite/wettbewerb/K3L":
                break
            if Team_URL == "/3-liga/startseite/wettbewerb/L3":
                break
            Base_URLs.append(First_URL+Team_URL)
    i = 0
    print("2")
    for Con_URL2 in Con_URLs:
        Con_html2 = requests.get(Con_URL2, headers=headers).text
        Con_soup2 = BeautifulSoup(Con_html2, 'html.parser')
        for alt in Con_soup2.find_all("td", {"class": 'zentriert'}):
            i = i + 1
            if i % 6 == 1:
                find_country = alt.find("img")["title"]
                Country.append(find_country)
    i = 0
    print("3")
    for Base_URL in Base_URLs:
        Base_html = requests.get(Base_URL, headers=headers).text
        Base_soup = BeautifulSoup(Base_html, 'html.parser')

        League_soup = Base_soup.find(
            "h1", {"class": 'spielername-profil'})
        try:
            League_name = League_soup.text
        except:
            pass

        for href in Base_soup.find_all("td", class_="hauptlink no-border-links show-for-small show-for-pad"):
            Team_URL = href.find("a")["href"]
            URLs.append(First_URL+Team_URL)
            Leauge_list.append(League_name)
            Country_list.append(Country[i])
        i = i + 1
    print("4")
    Team_list = []
    for URL in URLs:
        html = requests.get(URL, headers=headers).text
        soup = BeautifulSoup(html, 'html.parser')

        Team_soup = soup.find(
            "h1", {"itemprop": 'name'})
        try:
            print(Team_soup.text.strip())
            Team_list.append(Team_soup.text.strip())
        except:
            pass
    Team_value_list = []
    Team_value_soup = Base_soup.find_all(
        "td", {"class": 'rechts hide-for-small hide-for-pad'})
    i = 0
    for Team_value in Team_value_soup[2:]:
        i = i + 1
        if i % 2 == 0:
            continue
        try:
            Team_value_list.append(Team_value.text)
            print(Team_value.text)
        except:
            pass
    print("5")
    Team_age_list = []
    Team_age_soup = Base_soup.find_all(
        "td", {"class": 'zentriert'})
    i = 0
    for Team_age in Team_age_soup[4:]:
        i = i + 1
        if i % 4 == 2:
            Team_age_list.append(Team_age.text)
    print("6")
    db = sqlite3.connect("DB/FO_datafile.db")
    cursor = db.cursor()
    for i in range(len(Team_list)):
        insert_query = \
            f'INSERT INTO Teams VALUES("{League_list[i]}", "{Country_list[i]}", "{Team_list[i]}", "{Team_value_list[i]}", "{Team_age_list[i]}")'
        cursor.execute(insert_query)
        db.commit()


###########################################################################################################
# 선수 가져오기
###########################################################################################################
def Get_Player():
    Base_URLs = []
    Con_URLs = []
    continents = ['asien', 'asienn/wettbewerbe?ajax=yw1&page=2',
                  'amerika', 'afrika']
    # continents = ['europa', 'europa/wettbewerbe?ajax=yw1&page=2', 'europa/wettbewerbe?ajax=yw1&page=3', 'europa/wettbewerbe?ajax=yw1&page=4',
    #   'asien', 'asienn/wettbewerbe?ajax=yw1&page=2', 'amerika', 'afrika']
    for continent in continents:
        Con_URLs.append(
            f'https://www.transfermarkt.com/wettbewerbe/{continent}')

    URLs = []
    First_URL = 'https://www.transfermarkt.com'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    for Con_URL in Con_URLs:
        Con_html = requests.get(Con_URL, headers=headers).text
        Con_soup = BeautifulSoup(Con_html, 'html.parser')
        for href in Con_soup.find_all("table", {"class": 'inline-table'}):
            Team_URL = href.find_all("a")[1]["href"]
            if Team_URL == "/nedbank-cup/startseite/wettbewerb/NEDC":
                break
            if Team_URL == "/campeonato-brasileiro-serie-b/startseite/wettbewerb/BRA2":
                break
            if Team_URL == "/k3-league/startseite/wettbewerb/K3L":
                break
            if Team_URL == "/3-liga/startseite/wettbewerb/L3":
                break
            Base_URLs.append(First_URL+Team_URL)

    for Base_URL in Base_URLs:
        Base_html = requests.get(Base_URL, headers=headers).text
        Base_soup = BeautifulSoup(Base_html, 'html.parser')
        for href in Base_soup.find_all("td", class_="hauptlink no-border-links show-for-small show-for-pad"):
            Team_URL = href.find("a")["href"]
            URLs.append(First_URL+Team_URL)

    for URL in URLs:
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
        if len(Player_list) < len(Player_value_list):
            Player_value_list.pop(-1)

        db = sqlite3.connect("DB/FO_datafile.db")
        cursor = db.cursor()
        for i in range(len(Player_list)):
            try:
                insert_query = \
                    f'INSERT INTO Players VALUES("{Player_list[i]}","{Team_name}", "{Player_num_list[i]}", "{Player_pos_list[i]}","{Player_age_list[i]}", "{Player_value_list[i]}")'
                cursor.execute(insert_query)
                db.commit()
            except:
                insert_query = \
                    f'INSERT INTO Players VALUES("{Player_list[i]}","{Team_name}", "{Player_num_list[i]}", "{Player_pos_list[i]}","{Player_age_list[i]}", "")'
                cursor.execute(insert_query)
                db.commit()


########################################################################################
if __name__ == "__main__":
    Get_Leauge()
