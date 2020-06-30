import sqlite3
from tkinter import *
import tkinter.messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import time


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
    Date = ("%04d.%02d.%02d.%02d.%02d.%02d" % (now.tm_year, now.tm_mon,
                                               now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
    if name == None:
        return 'No'
    else:
        db = sqlite3.connect("DB/FO_savefile1.db")
        cursor = db.cursor()
        insert_query = \
            f"INSERT INTO Gamer VALUES('{name}',  '무직', '{Date}')"
        cursor.execute(insert_query)
        db.commit()


def input_Names2():
    name = askstring('구단주 생성', '구단주 이름을 입력하세요.')
    now = time.localtime()
    Date = ("%04d.%02d.%02d.%02d.%02d.%02d" % (now.tm_year, now.tm_mon,
                                               now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
    if name == None:
        pass
    else:
        db = sqlite3.connect("DB/FO_savefile2.db")
        cursor = db.cursor()
        insert_query = \
            f"INSERT INTO Gamer VALUES('{name}',  '무직', '{Date}')"
        cursor.execute(insert_query)
        db.commit()


def reset_datas():
    Warning_message = tkinter.messagebox.askokcancel(
        "경고", "정말 모든 데이터 파일을 삭제하시겠습니까?")
    if Warning_message == True:
        for i in range(3):
            db = sqlite3.connect(f"DB/FO_savefile{i+1}.db")
            cursor = db.cursor()
            cursor.execute("DELETE FROM Gamer")
            cursor.execute("DELETE FROM Players")
            cursor.execute("DELETE FROM Statistics")
            cursor.execute("DELETE FROM Team_Datas")
            db.commit()
