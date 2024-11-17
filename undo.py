from tkinter import *

import sqlite3

from tkinter import messagebox

from tkinter import filedialog
from tkinter import ttk



def open27():
    class undoOrder:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            labelTitle = Label(window, text="Undo Orders", font = "Verdana 32 bold").pack(pady=5)

            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()
            cursor.execute("SELECT OrderID FROM Order1 ORDER BY OrderID DESC LIMIT 5")
            queryResult2 = cursor.fetchall()
            print(queryResult2)



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
                    poppedItem = self.stack.pop()
                    return poppedItem
                    
                def printList(self):
                    for i in range(self.top, -1, -1):
                        if i == self.top:
                            print(self.stack[i])
                        else:
                            print(self.stack[i])

                #Creation of stack
            stack1 = stack()


          

            resultsFromQuery = []
            for j in queryResult2:
                resultsFromQuery.append(j[0])
            resultsFromQuery.sort()
            print(resultsFromQuery)
    


                
            #Pushes values onto stack, data structure
            stack1.push(resultsFromQuery[0])
            stack1.push(resultsFromQuery[1])
            stack1.push(resultsFromQuery[2])
            stack1.push(resultsFromQuery[3])
            stack1.push(resultsFromQuery[4])

            stack1.printList()

            def undo():
                messagebox.showinfo(message="Most recent order has been removed")
                query = """DELETE FROM Order1 WHERE OrderID = ?"""
                x = int(stack1.pop1())
                cursor.execute(query,(x,))
                db.commit()
                print("___-______")
                stack1.printList()



            button = Button(window, text="Undo", font = "Verdana 16 bold", command=undo).pack(pady=5)

            



            
   




    window = Tk()
    obj = undoOrder(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()