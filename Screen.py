from Make_label import Get_label
from Use_data import *
from tkinter import *
import time


class Screen:
    def __init__(self, Gui):
        self.Gui = Gui
        self.Menu_Screen()

    def _quit(self):
        answer = messagebox.askyesno("확인", "정말 종료하시겠습니까?")
        if answer == True:
            self.Gui.Gui.quit()
            self.Gui.Gui.destroy()
            exit()

    def no_action(self):
        pass

    def destroy(self):
        list1 = self.Gui.Gui.place_slaves()
        for l in list1:
            l.destroy()

    ############################################################################################################################################################################################
    # 첫 메뉴 화면
    ############################################################################################################################################################################################
    def Menu_Screen(self):
        Menu_Screen_background = Get_label.image_label(
            self.Gui, "Title_Screen_bg.png", 0, 0)
        Game_Start_button = Get_label.image_button(
            self.Gui, "Game_Start_btn.png", 20, 350, self.loadfiles_Screen)
        HowToPlay_button = Get_label.image_button(
            self.Gui, "HowToPlay_btn.png", 20, 450, self.HowToPlay_Screen)
        Settings_button = Get_label.image_button(
            self.Gui, "Settings_btn.png", 20, 550, self.Incomplete_Screen)
        Exit_button = Get_label.image_button(
            self.Gui, "Exit_btn.png", 20, 650, self._quit)
        Version_label = Label(self.Gui.Gui, text="Version 0.4",
                              fg="yellow", bg="purple", font=("맑은 고딕", 12), height=1)
        Version_label.place(x=1100, y=5)

    ############################################################################################################################################################################################
    # 미완성 화면
    ############################################################################################################################################################################################
    def Incomplete_Screen(self):
        self.destroy()
        Incomplete_Screen_background = Get_label.image_label(
            self.Gui, "Incomplete_bg.png", 0, 0)
        Return_button = Get_label.image_button(
            self.Gui, "Return_btn.png", 920, 10, self.Menu_Screen)
        reset_datas_btn = Button(self.Gui.Gui, text="reset datas",
                                 bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21, command=reset_datas)
        reset_datas_btn.place(x=75, y=198)

    ############################################################################################################################################################################################
    # 설명 화면
    ############################################################################################################################################################################################
    def HowToPlay_Screen(self):
        self.destroy()
        HowToPlay_Screen_background = Get_label.image_label(
            self.Gui, "HowToPlay_bg.png", 0, 0)
        Return_button = Get_label.image_button(
            self.Gui, "Return_btn.png", 920, 10, self.Menu_Screen)

    ############################################################################################################################################################################################
    # 세이브 화면
    ############################################################################################################################################################################################

    def Savefiles_Screen(self):
        self.destroy()
        time_save = time_auto_save()

        def save1():
            save = Save1_data()
            MainScreen = self.Main_Screen()

        def save2():
            save = Save2_data()
            MainScreen = self.Main_Screen()

        Savefiles_Screen_background = Get_label.image_label(
            self.Gui, "Savefiles_bg.png", 0, 0)
        Return_button = Get_label.image_button(
            self.Gui, "Return_btn.png", 885, 44, self.Main_Screen)
        Save_check1 = Check_Savefiles(1)
        Save_check2 = Check_Savefiles(2)
        Save_check3 = Check_Savefiles(3)
        if Save_check1 == None:
            first_save_btn = Get_label.image_button_text(
                self.Gui, "Save_label.png", 82, 198, save1, f"+", "#407F7F", ("1훈떡볶이 Regular", 26))
        else:
            first_save_btn = Get_label.image_button_text(
                self.Gui, "Save_label.png", 82, 198, save1, f"☆ 구단주 이름 : {Save_check1[0]}     ☆ 현재 자금 : {Save_check1[3]}만원\n☆ 소속 팀 : {Save_check1[1]}\n☆ 저장 날짜 : {Save_check1[2]}", "#407F7F", ("1훈떡볶이 Regular", 24))
        if Save_check2 == None:
            second_save_btn = Get_label.image_button_text(
                self.Gui, "Save_label.png", 82, 398, save2, f"+", "#407F7F", ("1훈떡볶이 Regular", 26))
        else:
            second_save_btn = Get_label.image_button_text(
                self.Gui, "Save_label.png", 82, 398, save2, f"☆ 구단주 이름 : {Save_check2[0]}     ☆ 현재 자금 : {Save_check2[3]}만원\n☆ 소속 팀 : {Save_check2[1]}\n☆ 저장 날짜 : {Save_check2[2]}", "#407F7F", ("1훈떡볶이 Regular", 24))
        if Save_check3 == None:
            third_save_btn = Get_label.image_button_text(
                self.Gui, "Save_label.png", 82, 598, self.no_action, f"자동 저장 된 정보가 없습니다", "#407F7F", ("1훈떡볶이 Regular", 26))
        else:
            third_save_btn = Get_label.image_button_text(
                self.Gui, "Save_label.png", 82, 598, self.no_action, f"☆ 구단주 이름 : {Save_check3[0]}     ☆ 현재 자금 : {Save_check3[3]}만원\n☆ 소속 팀 : {Save_check3[1]}\n☆ 저장 날짜 : {Save_check3[2]}", "#407F7F", ("1훈떡볶이 Regular", 24))

    ############################################################################################################################################################################################
    # 불러오기 화면
    ############################################################################################################################################################################################
    def loadfiles_Screen(self):
        self.destroy()
        time_save = time_auto_save()

        def load1():
            load = load1_data()
            MainScreen = self.Main_Screen()

        def load2():
            load = load2_data()
            MainScreen = self.Main_Screen()

        def first():
            name_save = input_Names1()
            data = Auto_save_get_data(1)
            load = load1_data()
            MainScreen = self.Main_Screen()

        def second():
            name_save = input_Names2()
            data = Auto_save_get_data(2)
            load = load2_data()
            MainScreen = self.Main_Screen()

        Savefiles_Screen_background = Get_label.image_label(
            self.Gui, "Loadfiles_bg.png", 0, 0)
        Return_button = Get_label.image_button(
            self.Gui, "Return_btn.png", 45, 44, self.Menu_Screen)
        Save_check1 = Check_Savefiles(1)
        Save_check2 = Check_Savefiles(2)
        Save_check3 = Check_Savefiles(3)
        if Save_check1 == None:
            first_save_btn = Get_label.image_button_text(
                self.Gui, "Save_label.png", 395, 198, first, f"+", "#407F7F", ("1훈떡볶이 Regular", 26))
        else:
            first_save_btn = Get_label.image_button_text(
                self.Gui, "Save_label.png", 395, 198, load1, f"☆ 구단주 이름 : {Save_check1[0]}     ☆ 현재 자금 : {Save_check1[3]}만원\n☆ 소속 팀 : {Save_check1[1]}\n☆ 저장 날짜 : {Save_check1[2]}", "#407F7F", ("1훈떡볶이 Regular", 24))
        if Save_check2 == None:
            second_save_btn = Get_label.image_button_text(
                self.Gui, "Save_label.png", 395, 398, second, f"+", "#407F7F", ("1훈떡볶이 Regular", 26))
        else:
            second_save_btn = Get_label.image_button_text(
                self.Gui, "Save_label.png", 395, 398, load2, f"☆ 구단주 이름 : {Save_check2[0]}     ☆ 현재 자금 : {Save_check2[3]}만원\n☆ 소속 팀 : {Save_check2[1]}\n☆ 저장 날짜 : {Save_check2[2]}", "#407F7F", ("1훈떡볶이 Regular", 24))
        if Save_check3 == None:
            third_save_btn = Get_label.image_button_text(
                self.Gui, "Save_label.png", 395, 598, self.no_action, f"자동 저장 된 정보가 없습니다", "#407F7F", ("1훈떡볶이 Regular", 26))
        else:
            third_save_btn = Get_label.image_button_text(
                self.Gui, "Save_label.png", 395, 598, self.Main_Screen, f"☆ 구단주 이름 : {Save_check3[0]}     ☆ 현재 자금 : {Save_check3[3]}만원\n☆ 소속 팀 : {Save_check3[1]}\n☆ 저장 날짜 : {Save_check3[2]}", "#407F7F", ("1훈떡볶이 Regular", 24))

    ############################################################################################################################################################################################
    # 메인 게임 화면
    ############################################################################################################################################################################################

    def Main_Screen(self):
        self.destroy()
        Menu_Screen_background = Get_label.image_label(
            self.Gui, "Main_Screen_bg.png", 0, 0)
        self.game_buttons()
        self.message()

    def game_buttons(self):
        Logo_button = Get_label.image_button(
            self.Gui, "logo_btn.png", 31, 33, self.logo_com)
        Save_button = Get_label.image_button(
            self.Gui, "save_btn.png", 121, 33, self.Savefiles_Screen)
        Go_button = Get_label.image_button(
            self.Gui, "go_btn.png", 1090, 33, self.no_action)
        self.menu1_button = Get_label.image_button(
            self.Gui, "menu1.png", 34, 140, self.message)
        self.menu2_button = Get_label.image_button(
            self.Gui, "menu2.png", 34, 210, self.no_action)
        self.menu3_button = Get_label.image_button(
            self.Gui, "menu3.png", 34, 280, self.acquisition)
        self.menu4_button = Get_label.image_button(
            self.Gui, "menu4.png", 34, 350, self.no_action)
        self.menu5_button = Get_label.image_button(
            self.Gui, "menu5.png", 34, 420, self.Team_Player_Screen)
        self.menu6_button = Get_label.image_button(
            self.Gui, "menu6.png", 34, 490, self.Team_Coach_Screen)
        self.menu7_button = Get_label.image_button(
            self.Gui, "menu7.png", 34, 560, self.Team_Staff_Screen)
        self.menu8_button = Get_label.image_button(
            self.Gui, "menu8.png", 34, 630, self.no_action)
        self.menu9_button = Get_label.image_button(
            self.Gui, "menu9.png", 34, 700, self.no_action)

    def logo_com(self):
        time_save = time_auto_save()
        answer = messagebox.askyesno("확인", "정말 메인화면으로 돌아가시겠습니까?")
        if answer == True:
            screen = self.Menu_Screen()

    ############################################################################################################################################################################################
    # 메세지 화면
    ############################################################################################################################################################################################
    def message(self):
        self.destroy()
        check_mon = check_money()
        if check_mon == '-':
            self.menu1_button.config(state='disabled')
            self.menu2_button.config(state='disabled')
            self.menu3_button.config(state='disabled')
            self.menu4_button.config(state='disabled')
            self.menu5_button.config(state='disabled')
            self.menu6_button.config(state='disabled')
            self.menu7_button.config(state='disabled')
            self.menu8_button.config(state='disabled')
            self.menu9_button.config(state='disabled')
            self.get_first_money()
        else:
            Message_Screen_background = Get_label.image_label(
                self.Gui, "message_box_bg.png", 0, 0)
            self.game_buttons()
            message_notice1 = Get_label.image_button(
                self.Gui, "message_notice_btn.png", 219, 130, self.no_action)
            message_notice1 = Get_label.image_button(
                self.Gui, "message_notice_btn.png", 219, 260, self.no_action)
            message_notice1 = Get_label.image_button(
                self.Gui, "message_notice_btn.png", 219, 390, self.no_action)
            message_notice1 = Get_label.image_button(
                self.Gui, "message_notice_btn.png", 219, 520, self.no_action)
            message_notice1 = Get_label.image_button(
                self.Gui, "message_notice_btn.png", 219, 650, self.no_action)

    ############################################################################################################################################################################################
    # 미니게임 화면
    ############################################################################################################################################################################################
    def get_first_money(self):
        self.money = 10000
        self.win = 0
        Name = Get_label.image_label(
            self.Gui, "Name_Tag.png", 250, 40)
        Intro1 = Get_label.image_label(
            self.Gui, "intro1.png", 245, 170)
        Intro2 = Get_label.image_label_text(
            self.Gui, "intro2.png", 250, 345, f"                {self.win}번", "#ed1c24", ("1훈떡볶이 Regular", 32))
        Intro3 = Get_label.image_label_text(
            self.Gui, "intro3.png", 600, 345, f"             {self.money}원", "#ed1c24", ("1훈떡볶이 Regular", 32))
        start = self.MINI_Game()

    def MINI_Game(self):
        self.first_player = mini_game()
        self.first_value = int(self.first_player[6])
        self.second_player = mini_game()
        self.second_value = int(self.second_player[6])
        self.bg1 = Get_label.image_button_text(
            self.Gui, "bg1.png", 250, 445, self.select1, f"\n이름 : {self.first_player[1]}\n팀 : {self.first_player[2]}\n등번호 : {self.first_player[3]}\n포지션 {self.first_player[4]}\n나이 : {self.first_player[5]}\n", "#472f91", ("타이포_헬로피오피 테두리B", 20))
        self.bg2 = Get_label.image_button_text(
            self.Gui, "bg1.png", 720, 445, self.select2, f"\n이름 : {self.second_player[1]}\n팀 : {self.second_player[2]}\n등번호 : {self.second_player[3]}\n포지션 {self.second_player[4]}\n나이 : {self.second_player[5]}\n", "#472f91", ("타이포_헬로피오피 테두리B", 20))

    def select1(self):
        self.bg1 = Get_label.image_button_text(
            self.Gui, "bg1.png", 250, 445, self.no_action, f"\n이름 : {self.first_player[1]}\n\n선수가치 : {self.first_value}\n", "#28a44a", ("타이포_헬로피오피 테두리B", 26))
        self.bg2 = Get_label.image_button_text(
            self.Gui, "bg1.png", 720, 445, self.no_action, f"\n이름 : {self.second_player[1]}\n\n선수가치 : {self.second_value}\n", "#28a44a", ("타이포_헬로피오피 테두리B", 26))

        if self.first_value >= self.second_value:
            self.bg2.after(2000, self.wait_answer)
        else:
            self.bg1.config(state='disabled')
            self.bg2.config(state='disabled')
            self.finished()

    def select2(self):
        self.bg1 = Get_label.image_button_text(
            self.Gui, "bg1.png", 250, 445, self.no_action, f"\n이름 : {self.first_player[1]}\n\n선수가치 : {self.first_value}\n", "#28a44a", ("타이포_헬로피오피 테두리B", 26))
        self.bg2 = Get_label.image_button_text(
            self.Gui, "bg1.png", 720, 445, self.no_action, f"\n이름 : {self.second_player[1]}\n\n선수가치 : {self.second_value}\n", "#28a44a", ("타이포_헬로피오피 테두리B", 26))

        if self.first_value <= self.second_value:
            self.bg2.after(3000, self.wait_answer)
        else:
            self.bg1.config(state='disabled')
            self.bg2.config(state='disabled')
            self.finished()

    def wait_answer(self):
        self.money *= 2
        self.win += 1
        Intro2 = Get_label.image_label_text(
            self.Gui, "intro2.png", 250, 345, f"                {self.win}번", "#472f91", ("1훈떡볶이 Regular", 32))
        Intro3 = Get_label.image_label_text(
            self.Gui, "intro3.png", 600, 345, f"             {self.money}원", "#472f91", ("1훈떡볶이 Regular", 32))
        restart = self.MINI_Game()

    def finished(self):
        if self.money <= 30000:
            self.money = 30000
        update_money = give_money(self.money)

        self.bg2.after(4000, self.Main_Screen)

    ############################################################################################################################################################################################
    # 인수 / 매각 화면
    ############################################################################################################################################################################################

    def acquisition(self):
        self.destroy()
        Message_Screen_background = Get_label.image_label(
            self.Gui, "acquisition_bg.png", 0, 0)
        self.game_buttons()
        money = int(check_money())
        myteam = check_myteam()
        self.myteam_info = my_team_ac()
        self.acquisition_list = ran_team_ac(money)
        self.Intro1 = Get_label.image_label_text(
            self.Gui, "ac1.png", 302, 138, f"팀 이름", "#472f91", ("고도 M", 12))
        self.Intro2 = Get_label.image_label_text(
            self.Gui, "ac2.png", 572, 138,  f"인수 가격", "#472f91", ("고도 M", 12))
        self.Intro3 = Get_label.image_label_text(
            self.Gui, "ac3.png", 722, 138,  f"속한 나라", "#472f91", ("고도 M", 12))
        self.Intro4 = Get_label.image_label_text(
            self.Gui, "ac4.png", 952, 138,  f"속한 리그", "#472f91", ("고도 M", 12))
        for i in range(7):
            team1 = Get_label.image_label_text(
                self.Gui, "ac1-1.png", 302, 188+(50*i), f"{self.acquisition_list[i][3]}", "#472f91", ("고도 M", 12))
            team2 = Get_label.image_label_text(
                self.Gui, "ac2-1.png", 572, 188+(50*i), f"{self.acquisition_list[i][4]} 만원", "#472f91", ("고도 M", 12))
            team3 = Get_label.image_label_text(
                self.Gui, "ac3-1.png", 722, 188+(50*i), f"{self.acquisition_list[i][2]}", "#472f91", ("고도 M", 12))
            team4 = Get_label.image_label_text(
                self.Gui, "ac4-1.png", 952, 188+(50*i), f"{self.acquisition_list[i][1]}", "#472f91", ("고도 M", 10))
        Team_label1 = Get_label.image_button(
            self.Gui, "acquisition_btn1.png", 222, 188+(50*0), self.buy1)
        Team_label2 = Get_label.image_button(
            self.Gui, "acquisition_btn1.png", 222, 188+(50*1), self.buy2)
        Team_label3 = Get_label.image_button(
            self.Gui, "acquisition_btn1.png", 222, 188+(50*2), self.buy3)
        Team_label4 = Get_label.image_button(
            self.Gui, "acquisition_btn1.png", 222, 188+(50*3), self.buy4)
        Team_label5 = Get_label.image_button(
            self.Gui, "acquisition_btn1.png", 222, 188+(50*4), self.buy5)
        Team_label6 = Get_label.image_button(
            self.Gui, "acquisition_btn1.png", 222, 188+(50*5), self.buy6)
        Team_label7 = Get_label.image_button(
            self.Gui, "acquisition_btn1.png", 222, 188+(50*6), self.buy7)

        self.Intro5 = Get_label.image_label_text(
            self.Gui, "ac1.png", 302, 575, f"팀 이름", "#472f91", ("고도 M", 12))
        self.Intro6 = Get_label.image_label_text(
            self.Gui, "ac2.png", 572, 575,  f"인수 가격", "#472f91", ("고도 M", 12))
        self.Intro7 = Get_label.image_label_text(
            self.Gui, "ac3.png", 722, 575,  f"속한 나라", "#472f91", ("고도 M", 12))
        self.Intro8 = Get_label.image_label_text(
            self.Gui, "ac4.png", 952, 575,  f"속한 리그", "#472f91", ("고도 M", 12))
        for i in range(myteam):
            team1 = Get_label.image_label_text(
                self.Gui, "ac1-1.png", 302, 625+(50*i), f"{self.myteam_info[i][3]}", "#472f91", ("고도 M", 12))
            team2 = Get_label.image_label_text(
                self.Gui, "ac2-1.png", 572, 625+(50*i), f"{self.myteam_info[i][4]} 만원", "#472f91", ("고도 M", 12))
            team3 = Get_label.image_label_text(
                self.Gui, "ac3-1.png", 722, 625+(50*i), f"{self.myteam_info[i][2]}", "#472f91", ("고도 M", 12))
            team4 = Get_label.image_label_text(
                self.Gui, "ac4-1.png", 952, 625+(50*i), f"{self.myteam_info[i][1]}", "#472f91", ("고도 M", 10))
        if myteam == 1:
            Team_label8 = Get_label.image_button(
                self.Gui, "acquisition_btn2.png", 222, 625+(50*0), self.sell1)
        elif myteam == 2:
            Team_label8 = Get_label.image_button(
                self.Gui, "acquisition_btn2.png", 222, 625+(50*0), self.sell1)
            Team_label8 = Get_label.image_button(
                self.Gui, "acquisition_btn2.png", 222, 625+(50*1), self.sell2)
        else:
            Team_label8 = Get_label.image_button(
                self.Gui, "acquisition_btn2.png", 222, 625+(50*0), self.sell1)
            Team_label9 = Get_label.image_button(
                self.Gui, "acquisition_btn2.png", 222, 625+(50*1), self.sell2)
            Team_label10 = Get_label.image_button(
                self.Gui, "acquisition_btn2.png", 222, 625+(50*2), self.sell3)

    def buy1(self):
        save_buy_team(self.acquisition_list[0])
        self.acquisition()

    def buy2(self):
        save_buy_team(self.acquisition_list[1])
        self.acquisition()

    def buy3(self):
        save_buy_team(self.acquisition_list[2])
        self.acquisition()

    def buy4(self):
        save_buy_team(self.acquisition_list[3])
        self.acquisition()

    def buy5(self):
        save_buy_team(self.acquisition_list[4])
        self.acquisition()

    def buy6(self):
        save_buy_team(self.acquisition_list[5])
        self.acquisition()

    def buy7(self):
        save_buy_team(self.acquisition_list[6])
        self.acquisition()

    def sell1(self):
        save_sell_team(self.myteam_info[0])
        self.acquisition()

    def sell2(self):
        save_sell_team(self.myteam_info[1])
        self.acquisition()

    def sell3(self):
        save_sell_team(self.myteam_info[2])
        self.acquisition()

    ############################################################################################################################################################################################
    # 팀 선수단 화면
    ############################################################################################################################################################################################

    def Team_Player_Screen(self):
        team_count = check_myteam()
        if team_count == 0:
            Team_Player_Screen_background = Get_label.image_label(
                self.Gui, "cantuse_bg.png", 0, 0)
            game_button = self.game_buttons()
        else:
            self.sort_num = 0
            self.sort_color = 0
            self.players = team_players('Position', self.sort_num)
            fir = self.first_player_scr()

    def first_player_scr(self):
        self.destroy()
        Team_Player_Screen_background = Get_label.image_label(
            self.Gui, "Main_Screen_bg.png", 0, 0)
        game_button = self.game_buttons()
        right_button = Get_label.image_button(
            self.Gui, "right.png", 980, 43, self.second_player_scr)
        left_button = Get_label.image_button(
            self.Gui, "left.png", 900, 43, self.no_action)
        left_button.config(state='disabled')
        self.len_player = len(self.players)
        if self.len_player < 16:
            right_button.config(state='disabled')
        self.Intro1 = Get_label.image_button_text(
            self.Gui, "player1.png", 222, 133, self.sortpla1, f"번호", "#472f91", ("고도 M", 12))
        self.Intro2 = Get_label.image_button_text(
            self.Gui, "player2.png", 282, 133, self.sortpla2, f"이름", "#472f91", ("고도 M", 12))
        self.Intro3 = Get_label.image_button_text(
            self.Gui, "player3.png", 542, 133, self.sortpla3, f"포지션", "#472f91", ("고도 M", 12))
        self.Intro4 = Get_label.image_button_text(
            self.Gui, "player4.png", 742, 133, self.sortpla4, f"나이", "#472f91", ("고도 M", 12))
        self.Intro5 = Get_label.image_button_text(
            self.Gui, "player5.png", 802, 133, self.sortpla5, f"선수 가치", "#472f91", ("고도 M", 12))
        self.Intro6 = Get_label.image_button_text(
            self.Gui, "player6.png", 932, 133, self.sortpla6, f"능력치", "#472f91", ("고도 M", 12))
        self.Intro7 = Get_label.image_button_text(
            self.Gui, "player7.png", 992, 133, self.sortpla7, f"잠재력", "#472f91", ("고도 M", 12))
        self.Intro8 = Get_label.image_button_text(
            self.Gui, "player8.png", 1052, 133, self.sortpla8, f"선수 주급", "#472f91", ("고도 M", 12))
        if self.sort_color == 1:
            fir = self.change_pla_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_pla_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_pla_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_pla_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_pla_sortnum()
            self.Intro5.config(fg="#B30000")
        elif self.sort_color == 6:
            fir = self.change_pla_sortnum()
            self.Intro6.config(fg="#B30000")
        elif self.sort_color == 7:
            fir = self.change_pla_sortnum()
            self.Intro7.config(fg="#B30000")
        elif self.sort_color == 8:
            fir = self.change_pla_sortnum()
            self.Intro8.config(fg="#B30000")
        first_len = 0
        if self.len_player > 14:
            first_len = 15
        else:
            first_len = self.len_player
        for i in range(first_len):
            pla1 = Get_label.image_label_text(
                self.Gui, "player1-1.png", 222, 173+(40*i), f"{self.players[i][2]}", "#472f91", ("고도 M", 12))
            pla2 = Get_label.image_label_text(
                self.Gui, "player2-1.png", 282, 173+(40*i), f"{self.players[i][0]}", "#472f91", ("고도 M", 12))
            pla3 = Get_label.image_label_text(
                self.Gui, "player3-1.png", 542, 173+(40*i), f"{self.players[i][3]}", "#472f91", ("고도 M", 12))
            pla4 = Get_label.image_label_text(
                self.Gui, "player4-1.png", 742, 173+(40*i), f"{self.players[i][4]}", "#472f91", ("고도 M", 12))
            pla5 = Get_label.image_label_text(
                self.Gui, "player5-1.png", 802, 173+(40*i), f"{self.players[i][5]} 만원", "#472f91", ("고도 M", 12))
            pla6 = Get_label.image_label_text(
                self.Gui, "player6-1.png", 932, 173+(40*i), f"{self.players[i][6]}", "#472f91", ("고도 M", 12))
            pla7 = Get_label.image_label_text(
                self.Gui, "player7-1.png", 992, 173+(40*i), f"{self.players[i][7]}", "#472f91", ("고도 M", 12))
            pla8 = Get_label.image_label_text(
                self.Gui, "player8-1.png", 1052, 173+(40*i), f"{self.players[i][8]} 만원", "#472f91", ("고도 M", 12))

    def second_player_scr(self):
        self.destroy()
        Team_Player_Screen_background = Get_label.image_label(
            self.Gui, "Main_Screen_bg.png", 0, 0)
        game_button = self.game_buttons()
        right_button = Get_label.image_button(
            self.Gui, "right.png", 980, 43, self.third_player_scr)
        left_button = Get_label.image_button(
            self.Gui, "left.png", 900, 43, self.first_player_scr)
        second_len = 0
        if self.len_player > 29:
            second_len = 15
        else:
            second_len = self.len_player-15
            right_button.config(state='disabled')
        self.Intro1 = Get_label.image_button_text(
            self.Gui, "player1.png", 222, 133, self.sortpla1, f"번호", "#472f91", ("고도 M", 12))
        self.Intro2 = Get_label.image_button_text(
            self.Gui, "player2.png", 282, 133, self.sortpla2, f"이름", "#472f91", ("고도 M", 12))
        self.Intro3 = Get_label.image_button_text(
            self.Gui, "player3.png", 542, 133, self.sortpla3, f"포지션", "#472f91", ("고도 M", 12))
        self.Intro4 = Get_label.image_button_text(
            self.Gui, "player4.png", 742, 133, self.sortpla4, f"나이", "#472f91", ("고도 M", 12))
        self.Intro5 = Get_label.image_button_text(
            self.Gui, "player5.png", 802, 133, self.sortpla5, f"선수 가치", "#472f91", ("고도 M", 12))
        self.Intro6 = Get_label.image_button_text(
            self.Gui, "player6.png", 932, 133, self.sortpla6, f"능력치", "#472f91", ("고도 M", 12))
        self.Intro7 = Get_label.image_button_text(
            self.Gui, "player7.png", 992, 133, self.sortpla7, f"잠재력", "#472f91", ("고도 M", 12))
        self.Intro8 = Get_label.image_button_text(
            self.Gui, "player8.png", 1052, 133, self.sortpla8, f"선수 주급", "#472f91", ("고도 M", 12))
        if self.sort_color == 1:
            fir = self.change_pla_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_pla_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_pla_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_pla_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_pla_sortnum()
            self.Intro5.config(fg="#B30000")
        elif self.sort_color == 6:
            fir = self.change_pla_sortnum()
            self.Intro6.config(fg="#B30000")
        elif self.sort_color == 7:
            fir = self.change_pla_sortnum()
            self.Intro7.config(fg="#B30000")
        elif self.sort_color == 8:
            fir = self.change_pla_sortnum()
            self.Intro8.config(fg="#B30000")
        for i in range(second_len):
            pla1 = Get_label.image_label_text(
                self.Gui, "player1-1.png", 222, 173+(40*i), f"{self.players[i+15][2]}", "#472f91", ("고도 M", 12))
            pla2 = Get_label.image_label_text(
                self.Gui, "player2-1.png", 282, 173+(40*i), f"{self.players[i+15][0]}", "#472f91", ("고도 M", 12))
            pla3 = Get_label.image_label_text(
                self.Gui, "player3-1.png", 542, 173+(40*i), f"{self.players[i+15][3]}", "#472f91", ("고도 M", 12))
            pla4 = Get_label.image_label_text(
                self.Gui, "player4-1.png", 742, 173+(40*i), f"{self.players[i+15][4]}", "#472f91", ("고도 M", 12))
            pla5 = Get_label.image_label_text(
                self.Gui, "player5-1.png", 802, 173+(40*i), f"{self.players[i+15][5]} 만원", "#472f91", ("고도 M", 12))
            pla6 = Get_label.image_label_text(
                self.Gui, "player6-1.png", 932, 173+(40*i), f"{self.players[i+15][6]}", "#472f91", ("고도 M", 12))
            pla7 = Get_label.image_label_text(
                self.Gui, "player7-1.png", 992, 173+(40*i), f"{self.players[i+15][7]}", "#472f91", ("고도 M", 12))
            pla8 = Get_label.image_label_text(
                self.Gui, "player8-1.png", 1052, 173+(40*i), f"{self.players[i+15][8]} 만원", "#472f91", ("고도 M", 12))

    def third_player_scr(self):
        self.destroy()
        Team_Player_Screen_background = Get_label.image_label(
            self.Gui, "Main_Screen_bg.png", 0, 0)
        game_button = self.game_buttons()
        right_button = Get_label.image_button(
            self.Gui, "right.png", 980, 43, self.second_player_scr)
        left_button = Get_label.image_button(
            self.Gui, "left.png", 900, 43, self.second_player_scr)

        right_button.config(state='disabled')
        third_len = self.len_player-30

        self.Intro1 = Get_label.image_button_text(
            self.Gui, "player1.png", 222, 133, self.sortpla1, f"번호", "#472f91", ("고도 M", 12))
        self.Intro2 = Get_label.image_button_text(
            self.Gui, "player2.png", 282, 133, self.sortpla2, f"이름", "#472f91", ("고도 M", 12))
        self.Intro3 = Get_label.image_button_text(
            self.Gui, "player3.png", 542, 133, self.sortpla3, f"포지션", "#472f91", ("고도 M", 12))
        self.Intro4 = Get_label.image_button_text(
            self.Gui, "player4.png", 742, 133, self.sortpla4, f"나이", "#472f91", ("고도 M", 12))
        self.Intro5 = Get_label.image_button_text(
            self.Gui, "player5.png", 802, 133, self.sortpla5, f"선수 가치", "#472f91", ("고도 M", 12))
        self.Intro6 = Get_label.image_button_text(
            self.Gui, "player6.png", 932, 133, self.sortpla6, f"능력치", "#472f91", ("고도 M", 12))
        self.Intro7 = Get_label.image_button_text(
            self.Gui, "player7.png", 992, 133, self.sortpla7, f"잠재력", "#472f91", ("고도 M", 12))
        self.Intro8 = Get_label.image_button_text(
            self.Gui, "player8.png", 1052, 133, self.sortpla8, f"선수 주급", "#472f91", ("고도 M", 12))
        if self.sort_color == 1:
            fir = self.change_pla_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_pla_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_pla_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_pla_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_pla_sortnum()
            self.Intro5.config(fg="#B30000")
        elif self.sort_color == 6:
            fir = self.change_pla_sortnum()
            self.Intro6.config(fg="#B30000")
        elif self.sort_color == 7:
            fir = self.change_pla_sortnum()
            self.Intro7.config(fg="#B30000")
        elif self.sort_color == 8:
            fir = self.change_pla_sortnum()
            self.Intro8.config(fg="#B30000")
        for i in range(third_len):
            pla1 = Get_label.image_label_text(
                self.Gui, "player1-1.png", 222, 173+(40*i), f"{self.players[i+30][2]}", "#472f91", ("고도 M", 12))
            pla2 = Get_label.image_label_text(
                self.Gui, "player2-1.png", 282, 173+(40*i), f"{self.players[i+30][0]}", "#472f91", ("고도 M", 12))
            pla3 = Get_label.image_label_text(
                self.Gui, "player3-1.png", 542, 173+(40*i), f"{self.players[i+30][3]}", "#472f91", ("고도 M", 12))
            pla4 = Get_label.image_label_text(
                self.Gui, "player4-1.png", 742, 173+(40*i), f"{self.players[i+30][4]}", "#472f91", ("고도 M", 12))
            pla5 = Get_label.image_label_text(
                self.Gui, "player5-1.png", 802, 173+(40*i), f"{self.players[i+30][5]} 만원", "#472f91", ("고도 M", 12))
            pla6 = Get_label.image_label_text(
                self.Gui, "player6-1.png", 932, 173+(40*i), f"{self.players[i+30][6]}", "#472f91", ("고도 M", 12))
            pla7 = Get_label.image_label_text(
                self.Gui, "player7-1.png", 992, 173+(40*i), f"{self.players[i+30][7]}", "#472f91", ("고도 M", 12))
            pla8 = Get_label.image_label_text(
                self.Gui, "player8-1.png", 1052, 173+(40*i), f"{self.players[i+30][8]} 만원", "#472f91", ("고도 M", 12))

    def sortpla1(self):
        self.players = team_players('Number', self.sort_num)
        self.sort_color = 1
        fir = self.first_player_scr()

    def sortpla2(self):
        self.players = team_players('Name', self.sort_num)
        self.sort_color = 2
        fir = self.first_player_scr()

    def sortpla3(self):
        self.players = team_players('Position', self.sort_num)
        self.sort_color = 3
        fir = self.first_player_scr()

    def sortpla4(self):
        self.players = team_players('Age', self.sort_num)
        self.sort_color = 4
        fir = self.first_player_scr()

    def sortpla5(self):
        self.players = team_players('Market_Value', self.sort_num)
        self.sort_color = 5
        fir = self.first_player_scr()

    def sortpla6(self):
        self.players = team_players('Ability', self.sort_num)
        self.sort_color = 6
        fir = self.first_player_scr()

    def sortpla7(self):
        self.players = team_players('Potential', self.sort_num)
        self.sort_color = 7
        fir = self.first_player_scr()

    def sortpla8(self):
        self.players = team_players('Money', self.sort_num)
        self.sort_color = 8
        fir = self.first_player_scr()

    def change_pla_sortnum(self):
        if self.sort_num == 0:
            self.sort_num = 1
        else:
            self.sort_num = 0
        self.Intro1.config(fg="#472f91")
        self.Intro2.config(fg="#472f91")
        self.Intro3.config(fg="#472f91")
        self.Intro4.config(fg="#472f91")
        self.Intro5.config(fg="#472f91")
        self.Intro6.config(fg="#472f91")
        self.Intro7.config(fg="#472f91")
        self.Intro8.config(fg="#472f91")

    ############################################################################################################################################################################################
    # 팀 코치단 화면
    ############################################################################################################################################################################################

    def Team_Coach_Screen(self):
        team_count = check_myteam()
        if team_count == 0:
            Team_Coach_Screen_background = Get_label.image_label(
                self.Gui, "cantuse_bg.png", 0, 0)
            game_button = self.game_buttons()
        else:
            self.sort_num = 0
            self.sort_color = 0
            self.coaches = team_coaches('Position', self.sort_num)
            fir = self.first_coach_scr()

    def first_coach_scr(self):
        self.destroy()
        Team_Coach_Screen_background = Get_label.image_label(
            self.Gui, "Main_Screen_bg.png", 0, 0)
        game_button = self.game_buttons()
        right_button = Get_label.image_button(
            self.Gui, "right.png", 980, 43, self.second_coach_scr)
        left_button = Get_label.image_button(
            self.Gui, "left.png", 900, 43, self.no_action)
        left_button.config(state='disabled')
        self.len_coach = len(self.coaches)
        if self.len_coach < 16:
            right_button.config(state='disabled')
        self.Intro1 = Get_label.image_button_text(
            self.Gui, "coach1.png", 222, 133, self.sortcoa1, f"이름", "#472f91", ("고도 M", 12))
        self.Intro2 = Get_label.image_button_text(
            self.Gui, "coach2.png", 552, 133, self.sortcoa2, f"포지션", "#472f91", ("고도 M", 12))
        self.Intro3 = Get_label.image_button_text(
            self.Gui, "coach3.png", 832, 133, self.sortcoa3, f"나이", "#472f91", ("고도 M", 12))
        self.Intro4 = Get_label.image_button_text(
            self.Gui, "coach4.png", 912, 133, self.sortcoa4, f"능력치", "#472f91", ("고도 M", 12))
        self.Intro5 = Get_label.image_button_text(
            self.Gui, "coach5.png", 992, 133, self.sortcoa5, f"주급", "#472f91", ("고도 M", 12))
        if self.sort_color == 1:
            fir = self.change_coa_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_coa_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_coa_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_coa_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_coa_sortnum()
            self.Intro5.config(fg="#B30000")
        first_len = 0
        if self.len_coach > 14:
            first_len = 15
        else:
            first_len = self.len_coach
        for i in range(first_len):
            coa1 = Get_label.image_label_text(
                self.Gui, "coach1-1.png", 222, 173+(40*i), f"{self.coaches[i][0]}", "#472f91", ("고도 M", 12))
            coa2 = Get_label.image_label_text(
                self.Gui, "coach2-1.png", 552, 173+(40*i), f"{self.coaches[i][2]}", "#472f91", ("고도 M", 12))
            coa3 = Get_label.image_label_text(
                self.Gui, "coach3-1.png", 832, 173+(40*i), f"{self.coaches[i][3]}", "#472f91", ("고도 M", 12))
            coa4 = Get_label.image_label_text(
                self.Gui, "coach4-1.png", 912, 173+(40*i), f"{self.coaches[i][4]}", "#472f91", ("고도 M", 12))
            coa5 = Get_label.image_label_text(
                self.Gui, "coach5-1.png", 992, 173+(40*i), f"{self.coaches[i][5]} 만원", "#472f91", ("고도 M", 12))

    def second_coach_scr(self):
        self.destroy()
        Team_Coach_Screen_background = Get_label.image_label(
            self.Gui, "Main_Screen_bg.png", 0, 0)
        game_button = self.game_buttons()
        right_button = Get_label.image_button(
            self.Gui, "right.png", 980, 43, self.no_action)
        left_button = Get_label.image_button(
            self.Gui, "left.png", 900, 43, self.first_coach_scr)
        second_len = self.len_coach-15
        right_button.config(state='disabled')
        self.Intro1 = Get_label.image_button_text(
            self.Gui, "coach1.png", 222, 133, self.sortcoa1, f"이름", "#472f91", ("고도 M", 12))
        self.Intro2 = Get_label.image_button_text(
            self.Gui, "coach2.png", 552, 133, self.sortcoa2, f"포지션", "#472f91", ("고도 M", 12))
        self.Intro3 = Get_label.image_button_text(
            self.Gui, "coach3.png", 832, 133, self.sortcoa3, f"나이", "#472f91", ("고도 M", 12))
        self.Intro4 = Get_label.image_button_text(
            self.Gui, "coach4.png", 912, 133, self.sortcoa4, f"능력치", "#472f91", ("고도 M", 12))
        self.Intro5 = Get_label.image_button_text(
            self.Gui, "coach5.png", 992, 133, self.sortcoa5, f"주급", "#472f91", ("고도 M", 12))
        if self.sort_color == 1:
            fir = self.change_coa_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_coa_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_coa_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_coa_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_coa_sortnum()
            self.Intro5.config(fg="#B30000")
        for i in range(second_len):
            coa1 = Get_label.image_label_text(
                self.Gui, "coach1-1.png", 222, 173+(40*i), f"{self.coaches[i+15][0]}", "#472f91", ("고도 M", 12))
            coa2 = Get_label.image_label_text(
                self.Gui, "coach2-1.png", 552, 173+(40*i), f"{self.coaches[i+15][2]}", "#472f91", ("고도 M", 12))
            coa3 = Get_label.image_label_text(
                self.Gui, "coach3-1.png", 832, 173+(40*i), f"{self.coaches[i+15][3]}", "#472f91", ("고도 M", 12))
            coa4 = Get_label.image_label_text(
                self.Gui, "coach4-1.png", 912, 173+(40*i), f"{self.coaches[i+15][4]}", "#472f91", ("고도 M", 12))
            coa5 = Get_label.image_label_text(
                self.Gui, "coach5-1.png", 992, 173+(40*i), f"{self.coaches[i+15][5]} 만원", "#472f91", ("고도 M", 12))

    def sortcoa1(self):
        self.coaches = team_coaches('Name', self.sort_num)
        self.sort_color = 1
        fir = self.first_coach_scr()

    def sortcoa2(self):
        self.coaches = team_coaches('Position', self.sort_num)
        self.sort_color = 2
        fir = self.first_coach_scr()

    def sortcoa3(self):
        self.coaches = team_coaches('Age', self.sort_num)
        self.sort_color = 3
        fir = self.first_coach_scr()

    def sortcoa4(self):
        self.coaches = team_coaches('Ability', self.sort_num)
        self.sort_color = 4
        fir = self.first_coach_scr()

    def sortcoa5(self):
        self.coaches = team_coaches('Money', self.sort_num)
        self.sort_color = 5
        fir = self.first_coach_scr()

    def change_coa_sortnum(self):
        if self.sort_num == 0:
            self.sort_num = 1
        else:
            self.sort_num = 0
        self.Intro1.config(fg="#472f91")
        self.Intro2.config(fg="#472f91")
        self.Intro3.config(fg="#472f91")
        self.Intro4.config(fg="#472f91")
        self.Intro5.config(fg="#472f91")

    ############################################################################################################################################################################################
    # 팀 직원 화면
    ############################################################################################################################################################################################

    def Team_Staff_Screen(self):
        team_count = check_myteam()
        if team_count == 0:
            Team_Staff_Screen_background = Get_label.image_label(
                self.Gui, "cantuse_bg.png", 0, 0)
            game_button = self.game_buttons()
        else:
            self.sort_num = 0
            self.sort_color = 0
            self.staffs = team_staffs('Position', self.sort_num)
            fir = self.first_staff_scr()

    def first_staff_scr(self):
        self.destroy()
        Team_Staff_Screen_background = Get_label.image_label(
            self.Gui, "Main_Screen_bg.png", 0, 0)
        game_button = self.game_buttons()
        right_button = Get_label.image_button(
            self.Gui, "right.png", 980, 43, self.second_staff_scr)
        left_button = Get_label.image_button(
            self.Gui, "left.png", 900, 43, self.no_action)
        left_button.config(state='disabled')
        self.len_staff = len(self.staffs)
        if self.len_staff < 16:
            right_button.config(state='disabled')
        self.Intro1 = Get_label.image_button_text(
            self.Gui, "coach1.png", 222, 133, self.sortsta1, f"이름", "#472f91", ("고도 M", 12))
        self.Intro2 = Get_label.image_button_text(
            self.Gui, "coach2.png", 552, 133, self.sortsta2, f"포지션", "#472f91", ("고도 M", 12))
        self.Intro3 = Get_label.image_button_text(
            self.Gui, "coach3.png", 832, 133, self.sortsta3, f"나이", "#472f91", ("고도 M", 12))
        self.Intro4 = Get_label.image_button_text(
            self.Gui, "coach4.png", 912, 133, self.sortsta4, f"능력치", "#472f91", ("고도 M", 12))
        self.Intro5 = Get_label.image_button_text(
            self.Gui, "coach5.png", 992, 133, self.sortsta5, f"주급", "#472f91", ("고도 M", 12))
        if self.sort_color == 1:
            fir = self.change_sta_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_sta_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_sta_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_sta_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_sta_sortnum()
            self.Intro5.config(fg="#B30000")
        first_len = 0
        if self.len_staff > 14:
            first_len = 15
        else:
            first_len = self.len_staff
        for i in range(first_len):
            sta1 = Get_label.image_label_text(
                self.Gui, "coach1-1.png", 222, 173+(40*i), f"{self.staffs[i][0]}", "#472f91", ("고도 M", 12))
            sta2 = Get_label.image_label_text(
                self.Gui, "coach2-1.png", 552, 173+(40*i), f"{self.staffs[i][2]}", "#472f91", ("고도 M", 12))
            sta3 = Get_label.image_label_text(
                self.Gui, "coach3-1.png", 832, 173+(40*i), f"{self.staffs[i][3]}", "#472f91", ("고도 M", 12))
            sta4 = Get_label.image_label_text(
                self.Gui, "coach4-1.png", 912, 173+(40*i), f"{self.staffs[i][4]}", "#472f91", ("고도 M", 12))
            sta5 = Get_label.image_label_text(
                self.Gui, "coach5-1.png", 992, 173+(40*i), f"{self.staffs[i][5]} 만원", "#472f91", ("고도 M", 12))

    def second_staff_scr(self):
        self.destroy()
        Team_Staff_Screen_background = Get_label.image_label(
            self.Gui, "Main_Screen_bg.png", 0, 0)
        game_button = self.game_buttons()
        right_button = Get_label.image_button(
            self.Gui, "right.png", 980, 43, self.no_action)
        left_button = Get_label.image_button(
            self.Gui, "left.png", 900, 43, self.first_staff_scr)
        second_len = self.len_staff-15
        right_button.config(state='disabled')
        self.Intro1 = Get_label.image_button_text(
            self.Gui, "coach1.png", 222, 133, self.sortsta1, f"이름", "#472f91", ("고도 M", 12))
        self.Intro2 = Get_label.image_button_text(
            self.Gui, "coach2.png", 552, 133, self.sortsta2, f"포지션", "#472f91", ("고도 M", 12))
        self.Intro3 = Get_label.image_button_text(
            self.Gui, "coach3.png", 832, 133, self.sortsta3, f"나이", "#472f91", ("고도 M", 12))
        self.Intro4 = Get_label.image_button_text(
            self.Gui, "coach4.png", 912, 133, self.sortsta4, f"능력치", "#472f91", ("고도 M", 12))
        self.Intro5 = Get_label.image_button_text(
            self.Gui, "coach5.png", 992, 133, self.sortsta5, f"주급", "#472f91", ("고도 M", 12))
        if self.sort_color == 1:
            fir = self.change_sta_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_sta_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_sta_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_sta_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_sta_sortnum()
            self.Intro5.config(fg="#B30000")
        for i in range(second_len):
            sta1 = Get_label.image_label_text(
                self.Gui, "coach1-1.png", 222, 173+(40*i), f"{self.staffs[i+15][0]}", "#472f91", ("고도 M", 12))
            sta2 = Get_label.image_label_text(
                self.Gui, "coach2-1.png", 552, 173+(40*i), f"{self.staffs[i+15][2]}", "#472f91", ("고도 M", 12))
            sta3 = Get_label.image_label_text(
                self.Gui, "coach3-1.png", 832, 173+(40*i), f"{self.staffs[i+15][3]}", "#472f91", ("고도 M", 12))
            sta4 = Get_label.image_label_text(
                self.Gui, "coach4-1.png", 912, 173+(40*i), f"{self.staffs[i+15][4]}", "#472f91", ("고도 M", 12))
            sta5 = Get_label.image_label_text(
                self.Gui, "coach5-1.png", 992, 173+(40*i), f"{self.staffs[i+15][5]} 만원", "#472f91", ("고도 M", 12))

    def sortsta1(self):
        self.staffs = team_staffs('Name', self.sort_num)
        self.sort_color = 1
        fir = self.first_staff_scr()

    def sortsta2(self):
        self.staffs = team_staffs('Position', self.sort_num)
        self.sort_color = 2
        fir = self.first_staff_scr()

    def sortsta3(self):
        self.staffs = team_staffs('Age', self.sort_num)
        self.sort_color = 3
        fir = self.first_staff_scr()

    def sortsta4(self):
        self.staffs = team_staffs('Ability', self.sort_num)
        self.sort_color = 4
        fir = self.first_staff_scr()

    def sortsta5(self):
        self.staffs = team_staffs('Money', self.sort_num)
        self.sort_color = 5
        fir = self.first_staff_scr()

    def change_coa_sortnum(self):
        if self.sort_num == 0:
            self.sort_num = 1
        else:
            self.sort_num = 0
        self.Intro1.config(fg="#472f91")
        self.Intro2.config(fg="#472f91")
        self.Intro3.config(fg="#472f91")
        self.Intro4.config(fg="#472f91")
        self.Intro5.config(fg="#472f91")
