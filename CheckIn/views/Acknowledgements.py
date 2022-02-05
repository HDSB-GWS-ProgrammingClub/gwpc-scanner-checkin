from tkinter import *
from .Base import Base
import json
import webbrowser


class Acknowledgements(Base):
    """Acknowledgements GUI"""

    def __init__(self):
        super().__init__(title='Acknowledgements')

        self.draw_window(self._get_data())

    @staticmethod
    def _get_data() -> list:
        """
        Get libraries from JSON file

        Returns: list of libraries
        """
        with open('acknowledgements.json', 'r') as f:
            return json.load(f)

    def draw_window(self, data: list):
        """Draws to screen"""

        # Frame for acknowledgements
        acknowledgements_frame = Frame(self, background='#101414', highlightbackground='white', highlightcolor='white',
                                       highlightthickness=1, pady=20)

        # Subtitle
        Label(acknowledgements_frame, text='GWPC Check-in 2.0 is made with open source libraries', font=('*', 15),
              background='#101414', foreground='white').pack()

        # Libraries
        for library in data:
            link = Label(acknowledgements_frame, text=library, font=('*', 12), fg='cyan', cursor='hand2',
                         background='#101414')
            link.pack()
            link.bind('<Button-1>', lambda e: webbrowser.open_new_tab(f'https://github.com/{e.widget["text"]}'))

        acknowledgements_frame.pack()
