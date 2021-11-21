from tkinter import *
from tkinter import ttk as ttk
from .Base import Base
import json
import webbrowser

class Acknowledgements(Base):
    '''Acknowledgements API'''
    def __init__(self):
        super().__init__('600x700', 'Acknowledgements', 'Acknowledgements')

        # Get data
        with open('acknowledgements.json', 'r') as f:
            data = json.load(f)
        
        # Frame for acknowledgements
        acknowledgements_frame = Frame(self, background='#101414', highlightbackground='white', highlightcolor='white', highlightthickness=1, pady=30)

        # Subtitle
        Label(acknowledgements_frame, text='GWPC Check-in 2.0 is made with open source libraries', font=('*', 25), background='#101414').pack()

        # Libraries
        for library in data:
            link = Label(acknowledgements_frame, text=library, font=('*', 18), fg='cyan', cursor='hand2', background='#101414')
            link.pack()
            link.bind('<Button-1>', lambda e: webbrowser.open_new_tab(f'https://github.com/{e.widget["text"]}'))

        acknowledgements_frame.pack()