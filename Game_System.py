import sqlite3


def change_values():
    db = sqlite3.connect(f"DB/FO_datafile.db")
    cursor = db.cursor()
    cursor.execute(
        "UPDATE Players SET Age='Apr 22, 1996 (24)'  WHERE Age == '- (-)'")
    db.commit()


def get_max():
    db = sqlite3.connect(f"DB/FO_datafile.db")
    cursor = db.cursor()
    cursor.execute(
        "SELECT Age From Players")
    a = cursor.fetchone()[0][-3:-1]
    max_age = int(a)
    min_age = int(a)
    for i in range(59293):
        a = int(cursor.fetchone()[0][-3:-1])
        if max_age < a:
            max_age = a
        if min_age > a:
            min_age = a
    print(max_age, min_age)


def make_row_num():
    db = sqlite3.connect(f"DB/FO_datafile.db")
    cursor = db.cursor()

    for i in range(59293):
        cursor.execute(
            f"SELECT * FROM Players ORDER By Field9 LIMIT 1 OFFSET {i}")
        a = cursor.fetchone()
        name = a[1]
        team = a[2]

        cursor.execute(
            f'UPDATE Players SET Seq = {i+1} Where Name = "{name}" AND Team = "{team}"')
        db.commit()


def make_ablity():
    Ability_data = []
    Value_data = []

    db = sqlite3.connect(f"DB/FO_datafile.db")
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
                f"UPDATE Players SET Ability='{i-23+Ability_data[r]}'  WHERE Age like '%({i})' AND Market_value == '€{Value_data[r]}0m'")
            db.commit()
    for i in range(30, 36):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{i-26+Ability_data[r]}'  WHERE Age like '%({i})' AND Market_value == '€{Value_data[r]}0m'")
            db.commit()
    for i in range(36, 55):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{i-12+Ability_data[r]}'  WHERE Age like '%({i})' AND Market_value == '€{Value_data[r]}0m'")
            db.commit()
    for i in range(22, 26):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{27-i+Ability_data[r]}'  WHERE Age like '%({i})' AND Market_value == '€{Value_data[r]}0m'")
            db.commit()
    for i in range(14, 22):
        for r in range(len(Ability_data)):
            cursor.execute(
                f"UPDATE Players SET Ability='{25-i+Ability_data[r]}'  WHERE Age like '%({i})' AND Market_value == '€{Value_data[r]}0m'")
            db.commit()


make_row_num()
