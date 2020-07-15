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


def make_ablity():
    db = sqlite3.connect(f"DB/FO_datafile.db")
    cursor1 = db.cursor()
    cursor1.execute(
        "SELECT Age From Players")
    cursor2 = db.cursor()
    cursor2.execute(
        "SELECT Market_Value From Players")
    cursor = db.cursor()

    for i in range(4):
        Age = cursor1.fetchone()[0]
        Market_value = cursor2.fetchone()[0]
        Age = Age[-3:-1]
        Market_value = Market_value[1:-1]
        print(Age, Market_value)
        cursor.execute(
            f"UPDATE Players SET Ability ='{i}' LIMIT 1 OFFSET {i}")
        db.commit()


get_max()
