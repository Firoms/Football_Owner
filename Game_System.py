import sqlite3
import random


def change_ages():
    db = sqlite3.connect(f"DB/FO_datafile1.db")
    cursor = db.cursor()
    cursor1 = db.cursor()
    # cursor.execute(
    #     "SELECT Seq, Age From Players")
    # for i in range(56297):
    #     a = cursor.fetchone()
    #     Seq = a[0]
    #     Age = a[1][-3:-1]
    cursor1.execute(
        f"UPDATE Players SET Age='23'  WHERE Age == '(-'")
    db.commit()


def change_values():
    db = sqlite3.connect(f"DB/FO_datafile1.db")
    cursor = db.cursor()
    cursor1 = db.cursor()
    cursor1.execute(
        f'UPDATE Leagues SET Value="0"')
    db.commit()
    # cursor.execute(
    #     "SELECT Seq, Age, Ability, Potential From Players")
    # for i in range(56297):
    #     a = cursor.fetchone()
    #     Seq = a[0]
    #     Age = int(a[1])
    #     Ability = int(a[2])
    #     Potential = int(a[3])
    #     Value = int(((Ability-Age+10)**3) *
    #                 ((Ability-45)**3)*(Potential**2)/20000000)
    #     cursor1.execute(
    #         f"UPDATE Players SET Market_Value='{Value}'  WHERE Seq == '{Seq}'")
    #     db.commit()

    # cursor.execute(
    #     "SELECT Team, sum(Market_Value) Value FROM Players GROUP By Team")
    # for i in range(2093):
    #     a = cursor.fetchone()
    #     Team = a[0]
    #     Value = a[1]
    #     print(Team, Value)
    #     cursor1.execute(
    #         f'UPDATE Teams SET Value="{Value}" WHERE Team=="{Team}"')
    #     db.commit()

    cursor.execute(
        "SELECT League,Country, sum(Value) Value FROM Teams GROUP By League")
    for i in range(2093):
        a = cursor.fetchone()
        League = a[0]
        Country = a[1]
        Value = a[2]
        print(League, Value)
        cursor1.execute(
            f'UPDATE Leagues SET Value="{Value}" WHERE Name=="{League}" AND Country=="{Country}"')
        db.commit()


# SELECT Team, sum(Market_Value) Value
# FROM Players
# GROUP By Team
# ORDER By Value
# ;


def delete_same():
    name = []
    team = []
    number = []
    position = []
    age = []
    market_value = []

    db = sqlite3.connect(f"DB/FO_datafile1.db")
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM(SELECT Name, Team, Position, Age, Count(*) Cnt	FROM Staffs GROUP by Name, Team) WHERE Cnt>1")
    for i in range(176):
        a = cursor.fetchone()
        name.append(a[0])
        team.append(a[1])
        position.append(a[2])
        age.append(a[3])
    print("delete 시작")
    for i in range(176):
        cursor.execute(
            f'DELETE FROM Staffs WHERE Name=="{name[i]}" and Team=="{team[i]}" and Age=="{age[i]}"')
        db.commit()
    print("insert 시작")
    for i in range(176):
        insert_query = \
            f'INSERT INTO Staffs VALUES("","{name[i]}", "{team[i]}","{position[i]}","{age[i]}")'
        cursor.execute(insert_query)
        db.commit()


def make_row_num():
    db = sqlite3.connect(f"DB/FO_datafile1.db")
    cursor = db.cursor()
    cursor1 = db.cursor()
    cursor.execute(
        f"SELECT * FROM Staffs")
    for i in range(5761):

        a = cursor.fetchone()
        league = a[1]
        country = a[2]
        team = a[3]
        value = a[4]

        cursor1.execute(
            f'UPDATE Staffs SET Seq = {i+1} Where Name = "{league}" AND Team = "{country}" AND Position = "{team}" AND Age = "{value}"')
        db.commit()


def make_ablity():
    Ability_data = []
    Value_data = []

    db = sqlite3.connect(f"DB/FO_datafile1.db")
    cursor = db.cursor()
    # cursor.execute(
    #     f"UPDATE Players SET Ability='0'")
    # db.commit()
    cursor.execute(
        "SELECT Market_Value From Players Group BY Market_Value")
    for i in range(116):
        a = cursor.fetchone()[0][1:-2]
        Value_data.append(a)
    for i in Value_data:
        i = float(i)
        if i == 0:
            Ability_data.append(52)
        elif 1 <= i < 2:
            Ability_data.append(55)
        elif 2 <= i < 3:
            Ability_data.append(57)
        elif 3 <= i < 4:
            Ability_data.append(60)
        elif 4 <= i < 5:
            Ability_data.append(63)
        elif 5 <= i < 8:
            Ability_data.append(65)
        elif 8 <= i < 12:
            Ability_data.append(67)
        elif 12 <= i < 20:
            Ability_data.append(69)
        elif 20 <= i < 25:
            Ability_data.append(71)
        elif 25 <= i < 30:
            Ability_data.append(74)
        elif 30 <= i < 40:
            Ability_data.append(77)
        elif 40 <= i < 50:
            Ability_data.append(80)
        elif 50 <= i < 60:
            Ability_data.append(83)
        elif 60 <= i < 70:
            Ability_data.append(85)
        elif 70 <= i < 80:
            Ability_data.append(86)
        elif 80 <= i < 100:
            Ability_data.append(87)
        elif 100 <= i < 120:
            Ability_data.append(88)
        elif 120 <= i <= 140:
            Ability_data.append(89)
        elif 140 <= i <= 180:
            Ability_data.append(90)
    for i in range(26, 31):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{i-23+Ability_data[r]-4}'  WHERE Age == '{i}' AND Market_value == '€{Value_data[r]}0m'")
            db.commit()
    for i in range(31, 36):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{i-26+Ability_data[r]-4}'  WHERE Age == '{i}' AND Market_value == '€{Value_data[r]}0m'")
            db.commit()
    for i in range(36, 55):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{56-i+Ability_data[r]-4}'  WHERE Age == '{i}' AND Market_value == '€{Value_data[r]}0m'")
            db.commit()
    for i in range(22, 26):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{27-i+Ability_data[r]-4}'  WHERE Age == '{i}' AND Market_value == '€{Value_data[r]}0m'")
            db.commit()
    for i in range(14, 22):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{25-i+Ability_data[r]-7}'  WHERE Age == '{i}' AND Market_value == '€{Value_data[r]}0m'")
            db.commit()


def make_potential():
    db = sqlite3.connect(f"DB/FO_datafile1.db")
    cursor = db.cursor()
    cursor1 = db.cursor()
    cursor.execute(
        "SELECT Seq, Age, Ability, Market_Value From Players")
    for i in range(56297):
        print(i)
        a = cursor.fetchone()
        Seq = a[0]
        Age = int(a[1])
        Ability = int(a[2])
        potential = Ability
        if 31 <= Age:
            ranpot = random.randrange(Ability, Ability+2)
            for i in range(3):
                if ranpot >= 85:
                    ranpot = random.randrange(Ability, Ability+2)
            if potential < ranpot:
                potential = ranpot
        elif 28 <= Age < 31:
            ranpot = random.randrange(Ability, Ability+3)
            for i in range(3):
                if ranpot >= 85:
                    ranpot = random.randrange(Ability, Ability+3)
            if potential < ranpot:
                potential = ranpot
        elif 25 <= Age < 28:
            ranpot = random.randrange(Ability, Ability+4)
            for i in range(3):
                if ranpot >= 85:
                    ranpot = random.randrange(Ability, Ability+4)
            if potential < ranpot:
                potential = ranpot
        elif 22 <= Age < 25:
            ranpot = random.randrange(Ability, 94)
            for i in range(3):
                if ranpot >= 85:
                    ranpot = random.randrange(Ability, 94)
            if potential < ranpot:
                potential = ranpot
        else:
            ranpot = random.randrange(Ability, 96)
            for i in range(3):
                if ranpot >= 85:
                    ranpot = random.randrange(Ability, 96)
            if potential < ranpot:
                potential = ranpot

        cursor1.execute(
            f"UPDATE Players SET Potential='{potential}'  WHERE Seq == '{Seq}'")
        db.commit()


make_row_num()
