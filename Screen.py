from Get_Image import Get_image
from Get_Savefiles import *
from tkinter import *


class Screen:
    def __init__(self, Gui):
        self.Gui = Gui
        self.Menu_Screen()

    def Menu_Screen(self):
        Menu_Screen_background = Get_image.image_label(
            self.Gui, "Main_Screen_bg.png", 0, 0)
        Game_Start_button = Get_image.image_button(
            self.Gui, "Game_Start_btn.png", 20, 350, self.Savefiles_Screen)
        HowToPlay_button = Get_image.image_button(
            self.Gui, "HowToPlay_btn.png", 20, 450, self.Incomplete_Screen)
        Settings_button = Get_image.image_button(
            self.Gui, "Settings_btn.png", 20, 550, self.Incomplete_Screen)
        Exit_button = Get_image.image_button(
            self.Gui, "Exit_btn.png", 20, 650, self._quit)
        Version_label = Label(self.Gui.Gui, text="Version 0.04",
                              fg="green", font=("맑은 고딕", 12), height=1)
        Version_label.place(x=1100, y=5)

    def Incomplete_Screen(self):
        Incomplete_Screen_background = Get_image.image_label(
            self.Gui, "Incomplete_bg.png", 0, 0)
        Return_button = Get_image.image_button(
            self.Gui, "Return_btn.png", 920, 10, self.Menu_Screen)

    def Savefiles_Screen(self):
        Incomplete_Screen_background = Get_image.image_label(
            self.Gui, "Savefiles_bg.png", 0, 0)
        Return_button = Get_image.image_button(
            self.Gui, "Return_btn.png", 885, 30, self.Menu_Screen)
        Save_check1, Save_check2, Save_check3 = Get_Savefiles()
        if Save_check1 == None:
            first_save_btn = Button(self.Gui.Gui, text="+",
                                    bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21, command=input_Names)
            first_save_btn.place(x=75, y=198)
        else:
            first_save_btn = Button(self.Gui.Gui, text=Save_check1,
                                    bg="yellowgreen", fg="blue", font=("맑은 고딕", 20), width=48, height=3)
            first_save_btn.place(x=75, y=198)
        if Save_check2 == None:
            second_save_btn = Button(self.Gui.Gui, text="+",
                                     bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21, command=input_Names)
            second_save_btn.place(x=75, y=402)
        else:
            second_save_btn = Button(self.Gui.Gui, text=Save_check2,
                                     bg="yellowgreen", fg="blue", font=("맑은 고딕", 20), width=48, height=3)
            second_save_btn.place(x=75, y=402)
        if Save_check3 == None:
            third_save_btn = Button(self.Gui.Gui, text="+",
                                    bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21, command=input_Names)
            third_save_btn.place(x=75, y=606)
        else:
            third_save_btn = Button(self.Gui.Gui, text=Save_check3,
                                    bg="yellowgreen", fg="blue", font=("맑은 고딕", 20), width=48, height=3)
            third_save_btn.place(x=75, y=606)

    def _quit(self):
        answer = messagebox.askyesno("확인", "정말 종료하시겠습니까?")
        if answer == True:
            self.Gui.Gui.quit()
            self.Gui.Gui.destroy()
            exit()
