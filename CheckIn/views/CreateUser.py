import re
from tkinter import *
from tkinter import messagebox
from tkinter import ttk as ttk

from .Base import Base
from ..User import User


class CreateUser(Base):
    """Create user GUI"""

    def __init__(self, studentID: int):
        super().__init__(geometry='575x575', title='Sign up')

        self.draw_window(studentID)

    def draw_window(self, studentID: int):
        """Draws to screen"""

        # Frame for inputs
        signup_frame = Frame(self, background='#101414', highlightbackground='white', highlightcolor='white',
                             highlightthickness=1, pady=30)

        # Full name
        fullname_frame = Frame(signup_frame, background='#101414', pady=7)
        fullname_frame.pack(fill=BOTH)
        Label(fullname_frame, text='Full name: ', background='#101414', anchor='w', foreground='white').pack(fill=BOTH)
        self.fullname_entry = ttk.Entry(signup_frame, background='#101414', width=60)
        self.fullname_entry.pack(ipady=3)

        # School email
        school_email_frame = Frame(signup_frame, background='#101414', pady=7)
        school_email_frame.pack(fill=BOTH)
        Label(school_email_frame, text='School email: ', background='#101414', anchor='w', foreground='white').pack(
            fill=BOTH)
        self.school_email_entry = ttk.Entry(signup_frame, background='#101414', width=60)
        self.school_email_entry.pack(ipady=3)

        # Phone number
        phonenumber_frame = Frame(signup_frame, background='#101414', pady=7)
        phonenumber_frame.pack(fill=BOTH)
        Label(phonenumber_frame, text='Phone number: ', background='#101414', anchor='w', foreground='white').pack(
            fill=BOTH)
        self.phonenumber_entry = ttk.Entry(signup_frame, background='#101414', width=60)
        self.phonenumber_entry.pack(ipady=3)

        # Address
        address_frame = Frame(signup_frame, background='#101414', pady=7)
        address_frame.pack(fill=BOTH)
        Label(address_frame, text='Address: ', background='#101414', anchor='w', foreground='white').pack(fill=BOTH)
        self.address_entry = ttk.Entry(signup_frame, background='#101414', width=60)
        self.address_entry.pack(ipady=3)

        # Student ID
        studentID_frame = Frame(signup_frame, background='#101414', pady=7)
        studentID_frame.pack(fill=BOTH)
        Label(studentID_frame, text='Student ID: ', background='#101414', anchor='w', foreground='white').pack(
            fill=BOTH)
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
        school_email = self.school_email_entry.get().strip()
        phonenumber = self.phonenumber_entry.get().strip()
        address = self.address_entry.get().strip()
        studentID = self.studentID_entry.get().strip()

        # Validation
        if not fullname:
            messagebox.showerror('Error', 'Please enter your full name.')
        elif not re.match('[a-zA-Z0-9]+@hdsb.ca', school_email):
            messagebox.showerror('Error', 'Please enter your school email address.')
        elif not phonenumber.isnumeric() and not re.match(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$',
                                                          phonenumber):
            messagebox.showerror('Error', 'Please enter your phone number.')
        elif not address:
            messagebox.showerror('Error', 'Please enter your address.')
        elif not studentID.isnumeric():
            messagebox.showerror('Error', 'Please scan your student ID barcode.')
        else:
            # Create user
            User.create_new_user(fullname, school_email, phonenumber, address, int(studentID))
            # Check in user
            checked_in_info = User.checkin_user(studentID)
            # Confirmation
            messagebox.showinfo('User created', f'Created new user {fullname}, and checked in at {checked_in_info[1]}.')
            self.destroy()
