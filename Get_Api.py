import requests
from datetime import datetime
import sqlite3

API_KEY = 'vt3RYmcPrf4zdoIQLYtV51cx58szBpFL10D757Bc'

if __name__ == "__main__":
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

    cursor.execute(
        "SELECT * FROM Competitions Where name = 'Premier League' and region = 'England'")
    EPL_id = cursor.fetchone()[0]
    print(EPL_id)
    r = requests.get(
        f'https://data.football-api.com/v3/standings/{EPL_id}?Authorization=cfnR6LWc4i4MDFLlPJrajoa465c4qjF594kpIy4b')
    data = r.json()
    print(r)
    print(data)
