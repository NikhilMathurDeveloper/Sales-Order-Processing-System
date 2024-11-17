from tkinter import *

import sqlite3

from tkinter import messagebox

from tkinter import filedialog

from datetime import *

def open25():
    class time:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            #Establishes front end requirements
            self.title = Label(window, text="Identify Amount of time remaining", font = "Verdana 32 bold").pack(pady=20)
   

            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()
            

            def insertIntoFormat(list1, result):
                for i in result:
                    list1.append(i[0])
                return list1

            query = """SELECT Order1.OrderID FROM Order1"""
            queryResultStorage = []
            cursor.execute(query)
            queryResult = cursor.fetchall()

            insertIntoFormat(queryResultStorage, queryResult)


            dropDown = StringVar(window)
            dropDown.set(queryResultStorage[0])
            drop = OptionMenu(window, dropDown, *queryResultStorage)
            drop.pack()
            drop.configure(width=5)

            def calcTime(orderID):
                query = "SELECT DateOfRequirement FROM Order1 WHERE OrderID = ?"
                cursor.execute(query, (orderID, ))
                queryResultStorage1 = []
                queryResult = cursor.fetchall()
                insertIntoFormat(queryResultStorage1,queryResult)

                current = datetime.now()
             
                date_time_obj = datetime.strptime(queryResultStorage1[0], '%y/%m/%d')
                number_of_days = date_time_obj - current 
                label1 = Label(window, text=str(number_of_days)).pack()
       
            
            button = Button(window,text="Calculate number of days until delivery", command=lambda:calcTime(dropDown.get())).pack()



                








            
   




    window = Tk()
    obj = time(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()