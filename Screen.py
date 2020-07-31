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
        HowToPlay_Screen_background = Get_label.image_label(
            self.Gui, "HowToPlay_bg.png", 0, 0)
        Return_button = Get_label.image_button(
            self.Gui, "Return_btn.png", 920, 10, self.Menu_Screen)

    ############################################################################################################################################################################################
    # 세이브 화면
    ############################################################################################################################################################################################

    def Savefiles_Screen(self):
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
            self.Gui, "menu6.png", 34, 490, self.no_action)
        self.menu7_button = Get_label.image_button(
            self.Gui, "menu7.png", 34, 560, self.no_action)
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
        Message_Screen_background = Get_label.image_label(
            self.Gui, "Main_Screen_bg.png", 0, 0)
        self.game_buttons()
        money = int(check_money())
        myteam = check_myteam()
        self.myteam_info = my_team_ac()
        self.acquisition_list = ran_team_ac(money)
        intro_label1 = f'☆ 인수\n/           팀            /     가격     /         나라        -         리그         /                                  '
        intro_label2 = '%-23s %s만원    %s - %s' % (
            self.acquisition_list[0][3], self.acquisition_list[0][4], self.acquisition_list[0][2], self.acquisition_list[0][1])
        intro_label3 = '%-23s %s만원    %s - %s' % (
            self.acquisition_list[1][3], self.acquisition_list[1][4], self.acquisition_list[1][2], self.acquisition_list[1][1])
        intro_label4 = '%-23s %s만원     %s - %s' % (
            self.acquisition_list[2][3], self.acquisition_list[2][4], self.acquisition_list[2][2], self.acquisition_list[2][1])
        intro_label5 = '%-23s %s만원     %s - %s' % (
            self.acquisition_list[3][3], self.acquisition_list[3][4], self.acquisition_list[3][2], self.acquisition_list[3][1])
        intro_label6 = '%-23s %s만원     %s - %s' % (
            self.acquisition_list[4][3], self.acquisition_list[4][4], self.acquisition_list[4][2], self.acquisition_list[4][1])
        intro_label7 = '%-23s %s만원     %s - %s' % (
            self.acquisition_list[5][3], self.acquisition_list[5][4], self.acquisition_list[5][2], self.acquisition_list[5][1])
        intro_label8 = '%-23s %s만원     %s - %s' % (
            self.acquisition_list[6][3], self.acquisition_list[6][4], self.acquisition_list[6][2], self.acquisition_list[6][1])
        Intro1 = Get_label.image_label_text(
            self.Gui, "acquisition_bg1.jpg", 212, 123, f"{intro_label1}\n\n1. {intro_label2}\n\n2. {intro_label3}\n\n3. {intro_label4}\n\n4. {intro_label5}\n\n5. {intro_label6}\n\n6. {intro_label7}\n\n7. {intro_label8}\n", "#472f91", ("고도 M", 17))
        Team_label1 = Get_label.image_button(
            self.Gui, "acquisition_btn1.png", 1060, 200+(52*0), self.buy1)
        Team_label2 = Get_label.image_button(
            self.Gui, "acquisition_btn1.png", 1060, 200+(52*1), self.buy2)
        Team_label3 = Get_label.image_button(
            self.Gui, "acquisition_btn1.png", 1060, 200+(52*2), self.buy3)
        Team_label4 = Get_label.image_button(
            self.Gui, "acquisition_btn1.png", 1060, 200+(52*3), self.buy4)
        Team_label5 = Get_label.image_button(
            self.Gui, "acquisition_btn1.png", 1060, 200+(52*4), self.buy5)
        Team_label6 = Get_label.image_button(
            self.Gui, "acquisition_btn1.png", 1060, 200+(52*5), self.buy6)
        Team_label7 = Get_label.image_button(
            self.Gui, "acquisition_btn1.png", 1060, 200+(52*6), self.buy7)

        if myteam == 0:
            Intro2 = Get_label.image_label(
                self.Gui, "acquisition_bg2.jpg", 212, 576)
        elif myteam == 1:
            intro_label9 = f'☆ 매각                                                                                                                        '
            intro_label10 = '%-23s %s만원     %s - %s' % (
                self.myteam_info[0][3], self.myteam_info[0][4], self.myteam_info[0][2], self.myteam_info[0][1])
            Intro2 = Get_label.image_label_text(
                self.Gui, "acquisition_bg2.jpg", 212, 576, f"{intro_label9}\n\n1. {intro_label10}\n\n\n\n", "#472f91", ("고도 M", 17))
            Team_label8 = Get_label.image_button(
                self.Gui, "acquisition_btn2.png", 1060, 625+(50*0), self.sell1)
        elif myteam == 2:
            intro_label9 = f'☆ 매각                                                                                                                        '
            intro_label10 = '%-23s %s만원     %s - %s' % (
                self.myteam_info[0][3], self.myteam_info[0][4], self.myteam_info[0][2], self.myteam_info[0][1])
            intro_label11 = '%-23s %s만원     %s - %s' % (
                self.myteam_info[1][3], self.myteam_info[1][4], self.myteam_info[1][2], self.myteam_info[1][1])
            Intro2 = Get_label.image_label_text(
                self.Gui, "acquisition_bg2.jpg", 212, 576, f"{intro_label9}\n\n1. {intro_label10}\n\n2. {intro_label11}\n\n", "#472f91", ("고도 M", 17))
            Team_label8 = Get_label.image_button(
                self.Gui, "acquisition_btn2.png", 1060, 625+(50*0), self.sell1)
            Team_label8 = Get_label.image_button(
                self.Gui, "acquisition_btn2.png", 1060, 625+(50*1), self.sell2)
        else:
            intro_label9 = f'☆ 매각                                                                                                                        '
            intro_label10 = '%-23s %s만원     %s - %s' % (
                self.myteam_info[0][3], self.myteam_info[0][4], self.myteam_info[0][2], self.myteam_info[0][1])
            intro_label11 = '%-23s %s만원     %s - %s' % (
                self.myteam_info[1][3], self.myteam_info[1][4], self.myteam_info[1][2], self.myteam_info[1][1])
            intro_label12 = '%-23s %s만원     %s - %s' % (
                self.myteam_info[2][3], self.myteam_info[2][4], self.myteam_info[2][2], self.myteam_info[2][1])
            Intro2 = Get_label.image_label_text(
                self.Gui, "acquisition_bg2.jpg", 212, 576, f"{intro_label9}\n\n1. {intro_label10}\n\n2. {intro_label11}\n\n3. {intro_label12}", "#472f91", ("고도 M", 17))
            Team_label8 = Get_label.image_button(
                self.Gui, "acquisition_btn2.png", 1060, 625+(50*0), self.sell1)
            Team_label9 = Get_label.image_button(
                self.Gui, "acquisition_btn2.png", 1060, 625+(50*1), self.sell2)
            Team_label10 = Get_label.image_button(
                self.Gui, "acquisition_btn2.png", 1060, 625+(50*2), self.sell3)

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
        Team_Player_Screen_background = Get_label.image_label(
            self.Gui, "Main_Screen_bg.png", 0, 0)
        game_button = self.game_buttons()
        right_button = Get_label.image_button(
            self.Gui, "right.png", 980, 43, self.second_player_scr)
        left_button = Get_label.image_button(
            self.Gui, "left.png", 900, 43, self.no_action)
        left_button.config(state='disabled')
        self.len_player = len(self.players)
        self.Intro1 = Get_label.image_button_text(
            self.Gui, "player1.png", 222, 133, self.sort1, f"번호", "#472f91", ("고도 M", 12))
        self.Intro2 = Get_label.image_button_text(
            self.Gui, "player2.png", 282, 133, self.sort2, f"이름", "#472f91", ("고도 M", 12))
        self.Intro3 = Get_label.image_button_text(
            self.Gui, "player3.png", 542, 133, self.sort3, f"포지션", "#472f91", ("고도 M", 12))
        self.Intro4 = Get_label.image_button_text(
            self.Gui, "player4.png", 742, 133, self.sort4, f"나이", "#472f91", ("고도 M", 12))
        self.Intro5 = Get_label.image_button_text(
            self.Gui, "player5.png", 802, 133, self.sort5, f"선수 가치", "#472f91", ("고도 M", 12))
        self.Intro6 = Get_label.image_button_text(
            self.Gui, "player6.png", 932, 133, self.sort6, f"능력치", "#472f91", ("고도 M", 12))
        self.Intro7 = Get_label.image_button_text(
            self.Gui, "player7.png", 992, 133, self.sort7, f"잠재력", "#472f91", ("고도 M", 12))
        self.Intro8 = Get_label.image_button_text(
            self.Gui, "player8.png", 1052, 133, self.sort8, f"선수 주급", "#472f91", ("고도 M", 12))
        if self.sort_color == 1:
            fir = self.change_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_sortnum()
            self.Intro5.config(fg="#B30000")
        elif self.sort_color == 6:
            fir = self.change_sortnum()
            self.Intro6.config(fg="#B30000")
        elif self.sort_color == 7:
            fir = self.change_sortnum()
            self.Intro7.config(fg="#B30000")
        elif self.sort_color == 8:
            fir = self.change_sortnum()
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
                self.Gui, "player5-1.png", 802, 173+(40*i), f"{self.players[i][5]}", "#472f91", ("고도 M", 12))
            pla6 = Get_label.image_label_text(
                self.Gui, "player6-1.png", 932, 173+(40*i), f"{self.players[i][6]}", "#472f91", ("고도 M", 12))
            pla7 = Get_label.image_label_text(
                self.Gui, "player7-1.png", 992, 173+(40*i), f"{self.players[i][7]}", "#472f91", ("고도 M", 12))
            pla8 = Get_label.image_label_text(
                self.Gui, "player8-1.png", 1052, 173+(40*i), f"{self.players[i][8]}", "#472f91", ("고도 M", 12))

    def second_player_scr(self):
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
            self.Gui, "player1.png", 222, 133, self.sort1, f"번호", "#472f91", ("고도 M", 12))
        self.Intro2 = Get_label.image_button_text(
            self.Gui, "player2.png", 282, 133, self.sort2, f"이름", "#472f91", ("고도 M", 12))
        self.Intro3 = Get_label.image_button_text(
            self.Gui, "player3.png", 542, 133, self.sort3, f"포지션", "#472f91", ("고도 M", 12))
        self.Intro4 = Get_label.image_button_text(
            self.Gui, "player4.png", 742, 133, self.sort4, f"나이", "#472f91", ("고도 M", 12))
        self.Intro5 = Get_label.image_button_text(
            self.Gui, "player5.png", 802, 133, self.sort5, f"선수 가치", "#472f91", ("고도 M", 12))
        self.Intro6 = Get_label.image_button_text(
            self.Gui, "player6.png", 932, 133, self.sort6, f"능력치", "#472f91", ("고도 M", 12))
        self.Intro7 = Get_label.image_button_text(
            self.Gui, "player7.png", 992, 133, self.sort7, f"잠재력", "#472f91", ("고도 M", 12))
        self.Intro8 = Get_label.image_button_text(
            self.Gui, "player8.png", 1052, 133, self.sort8, f"선수 주급", "#472f91", ("고도 M", 12))
        if self.sort_color == 1:
            fir = self.change_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_sortnum()
            self.Intro5.config(fg="#B30000")
        elif self.sort_color == 6:
            fir = self.change_sortnum()
            self.Intro6.config(fg="#B30000")
        elif self.sort_color == 7:
            fir = self.change_sortnum()
            self.Intro7.config(fg="#B30000")
        elif self.sort_color == 8:
            fir = self.change_sortnum()
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
                self.Gui, "player5-1.png", 802, 173+(40*i), f"{self.players[i+15][5]}", "#472f91", ("고도 M", 12))
            pla6 = Get_label.image_label_text(
                self.Gui, "player6-1.png", 932, 173+(40*i), f"{self.players[i+15][6]}", "#472f91", ("고도 M", 12))
            pla7 = Get_label.image_label_text(
                self.Gui, "player7-1.png", 992, 173+(40*i), f"{self.players[i+15][7]}", "#472f91", ("고도 M", 12))
            pla8 = Get_label.image_label_text(
                self.Gui, "player8-1.png", 1052, 173+(40*i), f"{self.players[i+15][8]}", "#472f91", ("고도 M", 12))

    def third_player_scr(self):
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
            self.Gui, "player1.png", 222, 133, self.sort1, f"번호", "#472f91", ("고도 M", 12))
        self.Intro2 = Get_label.image_button_text(
            self.Gui, "player2.png", 282, 133, self.sort2, f"이름", "#472f91", ("고도 M", 12))
        self.Intro3 = Get_label.image_button_text(
            self.Gui, "player3.png", 542, 133, self.sort3, f"포지션", "#472f91", ("고도 M", 12))
        self.Intro4 = Get_label.image_button_text(
            self.Gui, "player4.png", 742, 133, self.sort4, f"나이", "#472f91", ("고도 M", 12))
        self.Intro5 = Get_label.image_button_text(
            self.Gui, "player5.png", 802, 133, self.sort5, f"선수 가치", "#472f91", ("고도 M", 12))
        self.Intro6 = Get_label.image_button_text(
            self.Gui, "player6.png", 932, 133, self.sort6, f"능력치", "#472f91", ("고도 M", 12))
        self.Intro7 = Get_label.image_button_text(
            self.Gui, "player7.png", 992, 133, self.sort7, f"잠재력", "#472f91", ("고도 M", 12))
        self.Intro8 = Get_label.image_button_text(
            self.Gui, "player8.png", 1052, 133, self.sort8, f"선수 주급", "#472f91", ("고도 M", 12))
        if self.sort_color == 1:
            fir = self.change_sortnum()
            self.Intro1.config(fg="#B30000")
        elif self.sort_color == 2:
            fir = self.change_sortnum()
            self.Intro2.config(fg="#B30000")
        elif self.sort_color == 3:
            fir = self.change_sortnum()
            self.Intro3.config(fg="#B30000")
        elif self.sort_color == 4:
            fir = self.change_sortnum()
            self.Intro4.config(fg="#B30000")
        elif self.sort_color == 5:
            fir = self.change_sortnum()
            self.Intro5.config(fg="#B30000")
        elif self.sort_color == 6:
            fir = self.change_sortnum()
            self.Intro6.config(fg="#B30000")
        elif self.sort_color == 7:
            fir = self.change_sortnum()
            self.Intro7.config(fg="#B30000")
        elif self.sort_color == 8:
            fir = self.change_sortnum()
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
                self.Gui, "player5-1.png", 802, 173+(40*i), f"{self.players[i+30][5]}", "#472f91", ("고도 M", 12))
            pla6 = Get_label.image_label_text(
                self.Gui, "player6-1.png", 932, 173+(40*i), f"{self.players[i+30][6]}", "#472f91", ("고도 M", 12))
            pla7 = Get_label.image_label_text(
                self.Gui, "player7-1.png", 992, 173+(40*i), f"{self.players[i+30][7]}", "#472f91", ("고도 M", 12))
            pla8 = Get_label.image_label_text(
                self.Gui, "player8-1.png", 1052, 173+(40*i), f"{self.players[i+30][8]}", "#472f91", ("고도 M", 12))

    def sort1(self):
        self.players = team_players('Number', self.sort_num)
        self.sort_color = 1
        fir = self.first_player_scr()

    def sort2(self):
        self.players = team_players('Name', self.sort_num)
        self.sort_color = 2
        fir = self.first_player_scr()

    def sort3(self):
        self.players = team_players('Position', self.sort_num)
        self.sort_color = 3
        fir = self.first_player_scr()

    def sort4(self):
        self.players = team_players('Age', self.sort_num)
        self.sort_color = 4
        fir = self.first_player_scr()

    def sort5(self):
        self.players = team_players('Market_Value', self.sort_num)
        self.sort_color = 5
        fir = self.first_player_scr()

    def sort6(self):
        self.players = team_players('Ability', self.sort_num)
        self.sort_color = 6
        fir = self.first_player_scr()

    def sort7(self):
        self.players = team_players('Potential', self.sort_num)
        self.sort_color = 7
        fir = self.first_player_scr()

    def sort8(self):
        self.players = team_players('Money', self.sort_num)
        self.sort_color = 8
        fir = self.first_player_scr()

    def change_sortnum(self):
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
