from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox
from .Base import Base
from .CreateUser import CreateUser
from ..User import User
from ..Database import Database
import webbrowser

class App(Base):
    '''Main GUI'''
    def __init__(self):
        super().__init__('800x600')

        # Frame for input section
        input_frame = Frame(self, background='#101414')
        input_frame2 = Frame(input_frame, background='#101414')

        # Student ID Label
        studentid_label = Label(input_frame2, text='Student ID: ', font=('*', 20), background='#101414')
        studentid_label.pack(side=LEFT)

        # Input
        self.studentid_entry = ttk.Entry(input_frame2, background='#101414', width=40)
        self.studentid_entry.pack(ipady=3, side=LEFT)
        self.studentid_entry.focus()

        input_frame2.pack()

        # Check-in button
        checkin_button = ttk.Button(input_frame, text='Check-in', command=self.checkin)
        checkin_button.pack(side=RIGHT)

        self.bind('<Return>', self.checkin)

        input_frame.pack(pady=(20, 0))


        # Frame for credits links
        credits_frame = Frame(self, background='#101414')

        # Made by Jason
        madeby_link = Label(credits_frame, text='Made by Jason', font=('*', 18), fg='cyan', cursor='hand2', background='#101414')
        madeby_link.pack(side=LEFT, padx=30)
        madeby_link.bind('<Button-1>', lambda e: webbrowser.open_new_tab('https://jasonli0616.dev'))

        # Push data
        pushdata_link = Label(credits_frame, text='Push data', font=('*', 18), fg='cyan', cursor='hand2', background='#101414')
        pushdata_link.pack(side=LEFT, padx=30)
        pushdata_link.bind('<Button-1>', self.push_data)

        # Acknowledgements
        acknowledgement_link = Label(credits_frame, text='Acknowledgements', font=('*', 18), fg='cyan', cursor='hand2', background='#101414')
        acknowledgement_link.pack(side=LEFT, padx=30)
        acknowledgement_link.bind('<Button-1>', lambda e: print('Push data'))

        credits_frame.pack(side=BOTTOM, pady=(0, 30))
    
    def checkin(self, *args):
        '''Check in user'''

        studentID = self.studentid_entry.get().strip()

        if studentID.isnumeric():
            
            if User.check_user_exists(studentID):
                checkedin_info = User.checkin_user(studentID)
                messagebox.showinfo('Checked-in', f'Checked-in user {checkedin_info[0]} at {checkedin_info[1]}.')
            else:
                CreateUser(studentID).mainloop()

        else:
            messagebox.showerror('Error', 'Please scan your student ID barcode.')
        
        self.studentid_entry.delete(0, END)
    
    def push_data(self, *args):

        Database.push_data()
        Database.pull_data()
        messagebox.showinfo('Updated data', 'Data has been updated.')