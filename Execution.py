from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
from Screen import Screen
import threading
from playsound import playsound
import sys
import os
import time


class Execution:
    def __init__(self):
        self.Gui = Tk()
        self.Gui.title("Football Owner")
        self.Gui.geometry("1203x803")
        self.Gui.resizable(width=False, height=False)
        execute_location = self.center_window(1203, 823)
        self.Gui.iconbitmap('images/logo.ico')
        Make_menu = self.Game_menu()

        def songthread():
            while True:
                playsound('music/Alone_Together.mp3')
                time.sleep(1)
        song_thread = threading.Thread(target=songthread)
        song_thread.daemon = True
        song_thread.start()
        execute_Menu_Screen = Screen(self)
        self.Gui.mainloop()

    def center_window(self, width, height):
        screen_width = self.Gui.winfo_screenwidth()
        screen_height = self.Gui.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2) - 25
        self.Gui.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def Game_menu(self):
        def _msgBox():
            tkinter.messagebox.showinfo(
                '소개', 'Firoms가 만든 Football_Owner\n 약 8000명의 축구 선수와 함께하는 시뮬레이션 게임입니다.')

        def _quit():
            answer = messagebox.askyesno("확인", "정말 종료하시겠습니까?")
            if answer == True:
                self.Gui.quit()
                self.Gui.destroy()
                exit()

        def restart_program():
            answer = messagebox.askyesno("확인", "정말 재시작하시겠습니까?")
            if answer == True:
                python = sys.executable
                os.execl(python, python, * sys.argv)

        menu_bar = Menu(self.Gui)
        self.Gui.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(
            label="재시작", command=restart_program)
        file_menu.add_separator()
        file_menu.add_command(label="종료", command=_quit)
        menu_bar.add_cascade(label="파일", menu=file_menu)
        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="정보", menu=help_menu)
        help_menu.add_command(label="소개", command=_msgBox)


if __name__ == "__main__":
    execute = Execution()
