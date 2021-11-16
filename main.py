from tkinter import *
from tkinter import ttk as ttk
from PIL import Image, ImageTk

class App(Tk):
    def __init__(self):
        super().__init__()

        self.config(background='#101414')

        self.geometry('800x600')
        self.title('GWPC Check-in 2.0')


        # Title bar
        logo = ImageTk.PhotoImage(Image.open('public/img/gwpc-logo.png'))
        title = Label(self, text='GWPC Check-in 2.0', image=logo, height=2, font=('*', 32), background='#22252a')
        title.pack(fill=BOTH)


root = App()
root.mainloop()