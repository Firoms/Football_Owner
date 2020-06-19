from tkinter import *
from Get_Image import Get_image


class Menu_Screen:
    def __init__(self):
        self.Gui = Tk()
        self.Gui.title("Football Owner")
        self.Gui.geometry("800x800")
        self.Gui.resizable(width=None, height=None)
        GameScreen_background = Get_image.image(
            self, "background2.jpg", 0, 0, 0.5, 0.5)
        self.Gui.mainloop()


start = Menu_Screen()
