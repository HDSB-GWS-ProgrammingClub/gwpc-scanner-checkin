from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox
from .Base import Base
from CheckIn.User import User
import re

class CreateUser(Base):
    '''Create user GUI'''
    def __init__(self, studentID: int):
        super().__init__('575x575', title='Sign up', titlebar='Sign up')

        # Frame for inputs
        signup_frame = Frame(self, background='#101414', highlightbackground='white', highlightcolor='white', highlightthickness=1, pady=30)

        # Full name
        fullname_frame = Frame(signup_frame, background='#101414', pady=7)
        fullname_frame.pack(fill=BOTH)
        Label(fullname_frame, text='Full name: ', background='#101414', anchor='w').pack(fill=BOTH)
        self.fullname_entry = ttk.Entry(signup_frame, background='#101414', width=60)
        self.fullname_entry.pack(ipady=3)

        # School email
        schoolemail_frame = Frame(signup_frame, background='#101414', pady=7)
        schoolemail_frame.pack(fill=BOTH)
        Label(schoolemail_frame, text='School email: ', background='#101414', anchor='w').pack(fill=BOTH)
        self.schoolemail_entry = ttk.Entry(signup_frame, background='#101414', width=60)
        self.schoolemail_entry.pack(ipady=3)

        # Phone number
        phonenumber_frame = Frame(signup_frame, background='#101414', pady=7)
        phonenumber_frame.pack(fill=BOTH)
        Label(phonenumber_frame, text='Phone number: ', background='#101414', anchor='w').pack(fill=BOTH)
        self.phonenumber_entry = ttk.Entry(signup_frame, background='#101414', width=60)
        self.phonenumber_entry.pack(ipady=3)

        # Address
        address_frame = Frame(signup_frame, background='#101414', pady=7)
        address_frame.pack(fill=BOTH)
        Label(address_frame, text='Address: ', background='#101414', anchor='w').pack(fill=BOTH)
        self.address_entry = ttk.Entry(signup_frame, background='#101414', width=60)
        self.address_entry.pack(ipady=3)

        # Student ID
        studentID_frame = Frame(signup_frame, background='#101414', pady=7)
        studentID_frame.pack(fill=BOTH)
        Label(studentID_frame, text='Student ID: ', background='#101414', anchor='w').pack(fill=BOTH)
        self.studentID_entry = ttk.Entry(signup_frame, background='#101414', width=60)
        self.studentID_entry.pack(ipady=3)
        self.studentID_entry.insert(0, studentID)

        signup_frame.pack()



        # Sign up button
        signup_button = ttk.Button(self, text='Sign up', command=self.sign_up)
        signup_button.pack()

        self.bind('<Return>', self.sign_up)
    
    def sign_up(self, *args):
        fullname = self.fullname_entry.get().strip()
        schoolemail = self.schoolemail_entry.get().strip()
        phonenumber = self.phonenumber_entry.get().strip()
        address = self.address_entry.get().strip()
        studentID = self.studentID_entry.get().strip()

        # Validation
        if not fullname or not fullname.isalpha():
            messagebox.showerror('Error', 'Please enter your full name.')
        elif not re.match('/[a-zA-Z0-9]+@hdsb.ca/', schoolemail):
            messagebox.showerror('Error', 'Please enter your school email.')
        elif not address:
            messagebox.showerror('Error', 'Please enter your address.')
        elif not phonenumber.isalnum() or not re.match('^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$', phonenumber):
            messagebox.showerror('Error', 'Please enter your phone number.')
        elif not studentID.isnumeric():
            messagebox.showerror('Error', 'Please scan your student ID barcode.')
        else:
            User.create_new_user(fullname, schoolemail, phonenumber, address, int(studentID))
            messagebox.showinfo('User created', f'Created new user {fullname}.')