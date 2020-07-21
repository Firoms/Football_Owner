from Get_Image import Get_image
from Get_Savefiles import *
from tkinter import *
import time


class Screen:
    def __init__(self, Gui):
        self.Gui = Gui
        self.Menu_Screen()

    def Menu_Screen(self):
        Menu_Screen_background = Get_image.image_label(
            self.Gui, "Title_Screen_bg.png", 0, 0)
        Game_Start_button = Get_image.image_button(
            self.Gui, "Game_Start_btn.png", 20, 350, self.First_Savefiles_Screen)
        HowToPlay_button = Get_image.image_button(
            self.Gui, "HowToPlay_btn.png", 20, 450, self.HowToPlay_Screen)
        Settings_button = Get_image.image_button(
            self.Gui, "Settings_btn.png", 20, 550, self.Incomplete_Screen)
        Exit_button = Get_image.image_button(
            self.Gui, "Exit_btn.png", 20, 650, self._quit)
        Version_label = Label(self.Gui.Gui, text="Version 0.21",
                              fg="green", bg="purple", font=("맑은 고딕", 12), height=1)
        Version_label.place(x=1100, y=5)

    def Main_Screen(self):
        Menu_Screen_background = Get_image.image_label(
            self.Gui, "Main_Screen_bg.png", 0, 0)
        Logo_button = Get_image.image_button(
            self.Gui, "logo_btn.png", 31, 33, self.Menu_Screen)
        Save_button = Get_image.image_button(
            self.Gui, "save_btn.png", 121, 33, self.Savefiles_Screen)
        Go_button = Get_image.image_button(
            self.Gui, "go_btn.png", 1090, 33, self.Main_Screen)
        menu1_button = Get_image.image_button(
            self.Gui, "menu1.png", 34, 140, self.Main_Screen)
        menu2_button = Get_image.image_button(
            self.Gui, "menu2.png", 34, 210, self.Main_Screen)
        menu3_button = Get_image.image_button(
            self.Gui, "menu3.png", 34, 280, self.Main_Screen)
        menu4_button = Get_image.image_button(
            self.Gui, "menu4.png", 34, 350, self.Main_Screen)
        menu5_button = Get_image.image_button(
            self.Gui, "menu5.png", 34, 420, self.Main_Screen)
        menu6_button = Get_image.image_button(
            self.Gui, "menu6.png", 34, 490, self.Main_Screen)
        menu7_button = Get_image.image_button(
            self.Gui, "menu7.png", 34, 560, self.Main_Screen)
        menu8_button = Get_image.image_button(
            self.Gui, "menu8.png", 34, 630, self.Main_Screen)
        menu9_button = Get_image.image_button(
            self.Gui, "menu9.png", 34, 700, self.Main_Screen)
        self.message()

    def message(self):
        check_mon = check_money()
        if check_mon == '-':
            self.get_first_money()

    def get_first_money(self):
        money = 10000
        win = 0
        Name = Get_image.image_label(
            self.Gui, "Name_Tag.png", 250, 40)
        Intro1 = Get_image.image_label(
            self.Gui, "intro1.png", 245, 170)
        Intro2 = Get_image.image_label_text(
            self.Gui, "intro2.png", 250, 345, f"                {win}번", "DarkGreen", ("견고딕", 26))
        Intro3 = Get_image.image_label_text(
            self.Gui, "intro3.png", 600, 345, f"             {money}원", "DarkGreen", ("견고딕", 26))

        def Game():
            def select1():
                bg1.configure(
                    text=f"\n선수이름 : {first_player[1]}\n\n 선수가치 : {first_value}\n")
                bg2.configure(
                    text=f"\n선수이름 : {second_player[1]}\n\n 선수가치 : {second_value}\n")
                bg1.configure(state="disabled")
                bg2.configure(state="disabled")
                if first_value >= second_value:
                    money *= 2
                    win += 1
                    Intro2 = Get_image.image_label_text(
                        self.Gui, "intro2.png", 250, 345, f"                {win}번", "DarkGreen", ("견고딕", 26))
                    Intro3 = Get_image.image_label_text(
                        self.Gui, "intro3.png", 600, 345, f"             {money}원", "DarkGreen", ("견고딕", 26))
                    time.sleep(3000)
                    bg1.configure(state="disabled")
                    bg2.configure(state="disabled")
                    restart = Game()
                else:
                    time.sleep(3000)

            def select2():
                bg1.configure(
                    text=f"\n선수이름 : {first_player[1]}\n\n 선수가치 : {first_value}\n")
                bg2.configure(
                    text=f"\n선수이름 : {second_player[1]}\n\n 선수가치 : {second_value}\n")
                bg1.configure(state="disabled")
                bg2.configure(state="disabled")
                if first_value <= second_value:
                    money *= 2
                    win += 1
                    Intro2 = Get_image.image_label_text(
                        self.Gui, "intro2.png", 250, 345, f"                {win}번", "DarkGreen", ("견고딕", 26))
                    Intro3 = Get_image.image_label_text(
                        self.Gui, "intro3.png", 600, 345, f"             {money}원", "DarkGreen", ("견고딕", 26))
                    time.sleep(3000)
                    bg1.configure(state="disabled")
                    bg2.configure(state="disabled")
                    restart = Game()
                else:
                    time.sleep(3000)

            first_player = mini_game()
            first_value = int(first_player[6])
            second_player = mini_game()
            second_value = int(second_player[6])
            bg1 = Get_image.image_button_text(
                self.Gui, "bg1.png", 250, 445, select1, f"\n선수이름 : {first_player[1]}\n\n 팀 : {first_player[2]}\n\n 등번호 : {first_player[3]}\n\n 포지션 {first_player[4]}\n\n 나이 : {first_player[5]}\n", "DarkGreen", ("견고딕", 18))
            bg2 = Get_image.image_button_text(
                self.Gui, "bg1.png", 720, 445, select2, f"\n선수이름 : {second_player[1]}\n\n 팀 : {second_player[2]}\n\n 등번호 : {second_player[3]}\n\n 포지션 {second_player[4]}\n\n 나이 : {second_player[5]}\n", "DarkGreen", ("견고딕", 18))
        start = Game()

    def Incomplete_Screen(self):
        Incomplete_Screen_background = Get_image.image_label(
            self.Gui, "Incomplete_bg.png", 0, 0)
        Return_button = Get_image.image_button(
            self.Gui, "Return_btn.png", 920, 10, self.Menu_Screen)
        reset_datas_btn = Button(self.Gui.Gui, text="reset datas",
                                 bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21, command=reset_datas)
        reset_datas_btn.place(x=75, y=198)

    def Savefiles_Screen(self):
        time_load = time_auto_load()

        def save1():
            save = Save1_data()
            MainScreen = self.Main_Screen()

        def save2():
            save = Save2_data()
            MainScreen = self.Main_Screen()

        Savefiles_Screen_background = Get_image.image_label(
            self.Gui, "Savefiles_bg.png", 0, 0)
        Return_button = Get_image.image_button(
            self.Gui, "Return_btn.png", 885, 30, self.Main_Screen)
        Save_check1 = Check_Savefiles(1)
        Save_check2 = Check_Savefiles(2)
        Save_check3 = Check_Savefiles(3)
        if Save_check1 == None:
            first_save_btn = Button(self.Gui.Gui, text="+",
                                    bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21, command=save1)
            first_save_btn.place(x=75, y=198)
        else:
            first_save_btn = Button(self.Gui.Gui, text=Save_check1,
                                    bg="yellowgreen", fg="blue", font=("맑은 고딕", 20), width=48, height=3, command=save1)
            first_save_btn.place(x=75, y=198)
        if Save_check2 == None:
            second_save_btn = Button(self.Gui.Gui, text="+",
                                     bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21, command=save2)
            second_save_btn.place(x=75, y=402)
        else:
            second_save_btn = Button(self.Gui.Gui, text=Save_check2,
                                     bg="yellowgreen", fg="blue", font=("맑은 고딕", 20), width=48, height=3, command=save2)
            second_save_btn.place(x=75, y=402)
        if Save_check3 == None:
            third_save_btn = Button(self.Gui.Gui, text="자동 저장 된 정보가 없습니다.",
                                    bg="yellowgreen", fg="blue", font=("맑은 고딕", 20), width=48, height=3)
            third_save_btn.place(x=75, y=606)
        else:
            third_save_btn = Button(self.Gui.Gui, text=f"{Save_check3}\n자동 저장 공간입니다.",
                                    bg="yellowgreen", fg="blue", font=("맑은 고딕", 20), width=48, height=3)
            third_save_btn.place(x=75, y=606)

    def loadfiles_Screen(self):
        time_load = time_auto_load()

        def load1():
            load = load1_data()
            MainScreen = self.Main_Screen()

        def load2():
            load = load2_data()
            MainScreen = self.Main_Screen()

        Savefiles_Screen_background = Get_image.image_label(
            self.Gui, "Loadfiles_bg.png", 0, 0)
        Return_button = Get_image.image_button(
            self.Gui, "Return_btn.png", 885, 30, self.Menu_Screen)
        Save_check1 = Check_Savefiles(1)
        Save_check2 = Check_Savefiles(2)
        Save_check3 = Check_Savefiles(3)
        if Save_check1 == None:
            first_save_btn = Button(self.Gui.Gui, text="+",
                                    bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21, command=load1)
            first_save_btn.place(x=75, y=198)
        else:
            first_save_btn = Button(self.Gui.Gui, text=Save_check1,
                                    bg="yellowgreen", fg="blue", font=("맑은 고딕", 20), width=48, height=3, command=load1)
            first_save_btn.place(x=75, y=198)
        if Save_check2 == None:
            second_save_btn = Button(self.Gui.Gui, text="+",
                                     bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21, command=load2)
            second_save_btn.place(x=75, y=402)
        else:
            second_save_btn = Button(self.Gui.Gui, text=Save_check2,
                                     bg="yellowgreen", fg="blue", font=("맑은 고딕", 20), width=48, height=3, command=load2)
            second_save_btn.place(x=75, y=402)
        if Save_check3 == None:
            third_save_btn = Button(self.Gui.Gui, text="자동 저장 된 정보가 없습니다.",
                                    bg="yellowgreen", fg="blue", font=("맑은 고딕", 20), width=48, height=3)
            third_save_btn.place(x=75, y=606)
        else:
            third_save_btn = Button(self.Gui.Gui, text=Save_check3,
                                    bg="yellowgreen", fg="blue", font=("맑은 고딕", 20), width=48, height=3, command=self.Main_Screen)
            third_save_btn.place(x=75, y=606)

    def First_Savefiles_Screen(self):
        Save_check1 = Check_Savefiles(1)
        if Save_check1 == None:
            Savefiles_Screen_background = Get_image.image_label(
                self.Gui, "Savefiles_bg.png", 0, 0)
            Return_button = Get_image.image_button(
                self.Gui, "Return_btn.png", 885, 30, self.Menu_Screen)

            first_save_btn = Button(self.Gui.Gui, text="+",
                                    bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21)
            first_save_btn.place(x=75, y=198)
            second_save_btn = Button(self.Gui.Gui, text="+",
                                     bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21)
            second_save_btn.place(x=75, y=402)
            third_save_btn = Button(self.Gui.Gui, text="자동 저장 된 정보가 없습니다.",
                                    bg="yellowgreen", fg="blue", font=("맑은 고딕", 20), width=48, height=3)
            third_save_btn.place(x=75, y=606)
            Get_data = Auto_save_get_data(1)
            First_Save = input_Names1()
            load_data = load1_data()
            Main_Screen = self.Main_Screen()
            if First_Save == 'No':
                time.sleep(0.3)
                Return_MainScreen = self.Menu_Screen()
        else:
            Savefile_Screen = self.loadfiles_Screen()

    def Second_Savefiles_Screen(self):
        Save_check2 = Check_Savefiles(2)
        if Save_check2 == None:
            Second_Save = input_Names2()
            Main_Screen = self.Main_Screen()
            if Second_Save == 'No':
                time.sleep(0.3)
                Return_MainScreen = self.Menu_Screen()
        else:
            Savefile_Screen = self.Savefiles_Screen()

    def HowToPlay_Screen(self):
        HowToPlay_Screen_background = Get_image.image_label(
            self.Gui, "HowToPlay_bg.png", 0, 0)
        Return_button = Get_image.image_button(
            self.Gui, "Return_btn.png", 920, 10, self.Menu_Screen)

    def _quit(self):
        answer = messagebox.askyesno("확인", "정말 종료하시겠습니까?")
        if answer == True:
            self.Gui.Gui.quit()
            self.Gui.Gui.destroy()
            exit()
