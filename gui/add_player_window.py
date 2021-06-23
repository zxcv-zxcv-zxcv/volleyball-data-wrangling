from tkinter import *
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
from tkinter import messagebox
import re

class addPlayerWindow():

    def __init__(self, master):
        master.title('Add New Player')
        
        
        self.titleLabel = Label(master, text="Add Player Info")



        self.exitButton = Button(master, text= "Cancel", command=master.destroy, padx=20, pady=10)


        self.titleLabel.grid(row=0, column=0)
        self.exitButton.grid(row=99, column=4)
        return

    def checkString(self, String):
        
        regex=re.compile('[@_!#$%^&*()<>?/\|}{~:1234567890]')

        if(regex.search(String) == None):
            return True
        else:
            return False