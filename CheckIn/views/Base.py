from tkinter import *
from PIL import ImageTk, Image
from abc import ABC


class Base(Toplevel, ABC):
    """The base class for the GUI"""

    def __init__(self, geometry: str = '', title: str = ''):
        super().__init__()

        self.config(background='#101414')

        geometry and self.geometry(geometry)

        self.title(f'GWPC Check-in 2.0{f" - {title}" if title else ""}')

        # Logo
        logo = ImageTk.PhotoImage(Image.open('gwpc-logo.png').resize((60, 60)), Image.ANTIALIAS)

        # Title bar wrapper frame (background)
        titlebar_bg_frame = Frame(self, background='#22252a')
        # Title bar frame
        titlebar_frame = Frame(titlebar_bg_frame, background='#22252a')
        # Title bar logo
        logo_label = Label(titlebar_frame, image=logo, background='#22252a', foreground='white')
        logo_label.image = logo
        logo_label.pack(side=LEFT)
        # Title
        title = Label(titlebar_frame, text=title if title else 'GWPC Check-in 2.0', height=2, font=('*', 32),
                      background='#22252a', foreground='white')
        title.pack(side=LEFT)
        # Pack frames
        titlebar_frame.pack()
        titlebar_bg_frame.pack(fill=BOTH)
