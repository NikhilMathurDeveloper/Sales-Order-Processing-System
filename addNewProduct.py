
from inspect import Traceback
from tkinter import *



from tkinter import messagebox
from types import TracebackType
from tkcalendar import *

import sqlite3
from datetime import datetime, timedelta


def open10():
    class addNewProducts:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            #Establish front End
            self.title = Label(window, text="Add new Products", font = "Verdana 32 bold").pack(pady=20)
            #Connect to database
            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()
            def insertIntoFormat(list1, result):
                for i in result:
                    list1.append(i[0])
                return list1
                
            
          
            queryResultStorage = []
            #SQL statement used for identifying name in department
            cursor.execute("SELECT name FROM Department")
            queryResult = cursor.fetchall()

            insertIntoFormat(queryResultStorage, queryResult)


        
            #List used to supply front end details to drop down
            dropDown1 = StringVar(window)
            dropDown1.set(queryResultStorage[0])
            drop1 = OptionMenu(window, dropDown1, *queryResultStorage)
            drop1.pack(pady=20)
            drop1.configure(width=20)
            


            #Establishes front end
            self.newProductName = StringVar(window)
            self.newAmount = IntVar(window)

            self.productName = Label(window, text="Enter product Name", font = "Verdana 14 bold").pack(pady=10)
            self.productEnter = Entry(window, textvariable=self.newProductName)

            self.productEnter.pack(pady=10)
            self.amount = Label(window, text="Enter Amount KG", font = "Verdana 14 bold").pack(pady=10)

            self.enterAmount = Entry(window, textvariable=self.newAmount)
            self.enterAmount.pack(pady=20)

            self.amount = Label(window, text="Select Date Of Expiration ", font = "Verdana 14 bold").pack(pady=10)
            cal = Calendar(window, selectmode='day', date_pattern ='d/m/yy', background="blue")
            cal.pack(pady=10)

            self.date = cal.get_date()
        

            self.priceTitle = Label(window,text="Enter price per Kg", font = "Verdana 14 bold").pack(pady=10)
            self.priceInitalize = IntVar(window)
            self.price = Entry(window, textvariable=self.priceInitalize)
            self.price.pack(pady=10)
    

                #Function used to add products. Takes ProductName, Amout, DateOfExpiration, price and name as arguments.
            def add_product(productName, Amount, DateOfExpiration, Price, name):

                print(productName)
                print(Amount)
                
                #Takes date and makes into more understandable format. This is done through date time module, strp function.
                #Checks condition, whether the date selected by the user has passed or not. 
                #Checks if the amount entered by the user is > 100.
                #Performs paramatized SQL query, where an appropriate data item is identified. 
                #Inserts into product table. 

                
                date_time_obj = datetime.strptime(DateOfExpiration, '%d/%m/%y')
                print(date_time_obj)

                if date_time_obj < datetime.now():
                    messagebox.showinfo(message = "The date selected has passed!")
                    open10()
                
                if int(Amount) > 100:
                    messagebox.showinfo(message = "100 is the Minimum")
                    open10()
                print(Amount)
                
                
                with sqlite3.connect("SalesOrderProcessing.db") as db:
                    cursor=db.cursor()

                
                
                            
                #Parameterized SQL statement taking user input
                query = "SELECT CategoryID FROM Department WHERE name = ?"
                cursor.execute(query, (name,))
                
                queryResult1 = cursor.fetchall() 
            
                
          



                #Paramterized SQL used to insert values into product table. 
                cursor.execute("INSERT INTO Product(ProductName, CategoryID, Amount, DateOfExpiration, price) VALUES (?,?,?,?,?)", (productName, int(queryResult1[0][0]), Amount, DateOfExpiration, Price))
                db.commit()
                messagebox.showinfo(message="Details have been added")
             
          
    
            

            
            




            

            def execute():
                try:
                    add_product(self.newProductName.get(), self.newAmount.get(), cal.get_date(), self.newAmount.get()*self.priceInitalize.get(), dropDown1.get())
                except:
                    messagebox.showinfo(message="An error occured. The data inptued is contextually incorrect")
           
    
            buttonAdd = Button(window, text="Enter Details",command=lambda:execute(), font = "Verdana 14 bold").pack(pady=20)#cal.get_date(), self.newProductName.get(), valie1. newVal, cal.get_date(), newVal2
        

          

           
           



      



    window = Tk()
    obj = addNewProducts(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()