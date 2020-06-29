import sqlite3
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import time


def Get_Savefiles():
    db = sqlite3.connect("DB/Football_API_Test.db")
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM Gamer ORDER BY Date DESC")
    Save_list1 = cursor.fetchone()
    Save_list2 = cursor.fetchone()
    Save_list3 = cursor.fetchone()
    return Save_list1, Save_list2, Save_list3


def input_Names():
    name = askstring('구단주 생성', '구단주 이름을 입력하세요.')
    now = time.localtime()
    Date = ("%04d.%02d.%02d.%02d.%02d.%02d" % (now.tm_year, now.tm_mon,
                                               now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
    if name == None:
        pass
    else:
        db = sqlite3.connect("DB/Football_API_Test.db")
        cursor = db.cursor()
        insert_query = \
            f"INSERT INTO Gamer VALUES('{name}',  'not employed', '{Date}')"
        cursor.execute(insert_query)
        db.commit()
