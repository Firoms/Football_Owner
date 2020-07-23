import sqlite3
from tkinter import *
import tkinter.messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import time
import random

table_list = ['Coaches', 'Leagues', 'Players',
              'Staffs', 'Teams']


def Check_Savefiles(savefile):
    db = sqlite3.connect(f"DB/FO_savefile{savefile}.db")
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM Gamer ORDER BY Date DESC")
    Save_list = cursor.fetchone()
    return Save_list


def input_Names1():
    name = askstring('구단주 생성', '구단주 이름을 입력하세요.')
    now = time.localtime()
    Date = ("%04d년 %02d월 %02d일 %02d시 %02d분 %02d초" % (now.tm_year, now.tm_mon,
                                                     now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
    if name == None:
        return 'No'
    else:
        db = sqlite3.connect("DB/FO_savefile1.db")
        cursor = db.cursor()
        insert_query = \
            f"INSERT INTO Gamer VALUES('{name}',  '무직', '{Date}','-')"
        cursor.execute(insert_query)
        db.commit()


def input_Names2():
    name = askstring('구단주 생성', '구단주 이름을 입력하세요.')
    now = time.localtime()
    Date = ("%04d년 %02d월 %02d일 %02d시 %02d분 %02d초" % (now.tm_year, now.tm_mon,
                                                     now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
    if name == None:
        return 'No'
    else:
        db = sqlite3.connect("DB/FO_savefile2.db")
        cursor = db.cursor()
        insert_query = \
            f"INSERT INTO Gamer VALUES('{name}',  '무직', '{Date}','-')"
        cursor.execute(insert_query)
        db.commit()


def check_money():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM Gamer")
    Save_list = cursor.fetchone()[3]
    return Save_list


def give_money(money):
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"UPDATE Gamer SET Money ='{money}'")
    db.commit()
    return 0


def reset_datas():
    Warning_message = tkinter.messagebox.askokcancel(
        "경고", "정말 모든 데이터 파일을 삭제하시겠습니까?")
    if Warning_message == True:
        for i in range(3):
            db = sqlite3.connect(f"DB/FO_savefile{i+1}.db")
            cursor = db.cursor()
            for table in table_list:
                cursor.execute(f"DELETE FROM {table}")
            cursor.execute("DELETE FROM Gamer")
            db.commit()


def Auto_save_get_data(num):
    db_load = sqlite3.connect(f"DB/FO_datafile.db")
    l_cursor = db_load.cursor()
    db_save = sqlite3.connect(f"DB/FO_savefile{num}.db")
    s_cursor = db_save.cursor()
    for table in table_list:
        l_cursor.execute(
            f"SELECT COUNT(*) FROM {table}")
        count = l_cursor.fetchone()[0]
        l_cursor.execute(
            f"SELECT * FROM {table}")
        for i in range(count):
            Save_list = l_cursor.fetchone()
            s_cursor.execute(
                f"INSERT INTO {table} VALUES{Save_list}")
    db_save.commit()


def Save1_data():
    Warning_message = tkinter.messagebox.askokcancel(
        "경고", "정말 데이터 파일을 덮어씌우시겠습니까?")
    if Warning_message == True:
        db = sqlite3.connect(f"DB/FO_savefile1.db")
        cursor = db.cursor()
        for table in table_list:
            cursor.execute(f"DELETE FROM {table}")
        cursor.execute("DELETE FROM Gamer")
        db.commit()
        db_load = sqlite3.connect(f"DB/FO_savefile3.db")
        l_cursor = db_load.cursor()
        db_save = sqlite3.connect(f"DB/FO_savefile1.db")
        s_cursor = db_save.cursor()
        for table in table_list:
            l_cursor.execute(
                f"SELECT COUNT(*) FROM {table}")
            count = l_cursor.fetchone()[0]
            l_cursor.execute(
                f"SELECT * FROM {table}")
            for i in range(count):
                Save_list = l_cursor.fetchone()
                s_cursor.execute(
                    f"INSERT INTO {table} VALUES{Save_list}")
        l_cursor.execute(f"SELECT * FROM Gamer")
        Save_list = l_cursor.fetchone()
        now = time.localtime()
        Date = ("%04d년 %02d월 %02d일 %02d시 %02d분 %02d초" % (now.tm_year, now.tm_mon,
                                                         now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
        s_cursor.execute(
            f"INSERT INTO Gamer VALUES('{Save_list[0]}','{Save_list[1]}','{Date}','{Save_list[3]}')")
        db_save.commit()
        Save_message = tkinter.messagebox.showinfo(
            "저장 완료", "데이터 파일을 저장했습니다.")


def Save2_data():
    Warning_message = tkinter.messagebox.askokcancel(
        "경고", "정말 데이터 파일을 덮어씌우시겠습니까?")
    if Warning_message == True:
        db = sqlite3.connect(f"DB/FO_savefile2.db")
        cursor = db.cursor()
        for table in table_list:
            cursor.execute(f"DELETE FROM {table}")
        cursor.execute("DELETE FROM Gamer")
        db.commit()
        db_load = sqlite3.connect(f"DB/FO_savefile3.db")
        l_cursor = db_load.cursor()
        db_save = sqlite3.connect(f"DB/FO_savefile2.db")
        s_cursor = db_save.cursor()
        for table in table_list:
            l_cursor.execute(
                f"SELECT COUNT(*) FROM {table}")
            count = l_cursor.fetchone()[0]
            l_cursor.execute(
                f"SELECT * FROM {table}")
            for i in range(count):
                Save_list = l_cursor.fetchone()
                s_cursor.execute(
                    f"INSERT INTO {table} VALUES{Save_list}")
        l_cursor.execute(f"SELECT * FROM Gamer")
        Save_list = l_cursor.fetchone()
        now = time.localtime()
        Date = ("%04d년 %02d월 %02d일 %02d시 %02d분 %02d초" % (now.tm_year, now.tm_mon,
                                                         now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
        s_cursor.execute(
            f"INSERT INTO Gamer VALUES('{Save_list[0]}','{Save_list[1]}','{Date}','{Save_list[3]}')")
        db_save.commit()
        Save_message = tkinter.messagebox.showinfo(
            "저장 완료", "데이터 파일을 저장했습니다.")


def load1_data():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    for table in table_list:
        cursor.execute(f"DELETE FROM {table}")
    cursor.execute("DELETE FROM Gamer")
    db.commit()
    db_load = sqlite3.connect(f"DB/FO_savefile1.db")
    l_cursor = db_load.cursor()
    db_save = sqlite3.connect(f"DB/FO_savefile3.db")
    s_cursor = db_save.cursor()
    for table in table_list:
        l_cursor.execute(
            f"SELECT COUNT(*) FROM {table}")
        count = l_cursor.fetchone()[0]
        l_cursor.execute(
            f"SELECT * FROM {table}")
        for i in range(count):
            Save_list = l_cursor.fetchone()
            s_cursor.execute(
                f"INSERT INTO {table} VALUES{Save_list}")
    l_cursor.execute(f"SELECT * FROM Gamer")
    Save_list = l_cursor.fetchone()
    now = time.localtime()
    Date = ("%04d년 %02d월 %02d일 %02d시 %02d분 %02d초" % (now.tm_year, now.tm_mon,
                                                     now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
    s_cursor.execute(
        f"INSERT INTO Gamer VALUES('{Save_list[0]}','{Save_list[1]}','{Date}','{Save_list[3]}')")
    db_save.commit()


def load2_data():
    try:
        db = sqlite3.connect(f"DB/FO_savefile3.db")
        cursor = db.cursor()
        for table in table_list:
            cursor.execute(f"DELETE FROM {table}")
        cursor.execute("DELETE FROM Gamer")
        db.commit()
        db_load = sqlite3.connect(f"DB/FO_savefile2.db")
        l_cursor = db_load.cursor()
        db_save = sqlite3.connect(f"DB/FO_savefile3.db")
        s_cursor = db_save.cursor()
        for table in table_list:
            l_cursor.execute(
                f"SELECT COUNT(*) FROM {table}")
            count = l_cursor.fetchone()[0]
            l_cursor.execute(
                f"SELECT * FROM {table}")
            for i in range(count):
                Save_list = l_cursor.fetchone()
                s_cursor.execute(
                    f"INSERT INTO {table} VALUES{Save_list}")
        l_cursor.execute(f"SELECT * FROM Gamer")
        Save_list = l_cursor.fetchone()
        now = time.localtime()
        Date = ("%04d년 %02d월 %02d일 %02d시 %02d분 %02d초" % (now.tm_year, now.tm_mon,
                                                         now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
        s_cursor.execute(
            f"INSERT INTO Gamer VALUES('{Save_list[0]}','{Save_list[1]}','{Date}','{Save_list[3]}')")
        db_save.commit()
    except:
        input_Names2()


def time_auto_load():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    now = time.localtime()
    Date = ("%04d년 %02d월 %02d일 %02d시 %02d분 %02d초" % (now.tm_year, now.tm_mon,
                                                     now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
    cursor.execute(f"UPDATE Gamer Set Date= '{Date}'")
    db.commit()


def mini_game():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    ran = random.randrange(1, 3001)
    cursor.execute(
        f"SELECT * FROM Players Where Seq = '{ran}'")
    a = cursor.fetchone()
    return a
