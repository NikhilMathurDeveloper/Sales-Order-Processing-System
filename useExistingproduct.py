from tkinter import *

import sqlite3

from tkinter import messagebox
from tkinter import ttk
from tkcalendar import *
import smtplib

def open21():
    class useExistingProduct:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            self.title = Label(window, text="Select Existing product",font = "Verdana 32 bold").pack(pady=20)

            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()

            
            def insertIntoFormat(list1, result):
                for i in result:
                    list1.append(i[0])
                return list1
            
            try:
                #Query to identify the products which have an amount less than 50.
                queryResultStorage = []
                cursor.execute("SELECT ProductName FROM Product WHERE Amount < 50")
                queryResult = cursor.fetchall()
                insertIntoFormat(queryResultStorage, queryResult)


                #Front End Initalization 
                labelInfo = Label(window, text="Please select product!",font = "Verdana 14 bold").pack(pady=5)
                
                dropDown = StringVar(window)
                dropDown.set(queryResultStorage[0])
                drop = OptionMenu(window, dropDown, *queryResultStorage)
                drop.pack()
                drop.configure(width=20)

                label = Label(window, text="Enter Amount required", font = "Verdana 14 bold").pack(pady=5)
                textVariable = StringVar(window)
                enterAmount = Entry(window, textvariable=textVariable).pack(pady=5)

                label5 = Label(window, text="Please select requirement date: ", font = "Verdana 14 bold").pack(pady=5)
                cal = Calendar(window, selectmode='day', date_pattern ='d/m/yy', background="blue")
                cal.pack(pady=5)
            except:
                messagebox.showinfo(message="An error occured")

            def send(productName):
                
                    #Paramaterized Query which selects products cateogoryID, contactEmailAddress.
                    #Information used with body of email.
                    #Email address, , category name, 
                
                    
                    '''

                    query = """SELECT Product.CategoryID ,(SELECT contactEmailaddress FROM Supplier WHERE CategoryID = Product.CategoryID),
                    (SELECT name FROM Department WHERE CategoryID = Product.CategoryID)
                    FROM Product WHERE productName = ?"""
                    '''

                    query = """SELECT Supplier.contactEmailAddress FROM Supplier INNER JOIN Product ON
                    Supplier.CategoryID = Product.CategoryID
                    WHERE Product.ProductName = ?"""

                    

  
                    


                    cursor.execute(query,(productName, ))
                    combinedQuery = cursor.fetchall()
                    print(combinedQuery)

                    query2 = """SELECT Department.name FROM Department 
                    INNER JOIN Product ON Department.CategoryID = Product.CategoryID WHERE Product.ProductName = ?"""
                    cursor.execute(query2,(productName, ))
                    combinedQuery2 = cursor.fetchall()
                    print(combinedQuery2)
                    
           
                    print(textVariable.get())
                    
                    sender = "computersciencetest6@gmail.com"

                    reciever = combinedQuery[0][0]

                    password = "vmvpienhhrgtmatq"
                    #Query results supplied to body of message.
                    body = f"""

                    Subject: Products needed!\n
                    Product: {dropDown.get()}\n
                    Amount: {textVariable.get()} kg\n
                    Date: {cal.get_date()}\n
                    Department : {combinedQuery2[0][0]}\n

                    """

                    server = smtplib.SMTP('smtp.gmail.com',587)

                    server.starttls()

                    server.login(sender, password)

                    server.sendmail(sender, reciever, body)

                    
                    print("Mail Sent")
                    messagebox.showinfo(message="Mail Sent")
                    server.close()
           
            button = Button(window, text="Send Mail", font = "Verdana 14 bold", command=lambda:send(dropDown.get())).pack(pady=5)
   


    window = Tk()
    obj = useExistingProduct(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()