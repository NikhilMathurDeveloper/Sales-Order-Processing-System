from concurrent.futures import thread
from tkinter import *

from time import *
import threading

from tkinter import messagebox
import time

from tkcalendar import *
import pickle
import sqlite3
from datetime import datetime, timedelta
from viewOrder import open24
from undo import open27
import sys
import multiprocessing
from threading import Timer
import signal



def open11():
    class addProduct:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            def view():
                open24()
            def openUndo():
                open27()
          
            def insertIntoFormat(list1, result):
                for i in result:
                    list1.append(i[0])
                return list1
            try:
                #Establishes front End
                self.title = Label(window, text="Add new Order", font = "Verdana 32 bold").pack(pady=20)
                #Database connection 

                with sqlite3.connect("SalesOrderProcessing.db") as db:
                    cursor=db.cursor()
                #SQL query used to select clientID from Client table

                cursor.execute("SELECT clientID FROM Client")
                queryResult = cursor.fetchall()

                queryResultStorage = []

                insertIntoFormat(queryResultStorage, queryResult)

               
                buttonView = Button(window, text="View Orders", command=view, font = "Verdana 14 bold").pack(pady=5)
                buttonInfo = Button(window, text="Undo Orders", command=openUndo, font = "Verdana 14 bold").pack(pady=5)


                cursor.execute("SELECT Order1.OrderID, Product.ProductID FROM Order1 LEFT JOIN Product ON Product.ProductID = Order1.ProductID ORDER BY Order1.OrderID ASC")
                results1 = cursor.fetchall()


                #Unpacks query and stores in list
                label = Label(window, text="Select ClientID", font = "Verdana 14 bold").pack(pady=5)
                dropDown = StringVar(window)
                dropDown.set(queryResultStorage[0])
                drop1 = OptionMenu(window, dropDown, *queryResultStorage)
                drop1.pack(pady=20)
                drop1.configure(width=20)

                #SQL query statement used to select ProductID from product
                cursor.execute("SELECT productID FROM Product")
                queryResult2 = cursor.fetchall()

                queryResultStorage2 = []
                insertIntoFormat(queryResultStorage2, queryResult2)
            
                
                self.label2 = Label(window, text="Select ProductID", font = "Verdana 14 bold").pack(pady=5)

                dropDown2 = StringVar(window)
                dropDown2.set(queryResultStorage2[0])
                drop2 = OptionMenu(window, dropDown2, *queryResultStorage2)
                drop2.pack(pady=20)
                drop2.configure(width=20)
                
                


                self.label3 = Label(window, text="Select requirement date", font = "Verdana 14 bold").pack(pady=5)

                cal = Calendar(window, selectmode='day', date_pattern ='yy/m/d', background="blue")
                cal.pack(pady=10)

            

                self.label4 = Label(window, text="Select amount needed KG", font = "Verdana 14 bold").pack(pady=5)

                self.amount = StringVar(window)

                self.enterAmount = Entry(window, textvariable=self.amount).pack(pady=10)
                #Add function inserts into database
            except:
                messagebox.showinfo(message="Error occured")
            #Adds product.
            def add(productID, date, quantity):
        
                with sqlite3.connect("SalesOrderProcessing.db") as db:
                    cursor=db.cursor()

                #Selects ClientID, Product ID, uses INNER JOIN. 
                #Checks which order combinations have been established.ClientID and ProductID.
                # This is to ensure that the client will not establish the same order again.
                #However if this is intended this is allowed. 
                def locateCombo(pair):
                    cursor.execute("""SELECT Order1.ClientID, Order1.ProductID FROM Order1 
                    INNER JOIN Client ON Order1.ClientID = Client.ClientID""")
                    queryResult4 = cursor.fetchall()
                    #Iterates through query result, and identifies whether the client and product comibination match. 
                    #If yes, the employee has the ability to click not intended if the error is acknowledged by the employee.
                    #However, the employee is able to carry on if intended
                    for items in queryResult4:
                        if pair == items:
                            messagebox.showinfo(message = "This Order combination has already been established ClientID: " +str(dropDown.get() + "ProductID: " + str(dropDown2.get()) + "Please Select NOT INTENDED if wrongfully selected"))    
                            def back():
                                open11()
                            button2 = Button(window, text="Not Intended", command=back, font = "Verdana 14 bold").pack(pady=5)    
                pair = (int(dropDown.get()), int(dropDown2.get())) 

                locateCombo(pair)

   


                #Function created takes productID as argument, and identifies its corresponding amount.
                def productDetails(productID):
                 
                        #Paramterized SQL to find Amount
                        #Selects amount from product according to parameter passed to query.
                        sqlQuery = "SELECT Amount FROM Product WHERE ProductID = ?"
                        cursor.execute(sqlQuery, (productID, )) #dropDown2.get()[0]
                        queryResult3 = cursor.fetchall()
                        return queryResult3[0][0]
                    
                        #messagebox.showinfo(message="Product Not found")
                        #open11()
                
                #A new amount is calculated according to a calculation performed by subtracting query result from user input.
                new_amount = int(productDetails(productID)) - int(self.amount.get())
    
                #Values established for inserition into table. 
                value1 = dropDown.get()
                value2 = dropDown2.get()
                #Function takes new amount and productID as arguments, and are used to set new values in product table. 
                def updateProductTable(new_amount, productID):
                    #Paramterized Update statement
                    try:
                        sqlQuery2 = "UPDATE Product SET Amount = ? WHERE ProductID = ?"
                        #Executes statement 
                        cursor.execute(sqlQuery2, (new_amount, productID, ))
                        db.commit()
                    except:
                        messagebox.showinfo("The amount is invalid! 2")
                        open11()
                
                updateProductTable(new_amount, productID)
                #Identfies the number of days remaining taking a date as an argument.
                def identifyDays(date):
                    date_time_obj = datetime.strptime(date, '%y/%m/%d') #cal.get_date()
                    current = date_time_obj - datetime.now()
                    return current.days
                
                def identifyQuantity(quantity, productID):
                    query = "SELECT Amount FROM Product Where ProductID = ?"
                    cursor.execute(query, (productID, ))
                    queryResult = cursor.fetchall()
                    if int(quantity) > int(queryResult[0][0]):
                        messagebox.showinfo(message="The amount selected is invalid 1")
                        open11()
            
                identifyQuantity(quantity, productID)
              

                #Checks if the date has already passed. 
                if identifyDays(date) < 0:
                    messagebox.showinfo(message="The date selected has already passed")
                    open11()
                else:
                    pass

                #Identifies the last record in Order table. Used for stack data structure.
                cursor.execute("SELECT OrderID FROM Order1 ORDER BY OrderID DESC LIMIT 5")
                queryResult2 = cursor.fetchall()
               
                
          
                #Stack Data structure
                class stack():

                    def __init__(self):
                        self.stack = []
                        self.top = -1
                    
                    
                    def push(self, value):
                       
                        self.top +=1
                        self.stack.append(value)
                    
                    def pop1(self):
                        if self.top == -1:
                            print("Not valid")
                        self.top -=1
                        self.stack.pop()
                     
                    def printList(self):
                        for i in range(self.top, -1, -1):
                            if i == self.top:
                                print(self.stack[i])
                            else:
                                print(self.stack[i])

                #Creation of stack
                stack1 = stack()
                #Last value added to the order table pushed onto stacl.
                resultsFromQuery = []

                for j in queryResult2:
                    resultsFromQuery.append(j[0])
                resultsFromQuery.sort()
    


                
                #Pushes values onto stack, data structure
                stack1.push(resultsFromQuery[0])
                stack1.push(resultsFromQuery[1])
                stack1.push(resultsFromQuery[2])
                stack1.push(resultsFromQuery[3])

                stack1.printList()
                print("___-__")
       
                def confirm():
                    
                   
                    try:
                        
                       
                        def send(clientID, productID, DateOfRequirement, Quantity):
                            #Parametertized SQL statement
                            #Confirms order and inserts into table.
                            exit_even = threading.Event()
                      
                 
                           

                            productClient = str(productID) + str(clientID)
                            
                            stack1.push(productClient)
                            def countdown():
                                global clockSeconds
                                clockSeconds = 10
                                for second in range(10):
                        
                                    clockSeconds = clockSeconds - 1
                                    sleep(1)

                                    if exit_even.is_set():
                                        break
                           
                            
                                   
                                
                              
                           

                        
                            button = Button(window, text="Undo", command=lambda:undo,font = "Verdana 14 bold" ).pack()
                           
        
                            timer = threading.Thread(target=countdown)
                            
                            timer.start()

                           

                            x = 1
                            def undo():
                                x == 0
                                print("HELLO")
                                if clockSeconds != 0:
                                    stack1.pop1()
                                    def signal_handler(signum, frame):
                                        exit_even.set()
                                    messagebox.showinfo(message="Your order has been halted")
                            
                                    signal.signal(signal.SIGINT, signal_handler)
                                    timer.join()
                                if clockSeconds == 0:
                                    messagebox.showinfo(message="Cannot do")

                            while clockSeconds > 0:
                                window.update()
                            
                            
                            
                            
                    
                            
                            
                            
                                
                          
                             
                            if clockSeconds == 0 and x != 0:
                                stack1.pop1()
                                messagebox.showinfo(message="Your order has been added")
                                cursor.execute('INSERT INTO Order1(ClientID,ProductID,DateOfRequirement, Quantity) VALUES (?,?,?,?)', (clientID, productID, DateOfRequirement, Quantity))
                                db.commit()
                       
                            
                          
                            '''
                            def undo():
                                if clockSeconds != 0:

                                    stack1.pop1()
                                    messagebox.showinfo(message="Your Details have been halted")
                                else:
                                    messagebox.showinfo(message="The time has already been passed")
                                
                                
                            buttonUndo = Button(window, text="Undo", command=undo).pack()

                            '''
                            
                            
                           
                           
                   
                        buttonSend = Button(window, text="Send Order", command=lambda:send(value1, value2, cal.get_date(), int(self.amount.get())), font = "Verdana 14 bold").pack(pady=5)
                        
                    except:
                        messagebox.showinfo(message="An error occured")

       
                  
                   
                
                buttonConfirm = Button(window, text="Proceed", command=confirm, font = "Verdana 14 bold").pack(pady=5)

   
                  
          


            self.ButtonEnter = Button(window, text="Enter", command=lambda:add(dropDown2.get(), cal.get_date(), int(self.amount.get())), font = "Verdana 14 bold").pack(pady=10)
            




            
   




    window = Tk()
    obj = addProduct(window)
    window.configure(bg="light blue")
    window.geometry("300x300")
    window.mainloop()