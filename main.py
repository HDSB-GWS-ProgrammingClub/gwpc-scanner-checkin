from tkinter import *
from tkinter import messagebox
import CheckIn



# Make root window invisible
root = Tk()
root.geometry('0x0')

def pull_data():
    # Pull data
    if CheckIn.Internet.connected_to_internet():
        # If connected to the internet

        # Pull data
        CheckIn.Database.pull_data()
    else:
        # If not connected to the internet, ask to retry
        retry = messagebox.askretrycancel('Error', 'You are not connected to the internet. Connect to the internet and try again.')
        if retry:
            pull_data()

pull_data()

# Run main app GUI
app = CheckIn.views.App()

def on_close():
    '''Push data on close'''

    if CheckIn.Internet.connected_to_internet():
        # If connected to the internet

        # Push data
        messagebox.showinfo('Pushing data', 'Pushing data...')
        CheckIn.Database.push_data()
        messagebox.showinfo('Updated data', 'Data has been updated.')
        # Destroy GUI
        root.destroy()
        # Delete local database
        CheckIn.Database.shutdown()
    else:
        # If not connected to the internet, ask to retry
        retry = messagebox.askretrycancel('Error', 'You are not connected to the internet. Connect to the internet and try again.')
        if retry:
            on_close()

app.protocol('WM_DELETE_WINDOW', on_close)
root.protocol('WM_DELETE_WINDOW', on_close)

root.mainloop()