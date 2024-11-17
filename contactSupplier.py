from tkinter import *

import sqlite3

from tkinter import messagebox

from tkinter import ttk
from tkcalendar import *
import smtplib
from useExistingproduct import open21
from datetime import datetime, timedelta

def open20():
    class contactSupplier:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            self.title = Label(window, text="Contact Supplier", font = "Verdana 32 bold").pack(pady=20)

            #Connecting to database

            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()

            def insertIntoFormat(list1, result):
                for i in result:
                    list1.append(i[0])
                return list1

            try:
                label = Label(window, text="These are the products which are low in quantity", font = "Verdana 14 bold").pack(pady=10)
                def openExisting():
                    open21()
                button = Button(window, text="Use one of these products", font = "Verdana 14 bold", command=openExisting).pack(pady=10)
            except:
                messagebox.showinfo(message="There are no exisitng products which are low in stock!")


            try:
                dropDownStorage1 = []
                #SQL Query, results supplied to front end interface, allowing selection to be easier.
                cursor.execute("SELECT name FROM Department")
                #Front End creation
                label2 = Label(window, text="Please select Department: ", font = "Verdana 14 bold").pack(pady=10)
                queryResult1 = cursor.fetchall()
                insertIntoFormat(dropDownStorage1, queryResult1)

            except:
                messagebox.showinfo(message="Not enough of info")
            
            dropDown2 = StringVar(window)
            
            def getProducts(department_name):
                dropDownStorageProduct = []
            
                queryID = "SELECT CategoryID FROM department WHERE name = ? "
                cursor.execute(queryID,(department_name, ))
                queryIDresult = cursor.fetchall()
                print(queryIDresult)
                def retrieveProductname(queryIDResult1):
                    query = "SELECT ProductName FROM Product WHERE CategoryID = ?"
                    cursor.execute(query, (queryIDResult1[0][0],))
                    queryResultProduct = cursor.fetchall()
                    insertIntoFormat(dropDownStorageProduct, queryResultProduct)
                    print(queryResultProduct)
                    print(dropDownStorageProduct)
                    
                retrieveProductname(queryIDresult)

            
                

                
                
                dropDown2.set(dropDownStorageProduct[0])
                drop2 = OptionMenu(window, dropDown2, *dropDownStorageProduct)
                drop2.place(x=790, y=250)
                drop2.configure(width=20)
 
     



           
            
           #Front end Intialization 

            try:
                dropDown1 = StringVar(window)
                dropDown1.set(dropDownStorage1[0])
                drop1 = OptionMenu(window, dropDown1, *dropDownStorage1)
                drop1.pack()
                drop1.configure(width=20)
            except:
                messagebox.showinfo(message="Not enough of info")
            
            
           
            

            button = Button(window, text="Get products", command=lambda:getProducts(dropDown1.get()),  font = "Verdana 14 bold").pack(pady=5)


            #Front End initalization 

            

            label4 = Label(window, text="Please Enter Amount: ", font = "Verdana 14 bold").pack(pady=10)
            enterAmount = Entry(window)
            enterAmount.pack(pady=5)

            label5 = Label(window, text="Please select requirement date: ", font = "Verdana 14 bold").pack(pady=10)
            cal = Calendar(window, selectmode='day', date_pattern ='d/m/yy', background="blue")
            cal.pack(pady=5)

            #Function which sends emaul with all neccessary components
            #takes categoryID as an argument and uses it as part of a query.
            def send():
                    date_time_obj = datetime.strptime(cal.get_date(), '%d/%m/%y')
                

                    if date_time_obj < datetime.now():
                        messagebox.showinfo(message = "The date selected has passed!")
                        open20()

                    #Paramterized Sql, uses categoryID to locate contactEmailAddress

                    def getCategoryID(categoryName):
                        query1 = "SELECT CategoryID FROM Department WHERE name = ? "
                        cursor.execute(query1, (categoryName,))
                        queryResult3 = cursor.fetchall()
                        return queryResult3[0][0]

                    def retreive(categoryID):
                        query = "SELECT contactEmailAddress FROM Supplier WHERE CategoryID = ?"
                        cursor.execute(query, (categoryID,))
                        queryResult2 = cursor.fetchall()
          
                        return queryResult2
        
         
                    sender = "computersciencetest6@gmail.com"
        
                    
                    reciever = retreive(getCategoryID(dropDown1.get()))
                  

                    password = "vmvpienhhrgtmatq"

                    #Query results used within body of message.
                    body = f"""

                    Subject: Products needed!\n
                    Product: {dropDown2.get()}\n
                    Amount: {enterAmount.get()}\n
                    Date: {cal.get_date()}\n
                    Department : {dropDown1.get()}\n
                    

                    """
                    #Server connection with gmail made.
                    #Allows body of messages to be sent to supplier emails. 
                    server = smtplib.SMTP('smtp.gmail.com',587)

                    server.starttls()

                    server.login(sender, password)

                    server.sendmail(sender, reciever, body)

                
                    print("Mail Sent")
                    messagebox.showinfo(message="Mail Sent")
                    server.close()
           


            
            enter = Button(window, text="Enter Details", command=lambda:send(),font = "Verdana 14 bold").pack(pady=5)




        


    window = Tk()
    window.configure(bg="light blue")
    obj = contactSupplier(window)

    window.geometry("300x300")
    window.mainloop()