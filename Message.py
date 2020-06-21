import sys
from tkinter import messagebox
import tkinter.messagebox
import os


class Message:
    def _quit(Gui):
        answer = messagebox.askyesnocancel("확인", "정말 종료하시겠습니까?")
        if answer == True:
            Gui.Gui.quit()
            Gui.Gui.destroy()
            exit()

    def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
