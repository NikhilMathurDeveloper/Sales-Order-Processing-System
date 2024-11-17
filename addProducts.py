from tkinter import *

import sqlite3

from tkinter import messagebox
from tkinter import ttk

def open9():
    class editProducts:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            #Establishes front end
            self.title = Label(window, text="Update Product Stock", font = "Verdana 32 bold").pack()
            #Function to remove data item fron table and visalization 
            def update(rows, tree):
                for i in rows:
                    tree.insert('', 'end', values=i)
            def insertIntoFormat(list1, result):
                for i in result:
                    list1.append(i[0])
                return list1
            try:
                def remove():
                    #Connects to database
                    with sqlite3.connect("SalesOrderProcessing.db") as db:
                        cursor=db.cursor()
                    
                    #Deletes fron visualization    
                    x = trv.selection()[0]

                    print(trv.item(x)['values'])
                    data = trv.item(x)['values'][0]

                    #Parameterized SQL statement, which takes user input
                    query1 = "DELETE FROM Product WHERE productID = ?"
                    #Execute function executes statement with user input.
                    cursor.execute(query1, (data,))
                    db.commit()
        

                    trv.delete(x)
                    messagebox.showinfo(message="Details have been removed")
            except:
                messagebox.showinfo(message="An error occured")
            
            #Establishes visualization
            trv = ttk.Treeview(window, columns=(1,2,3,4,5,6), show = "headings")
            trv.pack()
            
            trv.heading(1, text="ProductID")
            trv.heading(2, text="Product Name")
            trv.heading(3, text="CategoryID")
            trv.heading(4, text="Amount")
            trv.heading(5, text="Date Of Expiration")
            trv.heading(6, text="Price")
            trv.pack()
            #Connects to database
            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()

            try:
                #Select SQL statement, identifying all information in product table.
                cursor.execute("SELECT * FROM Product")
                queryResult = cursor.fetchall()
                #Establushes visualization with neccessary argument. 
                update(queryResult, trv)
           

                self.delete = Button(window, text="Delete", command=remove, font = "Verdana 14 bold").pack()
                queryResultStorage = []
                #Select SQL satement, identifies names in department table. 
                cursor.execute("SELECT name FROM Department")
                queryResult1 = cursor.fetchall()
                insertIntoFormat(queryResultStorage, queryResult1)

                #The list is supplied to create a drop down menu, presenting all names.
                dropDown = StringVar(window)
                dropDown.set(queryResultStorage[0])
                drop1 = OptionMenu(window, dropDown, *queryResultStorage)
                drop1.pack()
                drop1.configure(width=20)
            except:
                messagebox.showinfo(message="Not enough of info")

            
            #Function which identifies information
            def select(name):
                with sqlite3.connect("SalesOrderProcessing.db") as db:
                    cursor=db.cursor()
                
                try:
                    #Select categoryID
                    #Select ProductID from product WHERE NAME =
                    #Select productID from product
                    #SQL parameterized QUERY used to select categoryID from DEPARTMENT according to user input
                    '''
                    query3 = """SELECT Department.CategoryID, (SELECT ProductName From Product WHERE CategoryID = Department.CategoryID) 
                    FROM Department WHERE name = ?"""
                    '''

                    query3 = """SELECT Product.ProductName FROM Department INNER JOIN Product ON Department.CategoryID =
                    Product.CategoryID WHERE Department.name = ?"""
                    cursor.execute(query3, (name,))#dropDown.get()
                    result = cursor.fetchall()


                    resultStore = []
                    resultStore.append(result[0][0])
                
                
                

                    #Results stored in productList list, and later used for drop down menu.
            

                    dropDown2 = StringVar(window)
                    dropDown2.set(result[0][0])
                    drop2 = OptionMenu(window, dropDown2, *resultStore)
                    drop2.pack()
                    drop2.configure(width=20)

                    #SQL parameterized QUERY used to select productID from product according to user input
                    query4 = "SELECT productID FROM Product WHERE productName = ?"
                    cursor.execute(query4, (dropDown2.get(), ))
                    

            
                    queryResult3 = cursor.fetchall()


                   
                    info = Label(window, text="New Amount", font = "Verdana 14 bold").pack()
                    amountEnter = Entry(window)
                    amountEnter.pack()
                    #Updates table accoring to user input
                except:
                    messagebox.showinfo(message="Error occured")
                def update(amount, productID):
                    try:
                        if int(amountEnter.get()) > 100:
                            messagebox.showinfo(message="The limit is 100")
                            open9()
                        with sqlite3.connect("SalesOrderProcessing.db") as db:
                            cursor=db.cursor()
                        #Parameterized SQL statement, taking user input.
                        query5 = "UPDATE Product SET Amount = ? WHERE ProductID = ?"

                        cursor.execute(query5, (amount, productID, ))

                        db.commit()
                        messagebox.showinfo(message="Details have been updated")
                    except:
                        messagebox.showinfo(message="An error occured")
                    



                
                def execute():
                    try:
                        update(int(amountEnter.get()), queryResult3[0][0])
                    except:
                        messagebox.showinfo(message="The inputs are of invalid context")

                buttonEnter = Button(window, text="Enter", command=lambda:execute(), font = "Verdana 14 bold").pack()

    
        

                
                
            self.select_button = Button(window, text="Search Department", command=lambda:select(dropDown.get()), font = "Verdana 14 bold").pack()

           

   
            

          



    window = Tk()
    obj = editProducts(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()