from tkinter import *
from tkinter import ttk as ttk
from PIL import ImageTk, Image

class Base(Toplevel):
    '''The base class for the GUI'''
    def __init__(self, geometry: str, title: str = '', titlebar: str = 'GWPC Check-in 2.0'):
        super().__init__()

        self.config(background='#101414')

        self.geometry(geometry)
        if title:
            self.title(f'GWPC Check-in 2.0 - {title}')
        else:
            self.title('GWPC Check-in 2.0')

        # Logo
        logo = ImageTk.PhotoImage(Image.open('gwpc-logo.png').resize((60, 60)), Image.ANTIALIAS)

        # Title bar wrapper frame (background)
        titlebar_bg_frame = Frame(self, background='#22252a')
        # Title bar frame
        titlebar_frame = Frame(titlebar_bg_frame, background='#22252a')
        # Title bar logo
        logo_label = Label(titlebar_frame, image=logo, background='#22252a')
        logo_label.image = logo
        logo_label.pack(side=LEFT)
        # Title
        title = Label(titlebar_frame, text=titlebar, height=2, font=('*', 32), background='#22252a')
        title.pack(side=LEFT)
        # Pack frames
        titlebar_frame.pack()
        titlebar_bg_frame.pack(fill=BOTH)