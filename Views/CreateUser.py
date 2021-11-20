from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox
from .Base import Base

class CreateUser(Base):
    '''Create user GUI'''
    def __init__(self, studentID: int):
        super().__init__('575x575', title='Sign up', titlebar='Sign up')

        Label(self, text=str(studentID)).pack()