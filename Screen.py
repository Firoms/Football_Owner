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
            self.Gui, "HowToPlay_btn.png", 20, 450, self.Incomplete_Screen)
        Settings_button = Get_image.image_button(
            self.Gui, "Settings_btn.png", 20, 550, self.Incomplete_Screen)
        Exit_button = Get_image.image_button(
            self.Gui, "Exit_btn.png", 20, 650, self._quit)
        Version_label = Label(self.Gui.Gui, text="Version 0.05",
                              fg="green", font=("맑은 고딕", 12), height=1)
        Version_label.place(x=1100, y=5)

    def Main_Screen(self):
        Menu_Screen_background = Get_image.image_label(
            self.Gui, "Main_Screen_bg.png", 0, 0)
        Return_button = Get_image.image_button(
            self.Gui, "Return_btn.png", 920, 10, self.Menu_Screen)

    def Incomplete_Screen(self):
        Incomplete_Screen_background = Get_image.image_label(
            self.Gui, "Incomplete_bg.png", 0, 0)
        Return_button = Get_image.image_button(
            self.Gui, "Return_btn.png", 920, 10, self.Menu_Screen)
        reset_datas_btn = Button(self.Gui.Gui, text="reset datas",
                                 bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21, command=reset_datas)
        reset_datas_btn.place(x=75, y=198)

    def Savefiles_Screen(self):
        Savefiles_Screen_background = Get_image.image_label(
            self.Gui, "Savefiles_bg.png", 0, 0)
        Return_button = Get_image.image_button(
            self.Gui, "Return_btn.png", 885, 30, self.Menu_Screen)
        Save_check1 = Check_Savefiles(1)
        Save_check2 = Check_Savefiles(2)
        Save_check3 = Check_Savefiles(3)
        if Save_check1 == None:
            first_save_btn = Button(self.Gui.Gui, text="+",
                                    bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21)
            first_save_btn.place(x=75, y=198)
        else:
            first_save_btn = Button(self.Gui.Gui, text=Save_check1,
                                    bg="yellowgreen", fg="blue", font=("맑은 고딕", 20), width=48, height=3, command=self.Main_Screen)
            first_save_btn.place(x=75, y=198)
        if Save_check2 == None:
            second_save_btn = Button(self.Gui.Gui, text="+",
                                     bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21, command=self.Second_Savefiles_Screen)
            second_save_btn.place(x=75, y=402)
        else:
            second_save_btn = Button(self.Gui.Gui, text=Save_check2,
                                     bg="yellowgreen", fg="blue", font=("맑은 고딕", 20), width=48, height=3, command=self.Main_Screen)
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
            First_Save = input_Names1()
            Main_Screen = self.Main_Screen()
            if First_Save == 'No':
                time.sleep(0.3)
                Return_MainScreen = self.Menu_Screen()
        else:
            Savefile_Screen = self.Savefiles_Screen()

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

    def _quit(self):
        answer = messagebox.askyesno("확인", "정말 종료하시겠습니까?")
        if answer == True:
            self.Gui.Gui.quit()
            self.Gui.Gui.destroy()
            exit()
