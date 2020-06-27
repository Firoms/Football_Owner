import requests
from datetime import datetime
import sqlite3

API_KEY = 'vt3RYmcPrf4zdoIQLYtV51cx58szBpFL10D757Bc'

if __name__ == "__main__":
    ##########################################################################
    # 리그 id 가져오기
    ##########################################################################

    # r = requests.get(
    #     'https://data.football-api.com/v3/competitions?Authorization=cfnR6LWc4i4MDFLlPJrajoa465c4qjF594kpIy4b')
    # data = r.json()

    db = sqlite3.connect("DB/Football_API.db")
    cursor = db.cursor()

    # for i in range(len(data)):
    #     leauge_data = data[i]
    #     leauge_id = leauge_data['id']
    #     leauge_name = leauge_data['name']
    #     leauge_region = leauge_data['region']
    #     insert_query = \
    #         f"INSERT INTO Competitions VALUES('{leauge_id}', '{leauge_name}', '{leauge_region}')"
    #     cursor.execute(insert_query)
    #     db.commit()

    ###########################################################################
    # 각 팀 id 가져오기
    ###########################################################################
    #
    # cursor.execute(
    #     "SELECT * FROM Competitions Where name = 'Premier League' and region = 'England'")
    # EPL_id = cursor.fetchone()[0]
    # r = requests.get(
    #     f'https://data.football-api.com/v3/standings/{EPL_id}?Authorization=cfnR6LWc4i4MDFLlPJrajoa465c4qjF594kpIy4b')
    # data = r.json()
    # for i in range(len(data)):
    #     Team_data = data[i]
    #     Team_country = Team_data["country"]
    #     Team_id = Team_data["team_id"]
    #     Team_name = Team_data["team_name"]
    #     Team_form = Team_data["recent_form"]
    #     Team_position = Team_data["position"]
    #     Team_home_match = Team_data["home_gp"]
    #     Team_home_win = Team_data["home_w"]
    #     Team_home_draw = Team_data["home_d"]
    #     Team_home_lose = Team_data["home_l"]
    #     Team_home_goal = Team_data["home_gs"]
    #     Team_home_goal_lost = Team_data["home_ga"]
    #     Team_away_match = Team_data["away_gp"]
    #     Team_away_win = Team_data["away_w"]
    #     Team_away_draw = Team_data["away_d"]
    #     Team_away_lose = Team_data["away_l"]
    #     Team_away_goal = Team_data["away_gs"]
    #     Team_away_goal_lost = Team_data["away_ga"]
    #     Team_goal_dif = Team_data["gd"]
    #     Team_points = Team_data["points"]
    #     insert_query = \
    #         f"INSERT INTO Team_Datas VALUES('{Team_country}', '{Team_id}', '{Team_name}', '{Team_form}', '{Team_position}', '{Team_home_match}',\
    #                                         '{Team_home_win}', '{Team_home_draw}', '{Team_home_lose}', '{Team_home_goal}', '{Team_home_goal_lost}',\
    #                                         '{Team_away_match}', '{Team_away_win}', '{Team_away_draw}', '{Team_away_lose}', '{Team_away_goal}',\
    #                                         '{Team_away_goal_lost}', '{Team_goal_dif}', '{Team_points}')"
    #     cursor.execute(insert_query)
    #     db.commit()

    ###########################################################################
    # 각 팀 Api 가져오기
    ###########################################################################

    cursor.execute(
        "SELECT COUNT(*) FROM Team_Datas")
    Team_range = cursor.fetchone()[0]
    Teams = []
    Teams_id = []

    cursor.execute(
        "SELECT name FROM Team_Datas ORDER BY position")
    for i in range(Team_range):
        Teams.append(cursor.fetchone()[0])

    cursor.execute(
        "SELECT id FROM Team_Datas")
    for i in range(Team_range):
        Teams_id.append(cursor.fetchone()[0])

    for i in range(Team_range):
        print(Teams[i])
        r = requests.get(
            f'https://data.football-api.com/v3/teams/{Teams_id[i]}?Authorization=cfnR6LWc4i4MDFLlPJrajoa465c4qjF594kpIy4b')
        player_datas = r.json()[0]["squad"]
        for j in range(len(player_datas)):
            try:
                data = player_datas[j]
                Player_id = data["id"]
                Player_name = data["name"]
                Player_number = data["number"]
                Player_age = data["age"]
                Player_position = data["position"]
                Player_injured = data["injured"]
                Player_minutes = data["minutes"]
                Player_appearences = data["appearences"]
                Player_goals = data["goals"]
                Player_assists = data["assists"]
                Player_yellowcards = data["yellowcards"]
                Player_yellowred = data["yellowred"]
                Player_redcards = data["redcards"]

                insert_query = \
                    f"INSERT INTO Players VALUES('{Teams[i]}',  '{Player_id}', '{Player_name}', '{Player_number}', '{Player_age}',\
                                                    '{Player_position}', '{Player_injured}', '{Player_minutes}', '{Player_appearences}',\
                                                    '{Player_goals}', '{Player_assists}', '{Player_yellowcards}', '{Player_yellowred}', '{Player_redcards}')"
                cursor.execute(insert_query)
                db.commit()
            except:
                print(Teams[i], end="")
                print("error")
