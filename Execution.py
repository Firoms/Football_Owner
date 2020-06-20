from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox
from Menu_Screen import Menu_Screen
import sys
import os


class Execution:
    def __init__(self):
        self.Gui = Tk()
        self.Gui.title("Football Owner")
        self.Gui.geometry("1203x803")
        self.Gui.resizable(width=False, height=False)
        execute_location = self.center_window(1203, 803)
        Make_menu = self.Game_menu()
        execute_Menu_Screen = Menu_Screen(self)
        self.Gui.mainloop()

    def center_window(self, width, height):
        screen_width = self.Gui.winfo_screenwidth()
        screen_height = self.Gui.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2) - 25
        self.Gui.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def Game_menu(self):
        def _quit():
            self.screen.quit()
            self.screen.destroy()
            exit()

        def _msgBox():
            tkinter.messagebox.showinfo(
                'About', '아직 미완성')

        def restart_program():
            python = sys.executable
            os.execl(python, python, * sys.argv)

        menu_bar = Menu(self.Gui)
        self.Gui.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Restart", command=restart_program)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=_quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        help_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=_msgBox)


if __name__ == "__main__":
    execute = Execution()
