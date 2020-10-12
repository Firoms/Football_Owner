import sqlite3
from tkinter import *
import tkinter.messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import time
import random
import threading
import queue

table_list = ['Coaches', 'Leagues', 'Players', 'Staffs', 'Teams', 'Gamer_Team',
              'League_Calander', 'League_table', 'Message_box', 'Player_Stat']

###############################################################################
# 게이머 생성
###############################################################################


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


###############################################################################
# 데이터 저장
###############################################################################
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


def Auto_save_get_data(num):
    db_load = sqlite3.connect(f"DB/FO_datafile.db")
    l_cursor = db_load.cursor()
    db_save = sqlite3.connect(f"DB/FO_savefile{num}.db")
    s_cursor = db_save.cursor()
    for table in table_list[0:5]:
        l_cursor.execute(
            f"SELECT COUNT(*) FROM {table}")
        count = l_cursor.fetchone()[0]
        l_cursor.execute(
            f"SELECT * FROM {table}")
        for i in range(count):
            Save_list = l_cursor.fetchone()
            s_cursor.execute(
                f"INSERT INTO {table} VALUES{Save_list}")
    db_load.commit()
    db_save.commit()

    def makethread():
        make_calander(num)
        make_player_stats(num)
    make_thread = threading.Thread(target=makethread)
    make_thread.daemon = True
    make_thread.start()


def time_auto_save():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    now = time.localtime()
    Date = ("%04d년 %02d월 %02d일 %02d시 %02d분 %02d초" % (now.tm_year, now.tm_mon,
                                                     now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
    cursor.execute(f"UPDATE Gamer Set Date= '{Date}'")
    db.commit()


###############################################################################
# 데이터 불러오기
###############################################################################
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
    db.commit()
    db_load.commit()
    db_save.commit()


def load2_data():
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
    db.commit()
    db_load.commit()
    db_save.commit()


###############################################################################
# 데이터 리셋
###############################################################################
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
    reset_message = tkinter.messagebox.showinfo(
        "리셋 완료", f"정보를 모두 리셋했습니다.")


###############################################################################
# 데이터 체크
###############################################################################
def Check_Savefiles(savefile):
    db = sqlite3.connect(f"DB/FO_savefile{savefile}.db")
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM Gamer ORDER BY Date DESC")
    Save_list = cursor.fetchone()
    return Save_list


def check_money():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM Gamer")
    Save_list = cursor.fetchone()[3]
    return Save_list


def check_myteam():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT COUNT(*) FROM Gamer_Team")
    count = cursor.fetchone()[0]
    return int(count)


###############################################################################
# 데이터 변경
###############################################################################
def give_money(money):
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"UPDATE Gamer SET Money ='{money}'")
    db.commit()
    return 0


def save_buy_team(Team):
    Warning_message = tkinter.messagebox.askokcancel(
        "인수", "정말 팀을 인수하시겠습니까?")
    if Warning_message == True:
        db = sqlite3.connect(f"DB/FO_savefile3.db")
        cursor = db.cursor()
        cursor.execute(
            f"SELECT COUNT(*) FROM Gamer_Team")
        count = cursor.fetchone()[0]
        cursor.execute(
            f"SELECT Money From Gamer")
        money = cursor.fetchone()[0]
        sale = int(Team[4])
        if count < 1 and money > sale:
            cursor.execute(
                f"INSERT INTO Gamer_Team VALUES{Team}")
            db.commit()
            Save_message = tkinter.messagebox.showinfo(
                "인수 완료", f"{Team[3]} 팀을 인수했습니다.")
            cursor.execute(
                f'UPDATE Gamer SET Money ="{money-sale}"')
            cursor.execute(
                f'UPDATE Gamer SET Team ="{Team[3]}"')
            db.commit()
        else:
            no_message = tkinter.messagebox.showinfo(
                "인수 불가", f"돈이 부족하거나 1팀 이상 인수 불가합니다.")


def save_sell_team(Team):
    Warning_message = tkinter.messagebox.askokcancel(
        "매각", "정말 팀을 매각하시겠습니까?")
    if Warning_message == True:
        db = sqlite3.connect(f"DB/FO_savefile3.db")
        cursor = db.cursor()
        cursor.execute(
            f"SELECT COUNT(*) FROM Gamer_Team")
        count = cursor.fetchone()[0]
        cursor.execute(
            f"SELECT Money From Gamer")
        money = cursor.fetchone()[0]
        sale = int(Team[4])
        Seq = int(Team[0])
        cursor.execute(
            f'DELETE FROM Gamer_Team WHERE Seq=="{Seq}"')
        db.commit()
        Save_message = tkinter.messagebox.showinfo(
            "매각 완료", f"{Team[3]} 팀을 매각했습니다.")
        cursor.execute(
            f'UPDATE Gamer SET Money ="{money+sale}"')
        if count == 1:
            cursor.execute(
                f'UPDATE Gamer SET Team ="무직"')
        else:
            cursor.execute(
                f'SELECT Team From Gamer_Team')
            team_name = cursor.fetchone()[0]
            cursor.execute(
                f'UPDATE Gamer SET Team ="{team_name}"')
        db.commit()


def get_injury():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f'UPDATE Players SET Injury ="0"')
    db.commit()
    cursor.execute(
        f"SELECT Seq, Market_Value FROM Players WHERE Injury =='0' ORDER BY random()")
    ran_length = random.randrange(5, 3000)
    injury_list = []
    for i in range(ran_length):
        injury_list.append(cursor.fetchone())
    for i in range(ran_length):
        ran_injury = random.randrange(1, 50)
        for j in range(7):
            new_injury = random.randrange(1, 50)
            if ran_injury > new_injury:
                ran_injury = new_injury
        cursor.execute(
            f'UPDATE Players SET Injury ="{ran_injury}" WHERE Seq == "{injury_list[i][0]}"')
        db.commit()
    player_Data = []
    famous = 0
    for j in range(5):
        num = 0
        famous = 0
        for i in range(len(injury_list)):
            if famous < int(injury_list[i][1]):
                famous = int(injury_list[i][1])
                num = i
        player_Data.append(injury_list[num][0])
        injury_list.pop(num)
    return_list = []
    for i in player_Data:
        cursor.execute(
            f"SELECT * FROM Players WHERE Seq =='{i}'")
        return_list.append(cursor.fetchone())
    cursor.execute(
        f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f"SELECT * FROM Players WHERE Team = '{my_team}' AND Injury != '0'")
    return_list += cursor.fetchall()

###############################################################################
# 데이터 SELECT
###############################################################################


def mini_game():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    ran = random.randrange(1, 3001)
    cursor.execute(
        f"SELECT * FROM Players Where Seq = '{ran}'")
    a = cursor.fetchone()
    return a


def ran_team_ac(money):
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM Teams WHERE Value<='{money}' ORDER BY random()")
    acquistion_list = []
    for i in range(7):
        acquistion_list.append(cursor.fetchone())
    if money <= 30000:
        acquistion_list = []
        for i in range(7):
            acquistion_list.append(['', '', '', '돈을 더 모으고 오세요', '', ''])
    return acquistion_list


def my_team_ac():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT COUNT(*) FROM Gamer_Team")
    count = cursor.fetchone()[0]
    cursor.execute(
        f"SELECT * FROM Gamer_Team")
    acquistion_list = []
    for i in range(count):
        acquistion_list.append(cursor.fetchone())
    return acquistion_list


def team_players(sort, desc):
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT COUNT(*) FROM Players Where Team =="{my_team}"')
    count_player = cursor.fetchone()[0]
    player_list = []
    if int(desc) == 0:
        cursor.execute(
            f'SELECT * FROM Players Where Team =="{my_team}" Order By "{sort}"')
    else:
        cursor.execute(
            f'SELECT * FROM Players Where Team =="{my_team}" Order By "{sort}" DESC')

    for i in range(count_player):
        player = cursor.fetchone()[1:]
        player_list.append(player)
    return player_list


def team_coaches(sort, desc):
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT COUNT(*) FROM Coaches Where Team =="{my_team}"')
    count_coaches = cursor.fetchone()[0]
    coach_list = []
    if int(desc) == 0:
        cursor.execute(
            f'SELECT * FROM Coaches Where Team =="{my_team}" Order By "{sort}"')
    else:
        cursor.execute(
            f'SELECT * FROM Coaches Where Team =="{my_team}" Order By "{sort}" DESC')

    for i in range(count_coaches):
        coach = cursor.fetchone()[1:]
        coach_list.append(coach)
    return coach_list


def team_staffs(sort, desc):
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT COUNT(*) FROM Staffs Where Team =="{my_team}"')
    count_staffs = cursor.fetchone()[0]
    staff_list = []
    if int(desc) == 0:
        cursor.execute(
            f'SELECT * FROM Staffs Where Team =="{my_team}" Order By "{sort}"')
    else:
        cursor.execute(
            f'SELECT * FROM Staffs Where Team =="{my_team}" Order By "{sort}" DESC')

    for i in range(count_staffs):
        staff = cursor.fetchone()[1:]
        staff_list.append(staff)
    return staff_list


def team_manager_ability(my_team):
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f'SELECT * FROM Coaches Where Position =="Manager" AND Team ==(?)', (my_team,))
    Ability = cursor.fetchone()
    return Ability


def team_keeper_ability(my_team):
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f'SELECT count(*) FROM Players Where (Team ==(?) AND Injury ==(?)) AND Position == "Midfielder" ORDER By Ability DESC', (my_team, "0"))
    count = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT * FROM Players Where (Team ==(?) AND Injury ==(?)) AND Position == "Goalkeeper" ORDER By Ability DESC', (my_team, "0"))
    Ability = []
    for i in range(count):
        Ability.append(cursor.fetchone())
    return list(Ability)


def team_defender_ability(my_team):
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f'SELECT count(*) FROM Players Where (Team ==(?) AND Injury ==(?)) AND Position == "Defender" ORDER By Ability DESC', (my_team, "0"))
    count = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT * FROM Players Where (Team ==(?) AND Injury ==(?)) AND Position == "Defender" ORDER By Ability DESC', (my_team, "0"))
    Ability = []
    for i in range(count):
        Ability.append(cursor.fetchone())
    return list(Ability)


def team_midfielder_ability(my_team):
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f'SELECT count(*) FROM Players Where (Team ==(?) AND Injury ==(?)) AND Position == "Midfielder" ORDER By Ability DESC', (my_team, "0"))
    count = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT * FROM Players Where (Team ==(?) AND Injury ==(?)) AND Position == "Midfielder" ORDER By Ability DESC', (my_team, "0"))
    Ability = []
    for i in range(count):
        Ability.append(cursor.fetchone())
    return list(Ability)


def team_forward_ability(my_team):
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f'SELECT count(*) FROM Players Where (Team ==(?) AND Injury ==(?)) AND Position == "Forward" ORDER By Ability DESC', (my_team, "0"))
    count = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT * FROM Players Where (Team ==(?) AND Injury ==(?)) AND Position == "Forward" ORDER By Ability DESC', (my_team, "0"))
    Ability = []
    for i in range(count):
        Ability.append(cursor.fetchone())
    return list(Ability)


def team_coaches_ability():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT COUNT(*) AVG(Ablility) FROM Coaches Where Team ==(?)', (my_team,))
    Data = cursor.fetchone()
    count_coaches = int(Data[0])
    avg_ability = int(Data[1])
    return int(count_coaches + avg_ability)


def team_staffs_ability():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT COUNT(*) AVG(Ablility) FROM Staffs Where Team ==(?)', (my_team,))
    Data = cursor.fetchone()
    count_staffs = int(Data[0])
    avg_ability = int(Data[1])
    return int(count_staffs + avg_ability)


def rec_players(ability):
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM Players WHERE Potential <= (?) ORDER BY random()", (ability,))
    Data = []
    for i in range(3):
        Data.append(cursor.fetchone())
    return Data


def rec_coaches(ability):
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM Coaches WHERE Ability <= (?) ORDER BY random()", (ability,))
    Data = []
    for i in range(3):
        Data.append(cursor.fetchone())
    return Data


def rec_staffs(ability):
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM Staffs WHERE Ability <= (?) ORDER BY random()", (ability,))
    Data = []
    for i in range(3):
        Data.append(cursor.fetchone())
    return Data


def ran_sell_player():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM Players ORDER BY random()")
    Data = cursor.fetchone()
    return Data


def ran_sell_coach():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM Coaches ORDER BY random()")
    Data = cursor.fetchone()
    return Data


def ran_sell_staff():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT * FROM Staffs ORDER BY random()")
    Data = cursor.fetchone()
    return Data


def sell_my_team():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT Value FROM Teams Where Team ==(?)', (my_team))
    Team_value = int(cursor.fetchone()[0])
    minus_value = int(Team_value*(0.5))
    plus_value = int(Team_value(0.3))
    result = random.randrange(Team_value-minus_value, Team_value+plus_value)
    return result


def ability_ran_change():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT * FROM Players Where Team ==(?) ORDER BY random()', (my_team,))
    player_list = []
    random_list = []
    player = cursor.fetchone()
    player_seq = player[0]
    player_ability = player[7]
    player_potential = player[8]
    random = random.randrange(-2, 2)
    if player_ability+random > player_potential:
        cursor.execute(
            f'UPDATE Players SET ability = (?) Where Seq == (?)', (player_potential, player_seq))
    else:
        cursor.execute(
            f'UPDATE Players SET ability = (?) Where Seq == (?)', (player_ability+random, player_seq))
    db.commit()
    player_list.append(player)
    random_list.append(random)

    cursor.execute(
        f'SELECT * FROM Players Where Team !=(?) ORDER BY random()', (my_team,))
    for i in range(1000):
        player = cursor.fetchone()
        player_seq = player[0]
        player_ability = player[7]
        player_potential = player[8]
        random = random.randrange(-2, 2)
        if player_ability+random > player_potential:
            cursor.execute(
                f'UPDATE Players SET ability = (?) Where Seq == (?)', (player_potential, player_seq))
        else:
            cursor.execute(
                f'UPDATE Players SET ability = (?) Where Seq == (?)', (player_ability+random, player_seq))
        db.commit()
        player_list.append(player)
        random_list.append(random)
    return (player_list, random_list)


def fan_res():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT count(*) FROM League_Calander Where result != (?) AND (Home == (?) OR Away == (?))', ("0", my_team, my_team))
    count = int(cursor.fetchone()[0])
    if count < 5:
        return False
    else:
        cursor.execute(
            f'SELECT * FROM League_Calander Where result != (?) AND (Home == (?) OR Away == (?)) ORDER BY Seq DESC', ("0", my_team, my_team))
        score = 0
        for i in range(5):
            Data = cursor.fetchone()
            Home = str(Data[4])
            Away = str(Data[5])
            result = int(Data[6])
            if result == 3:
                score += 1
            elif result == 1:
                if Home == my_team:
                    score += 3
            elif result == 2:
                if Away == my_team:
                    score += 3
        return score


def pla_Res():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT count(*) From League_Calander Where result != (?) AND (Home == (?) OR Away == (?))', ("0", my_team, my_team))
    count = int(cursor.fetchone()[0])
    if count < 5:
        return False
    else:
        cursor.execute(
            f'SELECT * FROM League_Calander Where result != (?) AND (Home == (?) OR Away == (?)) ORDER BY Seq DESC', ("0", my_team, my_team))
        score = 0
        for i in range(5):
            Data = cursor.fetchone()
            Home = str(Data[4])
            Away = str(Data[5])
            result = int(Data[6])
            if result == 3:
                score += 1
            elif result == 1:
                if Home == my_team:
                    score += 3
            elif result == 2:
                if Away == my_team:
                    score += 3
        return score

###############################################################################
# 그 외
###############################################################################


def make_calander(num):
    db = sqlite3.connect(f"DB/FO_savefile{num}.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM League_Calander")
    db.commit()
    cursor.execute(
        f'SELECT count(*) From Leagues')
    league_count = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT Name, Country From Leagues')
    league_list = []
    for i in range(league_count):
        league_list.append(cursor.fetchone())
    seq = 0
    for k in range(league_count):
        cursor.execute(
            f'SELECT count(*) From Teams Where League == (?) AND Country == (?)', (league_list[k][0], league_list[k][1],))
        count = cursor.fetchone()[0]
        cursor.execute(
            f'SELECT Team From Teams WHERE League == (?) AND Country == (?)', (league_list[k][0], league_list[k][1],))
        Team_list = []
        for i in range(count):
            Team_list.append(cursor.fetchone()[0])
        calander_list = []
        for i in range(len(Team_list)):
            for j in range(1, len(Team_list)):
                inter = i + j
                if inter > len(Team_list)-1:
                    inter -= len(Team_list)
                calander_list.append((Team_list[i], Team_list[inter]))
        calander_sort_list = []
        for i in range(len(Team_list)-1):
            ran_num = [i+1 for i in range(len(Team_list))]
            for j in range(len(Team_list)):
                choicenum = random.choice(ran_num)
                ran_num.remove(choicenum)
                result = choicenum*(len(Team_list)-1)-len(Team_list)+i-1
                calander_sort_list.append(calander_list[result])
        for i in range(len(calander_sort_list)):
            seq += 1
            cursor.execute(
                f'INSERT INTO League_Calander VALUES("{seq}", "{league_list[k][1]}", "{league_list[k][0]}", "{i+1}", "{calander_sort_list[i][0]}", "{calander_sort_list[i][1]}","0")')
        db.commit()


def make_player_stats(num):
    db = sqlite3.connect(f"DB/FO_savefile{num}.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM Player_Stat")
    db.commit()
    cursor.execute(
        f'SELECT count(*) From Leagues')
    league_count = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT Name, Country From Leagues')
    league_list = []
    for i in range(league_count):
        league_list.append(cursor.fetchone())
    seq = 0
    all_team = []
    for k in range(league_count):
        cursor.execute(
            f'SELECT count(*) From Teams Where League == (?) AND Country == (?)', (league_list[k][0], league_list[k][1],))
        count = cursor.fetchone()[0]
        cursor.execute(
            f'SELECT Team From Teams WHERE League == (?) AND Country == (?)', (league_list[k][0], league_list[k][1],))
        Team_list = []
        for i in range(count):
            Team_list.append(cursor.fetchone()[0])
        all_team += Team_list
        player_list = []
        for i in range(len(Team_list)):
            cursor.execute(
                f'SELECT count(*) From Players WHERE Team == (?)', (Team_list[i]))
            player_cnt = cursor.fetchone()[0]
            cursor.execute(
                f'SELECT Team, Name From Players WHERE Team == (?)', (Team_list[i]))
            for i in range(player_cnt):
                player_list.append(cursor.fetchone())
        for i in range(len(player_list)):
            seq += 1
            cursor.execute(
                f'INSERT INTO Player_Stat VALUES("{seq}", "{league_list[k][1]}", "{league_list[k][0]}","{player_list[i][0]}","{player_list[i][1]}","0","0","0","0")')
        db.commit()


def play_game(Home, Away):
    Home_Team_manager = team_manager_ability(Home)
    Away_Team_manager = team_manager_ability(Away)
    if Home_Team_manager == None:
        H_manager_ability = 50
    else:
        H_manager_ability = int(Home_Team_manager[5])
    if Away_Team_manager == None:
        A_manager_ability = 50
    else:
        A_manager_ability = int(Away_Team_manager[5])
    H_try = H_manager_ability-A_manager_ability+20
    A_try = A_manager_ability-H_manager_ability+20
    H_keeper = team_keeper_ability(Home)
    A_keeper = team_keeper_ability(Away)
    H_defender = team_defender_ability(Home)
    A_defender = team_defender_ability(Away)
    H_midfielder = team_midfielder_ability(Home)
    A_midfielder = team_midfielder_ability(Away)
    H_forward = team_forward_ability(Home)
    A_forward = team_forward_ability(Away)
    try:
        H1_k_abil = H_keeper[0][7]
    except:
        H1_k_abil = 48
    try:
        A1_k_abil = A_keeper[0][7]
    except:
        A1_k_abil = 48
    try:
        H4_d_abil = H_defender[0][7] + H_defender[1][7] + \
            H_defender[2][7] + H_defender[3][7]
    except:
        H4_d_abil = 200
    try:
        A4_d_abil = A_defender[0][7] + A_defender[1][7] + \
            A_defender[2][7] + A_defender[3][7]
    except:
        A4_d_abil = 200
    try:
        H3_m_abil = H_midfielder[0][7] + \
            H_midfielder[1][7] + H_midfielder[2][7]
    except:
        H3_m_abil = 150
    try:
        A3_m_abil = A_midfielder[0][7] + \
            A_midfielder[1][7] + A_midfielder[2][7]
    except:
        A3_m_abil = 150
    try:
        H3_f_abil = H_forward[0][7] + H_forward[1][7] + H_midfielder[2][7]
    except:
        H3_f_abil = 150
    try:
        A3_f_abil = A_forward[0][7] + A_forward[1][7] + A_forward[2][7]
    except:
        A3_f_abil = 150

    if H_try < 10:
        H_try = 10
    if A_try < 10:
        A_try = 10
    if H_try > 27:
        H_try = 27
    if A_try > 27:
        A_try = 27
    order = []
    for i in range(H_try):
        order.append('H')
    for i in range(A_try):
        order.append('A')
    random.shuffle(order)
    goal1 = 0
    goal1per = 101
    goal2 = 0
    goal2per = 101
    for i in order:
        if i == 'H':
            chance_dif = int((H3_m_abil-A3_m_abil)/4)
            if chance_dif < 0:
                chance_dif = int(chance_dif/2)
            ran = random.randrange(1, goal1per)
            if 60+chance_dif < ran:
                # print("찬스메이킹 실패1")
                continue
            pk_chance = int(H3_f_abil/100)
            ran = random.randrange(1, goal1per)
            if 1+pk_chance >= ran:
                # print("pk chance1")
                ran = random.randrange(1, goal1per)
                if ran <= 70:
                    # print("pk 성공1")
                    goal1per += 15
                    goal1 += 1
                    continue
                else:
                    # print("pk 실패1")
                    continue
            supersave_chance = int(A1_k_abil/10)
            ran = random.randrange(1, goal1per)
            if 1+supersave_chance >= ran:
                # print("슈퍼세이브2")
                continue
            goal_dif = int(((H3_f_abil + H3_m_abil) -
                            (A4_d_abil + (A1_k_abil)))/16)
            ran = random.randrange(1, goal1per)
            if goal_dif + 20 >= ran:
                # print("골1")
                goal1per += 15
                goal1 += 1
            else:
                # print("아 슛팅이 빗나갑니다!1")
                continue
            ran = random.randrange(1, goal1per)
            if ran <= 2:
                goal1per -= 15
                goal1 -= 1
                # print("VAR 취소...")
        else:
            chance_dif = int((A3_m_abil - H3_m_abil)/4)
            if chance_dif < 0:
                chance_dif = int(chance_dif/2)
            ran = random.randrange(1, goal2per)
            if 50+chance_dif < ran:
                # print("찬스메이킹 실패2")
                continue
            pk_chance = int(A3_f_abil/100)
            ran = random.randrange(1, goal2per)
            if 1+pk_chance >= ran:
                # print("pk chance2")
                ran = random.randrange(1, goal2per)
                if ran <= 70:
                    # print("pk 성공2")
                    goal2per += 15
                    goal2 += 1
                else:
                    # print("pk 실패2")
                    continue
            supersave_chance = int(H1_k_abil/10)
            ran = random.randrange(1, goal2per)
            if 1+supersave_chance >= ran:
                # print("슈퍼세이브1")
                continue
            goal_dif = int(((A3_f_abil + A3_m_abil) -
                            (H4_d_abil + (H1_k_abil)))/16)
            ran = random.randrange(1, goal2per)
            if goal_dif + 10 >= ran:
                # print("골2")
                goal2per += 15
                goal2 += 1
            else:
                # print("아 슛팅이 빗나갑니다!2")
                continue
            ran = random.randrange(1, goal2per)
            if ran <= 2:
                goal1per -= 15
                goal2 -= 1
                # print("VAR 취소...")
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f'UPDATE League_Calander SET result=(?) WHERE Home == (?) AND Away == (?)', (f"{goal1}:{goal2}", Home, Away))
    db.commit()


def match_progress(num):
    def makethread():
        lodate = date
        print(f"{lodate} 쓰레드 시작")
        db = sqlite3.connect(f"DB/FO_savefile3.db")
        cursor = db.cursor()
        # prepared sql python sqlite
        cursor.execute(
            'SELECT Home, Away FROM League_Calander WHERE Date == (?) AND result=="0"', (lodate,))
        # cursor.execute(
        #     f'SELECT Home, Away FROM League_Calander WHERE Date == "{lodate}" AND result=="0"')
        li = cursor.fetchall()
        for i in range(len(li)):
            play_game(li[i][0], li[i][1])
        print(f"{lodate} 쓰레드 끝")

    for i in range(1, num+1):
        date = i
        make_thread = threading.Thread(target=makethread)
        make_thread.daemon = True
        make_thread.start()
        time.sleep(0.05)


def search_calander():
    db = sqlite3.connect(f"DB/FO_savefile3.db")
    cursor = db.cursor()
    cursor.execute(
        f"SELECT Team FROM Gamer_Team")
    my_team = cursor.fetchone()[0]
    cursor.execute(
        f'SELECT * FROM League_Calander WHERE result==(?) AND (Home ==(?) or Away ==(?))', ("0", my_team, my_team,))
    return cursor.fetchone()


def one_position():
    db = sqlite3.connect(f"DB/FO_datafile.db")
    cursor = db.cursor()
    cursor.execute(
        f'UPDATE Players Set Position= "Defender" Where Position like "%Back" OR Position =="Defender"')
    db.commit()
    cursor.execute(
        f'UPDATE Players Set Position= "Midfielder" Where Position like "%Midfield" OR Position == "Midfielder"')
    db.commit()
    cursor.execute(
        f'UPDATE Players Set Position= "Forward" Where Position like "Second%" OR Position like "%Forward"')
    db.commit()
    cursor.execute(
        f'SELECT * FROM Players Group by Position')
    print(cursor.fetchall())
