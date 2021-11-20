from tkinter import *
from tkinter import messagebox
import CheckIn



# Make root window invisible
root = Tk()
root.geometry('0x0')

CheckIn.Database.pull_data()

app = CheckIn.views.App()

def on_close():
    '''Push data on close'''

    messagebox.showinfo('Pushing data', 'Pushing data...')
    CheckIn.Database.push_data()
    CheckIn.Database.shutdown()
    messagebox.showinfo('Updated data', 'Data has been updated.')
    root.destroy()

app.protocol('WM_DELETE_WINDOW', on_close)

root.mainloop()