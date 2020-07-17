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
    cursor.execute(
        "UPDATE Players Set Market_Value ='€0.00m' Where Market_Value like '%Th.' OR Market_Value == '-' OR Market_Value == ''")
    db.commit()


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
        "SELECT * FROM(SELECT Name, Team, Number, Position, Age, Market_Value, Count(*) Cnt	FROM Players GROUP by Name, Team, Age) WHERE Cnt>1")
    for i in range(2602):
        a = cursor.fetchone()
        name.append(a[0])
        team.append(a[1])
        number.append(a[2])
        position.append(a[3])
        age.append(a[4])
        market_value.append(a[5])
    print("delete 시작")
    for i in range(2602):
        cursor.execute(
            f'DELETE FROM Players WHERE Name=="{name[i]}" and Team=="{team[i]}" and Age=="{age[i]}"')
        db.commit()
    print("insert 시작")
    for i in range(2602):
        insert_query = \
            f'INSERT INTO Players VALUES("{name[i]}", "{team[i]}", "{number[i]}","{position[i]}","{age[i]}","{market_value[i]}")'
        cursor.execute(insert_query)
        db.commit()


def make_row_num():
    db = sqlite3.connect(f"DB/FO_datafile1.db")
    cursor = db.cursor()

    for i in range(56297):
        cursor.execute(
            f"SELECT * FROM Players ORDER By Field9 LIMIT 1 OFFSET {i}")
        a = cursor.fetchone()
        name = a[1]
        team = a[2]
        age = a[5]

        cursor.execute(
            f'UPDATE Players SET Seq = {i+1} Where Name = "{name}" AND Team = "{team}" AND Age = "{age}"')
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
            Ability_data.append(40)
        elif 1 <= i < 2:
            Ability_data.append(45)
        elif 2 <= i < 3:
            Ability_data.append(50)
        elif 3 <= i < 4:
            Ability_data.append(55)
        elif 4 <= i < 5:
            Ability_data.append(60)
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
            Ability_data.append(82)
        elif 60 <= i < 70:
            Ability_data.append(84)
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
    for i in range(26, 30):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{i-33+Ability_data[r]}'  WHERE Age == '{i}' AND Market_value == '€{Value_data[r]}0m'")
            db.commit()
    for i in range(30, 36):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{i-36+Ability_data[r]}'  WHERE Age == '{i}' AND Market_value == '€{Value_data[r]}0m'")
            db.commit()
    for i in range(36, 55):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{i-22+Ability_data[r]}'  WHERE Age == '{i}' AND Market_value == '€{Value_data[r]}0m'")
            db.commit()
    for i in range(22, 26):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{17-i+Ability_data[r]}'  WHERE Age == '{i}' AND Market_value == '€{Value_data[r]}0m'")
            db.commit()
    for i in range(14, 22):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{13-i+Ability_data[r]}'  WHERE Age == '{i}' AND Market_value == '€{Value_data[r]}0m'")
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
        Market_Value = a[3]

        potential = 0
        if Age < 34:
            if Ability < 50:
                Ability = Ability + 10
            for i in range(0, 34-Age, 2):
                ranpot = random.randrange(Ability, 86)
                if potential < ranpot:
                    potential = ranpot
            if potential > 80:
                ranpot = random.randrange(Ability, 86)
                potential = ranpot
        else:
            if Ability < 70:
                Ability = Ability + 4
            potential = Ability

        if len(Market_Value) == 7:
            potential += random.randrange(1, 4)
        cursor1.execute(
            f"UPDATE Players SET Potential='{potential}'  WHERE Seq == '{Seq}'")
        db.commit()


make_potential()
