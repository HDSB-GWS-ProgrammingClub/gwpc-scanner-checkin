import webbrowser
from tkinter import *
from tkinter import messagebox
from tkinter import ttk as ttk

from .Acknowledgements import Acknowledgements
from .Base import Base
from .CreateUser import CreateUser
from ..Database import Database
from ..Internet import Internet
from ..User import User


class App(Base):
    """Main GUI"""

    def __init__(self):
        super().__init__(geometry='800x600')

        self._pull_data()
        self.draw_window()

        self.protocol('WM_DELETE_WINDOW', self._on_close)

    def draw_window(self):
        """Draws to screen"""

        # Frame for input section
        input_frame = Frame(self, background='#101414')
        input_frame2 = Frame(input_frame, background='#101414')

        # Student ID Label
        studentID_label = Label(input_frame2, text='Student ID: ', font=('*', 20), background='#101414',
                                foreground='white')
        studentID_label.pack(side=LEFT)

        # Input
        self.studentID_entry = ttk.Entry(input_frame2, background='#101414', width=40)
        self.studentID_entry.pack(ipady=3, side=LEFT)
        self.studentID_entry.focus()

        input_frame2.pack()

        # Check-in button
        checkin_button = ttk.Button(input_frame, text='Check-in', command=self.checkin)
        checkin_button.pack(side=RIGHT)

        self.bind('<Return>', self.checkin)

        input_frame.pack(pady=(20, 0))

        # Frame for credits links
        credits_frame = Frame(self, background='#101414')

        # Made by Jason
        madeby_link = Label(credits_frame, text='Made by Jason', font=('*', 14), fg='cyan', cursor='hand2',
                            background='#101414')
        madeby_link.pack(side=LEFT, padx=30)
        madeby_link.bind('<Button-1>', lambda e: webbrowser.open_new_tab('https://jasonli0616.dev'))

        # Push data
        pushdata_link = Label(credits_frame, text='Push data', font=('*', 14), fg='cyan', cursor='hand2',
                              background='#101414')
        pushdata_link.pack(side=LEFT, padx=30)
        pushdata_link.bind('<Button-1>', self.push_data)

        # Acknowledgements
        acknowledgement_link = Label(credits_frame, text='Acknowledgements', font=('*', 14), fg='cyan', cursor='hand2',
                                     background='#101414')
        acknowledgement_link.pack(side=LEFT, padx=30)
        acknowledgement_link.bind('<Button-1>', lambda e: Acknowledgements().mainloop())

        credits_frame.pack(side=BOTTOM, pady=(0, 30))

    def checkin(self, *args):
        """Check in user"""

        studentID = self.studentID_entry.get().strip()

        self.studentID_entry.delete(0, END)
        self.studentID_entry.focus()

        if studentID.isnumeric():
            if User.check_user_exists(studentID):
                # If user exists, check-in
                checked_in_info = User.checkin_user(studentID)
                messagebox.showinfo('Checked-in', f'Checked-in user {checked_in_info[0]} at {checked_in_info[1]}.')
            else:
                # Else create user
                CreateUser(studentID).mainloop()
        else:
            # User does not exist
            messagebox.showerror('Error', 'Please scan your student ID barcode.')

    def _pull_data(self):
        """Pull data on app launch"""
        if Internet.connected_to_internet():
            # If connected to the internet

            # Pull data
            Database.pull_data()
        else:
            # If not connected to the internet, ask to retry
            retry = messagebox.askretrycancel('Error',
                                              'You are not connected to the internet. Connect to the internet and try again.')
            if retry:
                self.pull_data()

    def push_data(self, *_):
        if Internet.connected_to_internet():
            # If connected to the internet

            # Push data, then pull data
            Database.push_data()
            Database.pull_data()
            messagebox.showinfo('Updated data', 'Data has been updated.')
        else:
            # If not connected to the internet, ask to retry
            retry = messagebox.askretrycancel('Error',
                                              'You are not connected to the internet. Connect to the internet and try again.')
            if retry:
                self.push_data()

    def _on_close(self):
        """Push data on close"""

        if Internet.connected_to_internet():
            # If connected to the internet

            # Push data
            messagebox.showinfo('Pushing data', 'Pushing data...')
            Database.push_data()
            messagebox.showinfo('Updated data', 'Data has been updated.')

            # Destroy GUI
            self.destroy()

            # Delete local database
            Database.shutdown()
        else:
            # If not connected to the internet, ask to retry
            retry = messagebox.askretrycancel('Error',
                                              'You are not connected to the internet. Connect to the internet and try again.')
            if retry:
                self._on_close()
