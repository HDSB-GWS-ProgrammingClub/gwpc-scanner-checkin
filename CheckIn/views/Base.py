from abc import ABC
from tkinter import *

from PIL import ImageTk, Image


class Base(Toplevel, ABC):
    """The base class for the GUI"""

    def __init__(self, geometry: str = '', title: str = ''):
        super().__init__()

        self._configure_window(geometry, title)
        self._draw_window(geometry, title)

    def _configure_window(self, geometry: str, title: str):
        """Configure the window"""

        # Set background colour
        self.config(background='#101414')

        # Set window size (if applicable)
        if geometry:
            self.geometry(geometry)

        # Set window title
        self.title(f'GWPC Check-in 2.0{f" - {title}" if title else ""}')

    def _draw_window(self, geometry: str, title: str):
        """Draws to screen"""

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
