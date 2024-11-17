

from fileinput import filename
from tkinter import *

import sqlite3

from tkinter import messagebox

import datetime 

import pickle


from location import open16

from datetime import *
from sendDelivery import open19
from tkinter import ttk
from viewDeliveries import open17
from timeForDelivery import open25



def open14():
    class delivery:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            #Establishes Front End
            self.title = Label(window, text="Delivery", font = "Verdana 24 bold")
            self.title.place(x=680, y=200)

            def insertIntoFormat(list1, result):
                for i in result:
                    list1.append(i[0])
                return list1

            trv = ttk.Treeview(window, columns=(1,2,3,4,5), show = "headings")
            trv.pack()
            #Functions creates a visual platform
            def update(rows, tree):
                for i in rows:
                    tree.insert('', 'end', values=i)
            trv.heading(1, text="OrderID")
            trv.heading(2, text="ClientID")
            trv.heading(3, text="Name")
            trv.heading(4, text="Date Of Requirement")
            trv.heading(5, text="Quantity")
            trv.pack()
            
            
            #Connects to database
            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()
            
            
            
            #SQL query selcts everything from client table
            cursor.execute("SELECT * FROM Order1")
            details = cursor.fetchall()
            #Argument supplied to function in order to supply details
            update(details, trv)

            

          

            #SQL query identifies OrderID from Order table
            
            cursor.execute("""SELECT OrderID FROM Order1 """)
            queryResult = cursor.fetchall()
            queryResultStorage = []
            insertIntoFormat(queryResultStorage, queryResult)
            
            

            #Function for opening next page
            def func():
                open16()
            buttonLocation = Button(window, text="Find Location", command=func, font = "Verdana 14 bold").place(x=600, y=240)
            def send():
                open19()
            def openTimeDelivery():
                open25()
            buttonSend = Button(window, text="Send Deliveries", command=send, font = "Verdana 14 bold").place(x=740, y=240)
            buttonRequestFaster = Button(window, text="Time", font = "Verdana 14 bold", command=openTimeDelivery).place(x=900, y = 240)
            def openDeliveries():
                open17()

            buttonViewDeliveries = Button(window, text="View Deliveries", font = "Verdana 14 bold", command=openDeliveries).place(x=450, y=240)
            

            value1 = IntVar(window)
            value2 = IntVar(window)
            value3 = IntVar(window)
            value4 = IntVar(window)
            value5 = IntVar(window)
            

            entry1 = Entry(window, textvariable=value1).place(x=550, y = 360)
            entry2 = Entry(window, textvariable=value2).place(x=550, y = 420)

            entry3 = Entry(window, textvariable=value3).place(x=550, y = 540)
            entry4 = Entry(window, textvariable=value4).place(x=550, y = 600)
            entry5 = Entry(window, textvariable=value5).place(x=550, y = 660)



            '''
            dropDown = StringVar(window)
            dropDown.set(queryResultStorage[0])
            drop1 = OptionMenu(window, dropDown, *queryResultStorage)
            drop1.place(x=550, y = 360)
            drop1.configure(width=5)

            dropDown1 = StringVar(window)
            dropDown1.set(queryResultStorage[0])
            drop2 = OptionMenu(window, dropDown1, *queryResultStorage)
            drop2.place(x=550, y=420)
            drop2.configure(width=5)

            dropDown2 = StringVar(window)
            dropDown2.set(queryResultStorage[0])
            drop3 = OptionMenu(window, dropDown2, *queryResultStorage)
            drop3.place(x=550, y = 540)
            drop3.configure(width=5)

            dropDown3 = StringVar(window)
            dropDown3.set(queryResultStorage[0])
            drop4 = OptionMenu(window, dropDown3, *queryResultStorage)
            drop4.place(x=550, y = 600)
            drop4.configure(width=5)

            dropDown4 = StringVar(window)
            dropDown4.set(queryResultStorage[0])
            drop5 = OptionMenu(window, dropDown4, *queryResultStorage)
            drop5.place(x=550, y = 660)
            drop5.configure(width=5)

            '''

            self.label = Label(window, text="Select OrderID", font = "Verdana 14 bold").place(x=550, y=300)
            #Creation of node
            class node:
                #Constructor initalizes attributes within.
                def __init__(self, data, priority):
                    self.data = data
                    self.priority = priority
                    self.next = None 
            #PriorityLinkedListClass
            class priorityClass:
                #Constructure initalizes head attribute
                def __init__(self):
                    self.head = None
                #Returns true if empty
                def empty(self):
                    return True if self.head ==None else False
                #Locates a data item within the linked list. Checks if Empty, if not checks the data and its accociated priority and inserts accoridingly.
                def insert1(self, data, priority):
                    
                    if self.empty() == True:
                        self.head = node(data, priority)
                    else:
                        if self.head.priority > priority:
                            new_node = node(data, priority)
                            new_node.next = self.head
                            self.head = new_node
                
                        else:
                            current = self.head
                            while current.next:
                                if priority <= current.next.priority:
                                    break
                                current = current.next
                            new_node = node(data, priority)
                            new_node.next = current.next
                            current.next = new_node
                def remove(self, data):

                    current = self.head
                    

                    if current.data == data:
                        self.head = current.next
                    else:
                        while current.next.data != data:
                            current = current.next
                        current.next = current.next.next
                    
                        
                        


            
                        

                #Displays the linked list through iteration. Produces an automatic file which assings a truck number accordingly.
                def printLinked(self):
                    arr = []
                    file_name = str(self.head.data) + ".txt"
                    f = open(file_name, "w")
                    if self.empty():
                        print("not valid")
                    else:
                        current = self.head
                        while current:
                            f.write(", "+str(current.data) + ", ")
                            if current.priority == 1:
                                f.write(", Delivery ID" + str(current.data) + "goes in Truck 1")
                            if current.priority == 2:
                                f.write(", Delivery ID" + str(current.data) + "goes in Truck 2")
                            if current.priority == 3:
                                f.write(",  Delivery ID" + str(current.data) + "goes in Truck 3")
                            arr.append(current.data)

                            
                          
                           
                            




                          
                            current = current.next
                    return arr
                    
         
            
            def get_delivery():
            
                with sqlite3.connect("SalesOrderProcessing.db") as db:
                    cursor=db.cursor()


       


               
                c = priorityClass()
               
                #Function for getting suggested priority
                def get_suggested_priority():
                
                    #list used to store date
                    list_of_dates = []
                    #Python function sotring functionality of query. Takes orderID as argument.
                    def getDateOfRequirement(OrderID):
                        #Paramterized SQL statement
                        try:
                            sql1 = "SELECT DateOfRequirement FROM Order1 WHERE OrderID = ?"
                            cursor.execute(sql1, (OrderID, ))
                            queryResult1 = cursor.fetchall()
                            list_of_dates.append(queryResult1[0][0])
                        except:
                            messagebox.showinfo(message="Information is not existent.")
                    #Information supplied to function.
                    getDateOfRequirement(value1.get())
                    getDateOfRequirement(value2.get())
                    getDateOfRequirement(value3.get())
                    getDateOfRequirement(value4.get())
                    getDateOfRequirement(value5.get())
                    print(list_of_dates)
           


                    #Current Date
                    current = datetime.now()
                    #List used to store the number of days in between the current day and the elemnts in list_of_dates list.
                    days = []
                    for j in list_of_dates:
                        #Uses date time function to retrieve desired format.
                        date_time_obj = datetime.strptime(j, '%y/%m/%d')
                        number_of_days = date_time_obj - current 
                        #Append the difference
                        days.append(number_of_days.days)
                    print(days)

                    #Dynamic List creation
                    file_name = "priority" +str(value1.get()) + ".txt"
                    f = open(file_name,"w")
            
                    x=0
                    #Checks the number of days, and accordingly inserts into text file
                    for j in days: 
                        if j >= 1 and j <= 5:
                            x+=1
        
                            f.write("Priority 1 for orders" +  str(days.index(j)+1) + ",")

                        if j >= 5 and j <= 10:
                            days.index(j)
                            x+=1
                         
                            f.write("Priority 2 for orders" +  str(days.index(j)+1) + ",")
                        if j >= 10 and j <=15:
                            x+=1
                
                            f.write("Priority 2 for orders" +  str(days.index(j)+1) + ",")


                        if j >= 15:
                            pass
                            f.write("Priority 3 for orders" +  str(days.index(j)+1) + ",")
                    #Close text file for good practices
                    #f.close()


                    messagebox.showinfo(message = "Completed")
                    


                
                button_priority = Button(window, text="Get Suggested Priority", command=get_suggested_priority, font = "Verdana 14 bold")
                button_priority.place(x=700, y = 800)


                
            
                
     
              
          

                
                        

                 
                    
                """
                #Finds day, month, year of select date from table. 
                date_time_obj = datetime.strptime(queryResultStorage1[0], '%y/%m/%d') 
                arrDate = [] 
                    
                arrDate.append(date_time_obj.day)
            
                arrDate.append(date_time_obj.month)
      
                arrDate.append(date_time_obj.year)
                    
 
                today = date.today()
                #Checks whether on same month, and year.
                if int(arrDate[1]) == today.month and int(arrDate[2]) == today.year:
                    remaining_number_of_days =  int(arrDate[0])- today.day 
                    #print(remaining_number_of_days)
                    priority = 0
                if remaining_number_of_days > 10:
                        priority = 3
                if remaining_number_of_days < 10 and remaining_number_of_days > 5:
                        priority = 2
                if remaining_number_of_days < 5:
                        priority = 1
                """
                priority_list = [1,2,3]
                dropDown5 = StringVar(window)
                dropDown5.set(priority_list[0])
                drop6 = OptionMenu(window, dropDown5, *priority_list)
                drop6.place(x=900, y = 360)
                drop6.configure(width=5)


                dropDown6 = StringVar(window)
                dropDown6.set(priority_list[0])
                drop7 = OptionMenu(window, dropDown6, *priority_list)
                drop7.place(x=900, y = 420)
                drop7.configure(width=5)

                dropDown7 = StringVar(window)
                dropDown7.set(priority_list[0])
                drop8 = OptionMenu(window, dropDown7, *priority_list)
                drop8.place(x=900, y=540)
                drop8.configure(width=5)


                dropDown8 = StringVar(window)
                dropDown8.set(priority_list[0])
                drop9 = OptionMenu(window, dropDown8, *priority_list)
                drop9.place(x=900, y = 600 )
                drop9.configure(width=5)

                dropDown9 = StringVar(window)
                dropDown9.set(priority_list[0])
                drop10 = OptionMenu(window, dropDown9, *priority_list)
                drop10.place(x=900, y =660 )
                drop10.configure(width=5)
                
                


               
                label = Label(window, text="Enter Priority", font = "Verdana 14 bold").place(x=900, y = 300)
             

                
                def enter():

                    try:
                        with sqlite3.connect("SalesOrderProcessing.db") as db:
                            cursor=db.cursor()
                        try:
                            query1 = "SELECT OrderID FROM Order1"
                            cursor.execute("SELECT OrderID FROM Order1")
                            queryResult = cursor.fetchall()
                            queryResultStorage2 = []
                            for items in queryResult:
                                queryResultStorage2.append(items[0])
                        except:
                            messagebox.showinfo(message="Not enoigh of information")
                        def selection(OrderID):
                            #Selects the ClientID, the client Name, ProductID, ProductName. This query is paramterized.
                            #These details are used within the program for different reasons.
                            try:
                                query = """SELECT Order1.ClientID , (SELECT name FROM Client WHERE ClientID = Order1.ClientID), 
                                Order1.ProductID, (SELECT ProductName FROM Product WHERE ProductID = Order1.ProductID), 
                                (SELECT price FROM Product WHERE ProductID = Order1.ProductID), 
                                (SELECT Amount FROM Product WHERE ProductID = Order1.ProductID) 
                                FROM Order1 WHERE OrderID = ?"""
                            except:
                                messagebox.showinfo(message="There is not enough of information")

        
                            cursor.execute(query, (OrderID, ))
                            resultOfQuery = cursor.fetchall()
                            return resultOfQuery
                        x = 1
                        #Binary search
                        #This function checks whether the order has already been established 
                        def checkFrqueny(OrderID):
                           
                            #Sort function used to sort list.
                            queryResultStorage2.sort()
                            position = -1
                            #A binary saerch is used to locate the items 
                
                            def binarySearch(list1, target):
                                l = 0
                                u = len(list1)-1
                                x = 0
                                while l <= u:
                                    mid = (l + u)//2

                             
                                    if list1[mid] == target:
                                        
                                        globals()['position'] = mid
                                        print("Found")
                                        x = 1
                                        return True 
                                    else:
                                        if list1[mid] < target:
                                            l = mid+1
                                        else:
                                            u = mid-1
                         
                                print("not found")
                                return False
                            #Flag value
                            x = 0

                            #Conditions for binary search. 
                            if binarySearch(queryResultStorage2, OrderID):
                                x+=1
                            else:
                                pass
                            # If all inputs were found then the process is valid. 
                            #Else some of the products do not exist. 
                            if x == 1:
                                return True
                            else:
                                return False

                        #Conditions to check
                        if checkFrqueny(value1.get()) == False or checkFrqueny(value2.get()) == False or checkFrqueny(value3.get()) == False or checkFrqueny(value4.get()) == False or checkFrqueny(value5.get()) == False:
                            messagebox.showinfo(message = "Order is not existent")
                            print("Nope")
                        else:
                            #Average function returning average
                            '''
                            def average1(a,b,c,d,e):
                                avg = a+b+c+d+e/5
                                return avg
                                
                            #Caclulating average price and quantity with usage of function and SQL queries. 
                            averagePrice = average1(selection(value1.get())[0][4], selection(value2.get())[0][4], selection(value3.get())[0][4], selection(value4.get())[0][4], selection(value5.get())[0][4])
                            averageQuantity = average1(selection(value1.get())[0][5], selection(value2.get())[0][5], selection(value3.get())[0][5], selection(value4.get())[0][5], selection(value5.get())[0][5])
                            #Dynamic file creation
                            fileName = "Report"+str(value1.get())+".txt"
                            f = open(fileName, "w")
                            body = f"""
                

                            Reporting Stats:
                            Average Price: {averagePrice}\n
                            Average Amount: {averageQuantity}\n
                            Date: {date.today()}\n
                            
                            """
                            #File operations
                            f.write(body)
                            f.close()
                            '''

                            #Priority queue implementation.
                            c.insert1(value1.get(), int(dropDown5.get()))
                            c.insert1(value2.get(), int(dropDown6.get()))

                            c.insert1(value3.get(), int(dropDown7.get()))
                            c.insert1(value4.get(), int(dropDown8.get()))
                            c.insert1(value5.get(), int(dropDown9.get()))
                            c.printLinked()

                            #Asks user if they want to remove an order
                            titleRepresentation = Label(window, text = "If you would like to remove an order: ", font = "Verdana 10 bold").place(x=1000, y=800)
                            #Variable used to store user input
                            textvaribale1 = IntVar(window)
                            orderEntry = Entry(window, textvariable=textvaribale1).place(x=1300, y = 800)
                            #Function to call linked list remove function. 
                            def remove1():
                                try:
                                    messagebox.showinfo(message="Order removed")
                                    #Calls linked list remove function
                                    c.remove(textvaribale1.get())
                                    #Prints linkedlist, and stores in text file. 

                                    
                                    

                       
                                    label = Label(window, text=c.printLinked(),font= "Verdana 14 bold").place(x=1000, y = 700)
                                except:
                                    messagebox.showinfo(message="Order does not exist")
                            

                            #Button inheriting features. 

                            button1 = Button(window, text= "Remove", command=remove1, font = "Verdana 14 bold").place(x=1200, y=830)


                            messagebox.showinfo(message = "Completed")

                            #Function for inserting into table
                            #def insertIntoTable(OrderID):
                                #cursor.execute("INSERT INTO Delivery(OrderID) VALUES (?)", (OrderID,))
                                #db.commit()

                            #Function Call   
                            #insertIntoTable(value1.get())
                            #insertIntoTable(value2.get())
                            ##insertIntoTable(value3.get())
                            #insertIntoTable(value4.get())
                            #insertIntoTable(value5.get())
                           

                    except TclError:
                        messagebox.showinfo(message = "Please Enter Numbers")
                       
                    
                

                button = Button(window, text="Establish Delivery", command=enter, font = "Verdana 14 bold").place(x=700, y=830)
            
               


               
                

                    
                
            
              
                
                
                    
                        
                            
                #label = Label(window, text="The number of days remaining till order needs to be fufilled are" + str(remaining_number_of_days) + "We are providing a priority of" + str(priority))
                #label.pack(pady=20)
                #label2 = Label(window, text="Do you wish to change the priority of the order").pack(pady=20)
                #arr = []
                    #Allows to enter new priority 
                       

                     
          
                    #Allows to use current priority 
     
          
                #Enters into database details of Delivery 
          
                
                
            button = Button(window, text = "Enter", command=get_delivery, font = "Verdana 14 bold").place(x=700, y=800)





    window = Tk()
    
    obj = delivery(window)

    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()