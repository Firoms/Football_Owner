from Get_Image import Get_image
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
        Version_label = Label(self.Gui.Gui, text="Version 0.02",
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
        first_save_btn = Button(self.Gui.Gui, text="+",
                                bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21)
        first_save_btn.place(x=75, y=198)
        second_save_btn = Button(self.Gui.Gui, text="+",
                                 bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21)
        second_save_btn.place(x=75, y=402)
        third_save_btn = Button(self.Gui.Gui, text="+",
                                bg="yellowgreen", fg="blue", font=("맑은 고딕", 45), width=21)
        third_save_btn.place(x=75, y=606)

    def _quit(self):
        answer = messagebox.askyesno("확인", "정말 종료하시겠습니까?")
        if answer == True:
            self.Gui.Gui.quit()
            self.Gui.Gui.destroy()
            exit()
