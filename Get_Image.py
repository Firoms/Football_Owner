from tkinter import *
import os
from PIL import ImageTk


class Get_image:
    def image(self, file_name, x, y, rw, rh):
        img_path = os.path.join(os.getcwd(), "images")
        final_path = os.path.join(img_path, file_name)
        image = ImageTk.PhotoImage(file=final_path)
        image_label = Label(self.Gui)
        image_label.configure(image=image)
        image_label.image = image
        image_label.place(x=x, y=y, relwidth=rw,
                          relheight=rh)
