from Get_Image import Get_image
from Main_Screen import Main_Screen
from tkinter import *


class Menu_Screen:
    def __init__(self, Gui):
        Menu_Screen_background = Get_image.image_label(
            Gui, "Main_Screen_bg.png", 0, 0)
        Game_Start_button = Get_image.image_button(
            Gui, "Game_Start_btn.png", 20, 350, Main_Screen())
        HowToPlay_button = Get_image.image_button(
            Gui, "HowToPlay_btn.png", 20, 450, Main_Screen())
        Settings_button = Get_image.image_button(
            Gui, "Settings_btn.png", 20, 550, Main_Screen())
        Exit_button = Get_image.image_button(
            Gui, "Exit_btn.png", 20, 650, Gui.Gui.destroy)
        Version_label = Label(Gui.Gui, text="Version 0.01",
                              fg="green", font=("맑은 고딕", 12), height=1)
        Version_label.place(x=1100, y=5)
