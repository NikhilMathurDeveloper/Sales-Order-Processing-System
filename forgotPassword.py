#Neccessary modules, from local files and libraries. 
from tkinter import *


import sqlite3
from tkinter import messagebox
from unittest import result
from clients import open2

from product import open7

from order import open11
from invoice import open12

from delivery import open14
from reports import open23
def open28():
    class forgotPassword:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            #Initializing front end. Combining function calls with buttons.

            #Front End 
            self.title = Label(window, text="Forgot Menu", font = "Verdana 32 bold").pack(pady=20)

            enterLabel = Label(window, text="Enter Username", font = "Verdana 16 bold").pack(pady=5)

            info = StringVar(window)
            enterUsername = Entry(window, textvariable=info).pack(pady=5)

            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()
            #Gets details according to user entered username
            def getDetails(username):
                
                try:
                    #Selects email according to corresponding employee username
                    query = """SELECT Email FROM REGISTER WHERE EmployeeUsername =?"""
                    cursor.execute(query, (username,))
                    #Fetches result
                    resultFromQuery = cursor.fetchall()

                    #Front end initalization
                    email1 = StringVar(window)
                    emailInfo = Label(window, text="Enter Email: ").pack(pady=5)
                    enterEmail = Entry(window, textvariable=email1).pack(pady=5)
                    def hash1(hash_key, numberOFSlots):
                        sum = 0
                        for i in range(0,len(hash_key)-1):
                            ascii_code = ord(hash_key[i])
                            sum = sum + ascii_code
                        hash_value = sum % numberOFSlots
                        return hash_value
                    #Checks if email entered is matching to corresponding table information
                    def check(email):
                        #Update function which updates the neccessary rows accordingly.
                        def update(password, employeeUsername):
                            #paramterized SQL
                            query = """UPDATE REGISTER SET Password = ? WHERE EmployeeUsername = ?"""
                            cursor.execute(query, (password, employeeUsername,))
                            db.commit()
                            print(password)
                        #Checks if the email entered is matching.
                        try:
                            if email == resultFromQuery[0][0]:
                                #Hash function to get confidential password.
                                title1 = Label(window, text="Enter new password", font = "Verdana 16 bold").pack(pady=5)
                                entryPass = StringVar(window)
                                entryPassword = Entry(window, textvariable=entryPass).pack(pady=5)
                    
                                #Calls function
                                def changePassword():
                                    print(entryPass.get())
                                    update(hash1(entryPass.get(),100), info.get())
                                    messagebox.showinfo(message="Your Password has been changed")
                                #Front End initalization 
                                button = Button(window, text="Enter", command=changePassword, font = "Verdana 16 bold").pack(pady=5)
                            else:
                                messagebox.showinfo(message="Your email is wrong")
                                open28()
                        except:
                            messagebox.showinfo(message="Your Email does not exist")
                            #Enteries initalized allowing user to enter new password
                            
                            
                           
                    
                    #Front end initalization  
                    button = Button(window, text="Check", command=lambda:check(email1.get()), font = "Verdana 20 bold").pack(pady=5)
                except:
                    messagebox.showinfo(message="The username does not exist")
                    open28()
         
            button = Button(window, text="Check", command=lambda:getDetails(info.get()),font = "Verdana 16 bold").pack(pady=5)

            


    window = Tk()
    obj = forgotPassword(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()