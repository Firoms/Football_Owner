from tkinter import *
import os
from PIL import ImageTk


class Get_image:
    def image_label(Gui, file_name, x, y):
        img_path = os.path.join(os.getcwd(), "images")
        final_path = os.path.join(img_path, file_name)
        image = ImageTk.PhotoImage(file=final_path)
        image_label = Label(Gui.Gui)
        image_label.configure(image=image)
        image_label.image = image
        image_label.place(x=x, y=y)

    def image_button(Gui, file_name, x, y, command):
        img_path = os.path.join(os.getcwd(), "images")
        final_path = os.path.join(img_path, file_name)
        image = ImageTk.PhotoImage(file=final_path)
        image_button = Button(
            Gui.Gui, overrelief=SOLID,  command=command)
        image_button.configure(image=image)
        image_button.image = image
        image_button.place(x=x, y=y)
