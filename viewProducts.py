from tkinter import *

import sqlite3

from tkinter import messagebox
from tkinter import ttk

def open8():
    class viewProducts:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            self.title = Label(window, text="View Products",font = "Verdana 32 bold").pack(pady=20)
            #Front End Established
            trv = ttk.Treeview(window, columns=(1,2,3,4,5,6), show = "headings")
            trv.pack()
            #Function used to vislauze details within table.
            def update(rows, tree):
                for i in rows:
                    tree.insert('', 'end', values=i)
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
            #Select SQL query used to select all details from Product table.
                cursor.execute("""SELECT Product.ProductID, ProductName, Product.CategoryID, Amount, DateOfExpiration, price FROM Product 
                INNER JOIN Department ON Product.CategoryID = Department.CategoryID""")
                queryResult = cursor.fetchall()
                update(queryResult, trv)
                #Selects the average amount, and the mode category in product table. The data is grouped and ordered accordingly. 
                query1 = """SELECT AVG(Amount), (SELECT COUNT(CategoryID) FROM Product 
                GROUP BY CategoryID ORDER BY COUNT(CategoryID) DESC) FROM Product"""
                cursor.execute(query1)
                queryResult1 = cursor.fetchall()

                query2 = """SELECT Amount, COUNT(Amount) FROM Product GROUP BY Amount ORDER BY COUNT(Amount) DESC"""
                queryResult2 = cursor.fetchall()
                
                #Selects the amoumt, and evaluates the value against specific conditions. 
                query3 = """SELECT Amount, CASE WHEN Amount > 10 AND Amount < 50 
                THEN "Small Amount" WHEN Amount > 50 AND Amount < 90 THEN "Medium amount" WHEN Amount > 90 AND Amount < 100 THEN "Large amount" ELSE "INVALID" END AS AmountText FROM Product """
                cursor.execute(query3)
                queryResult3 = cursor.fetchall()

                trv1 = ttk.Treeview(window, columns=(1,2), show = "headings")
                trv1.pack()
                #Function used to vislauze details within table.
                
                trv1.heading(1, text="Quantity")
                trv1.heading(2, text="Quantity Text")
                trv1.pack()
                update(queryResult3, trv1)

                trv2 = ttk.Treeview(window, columns=(1,2), show = "headings")
                trv2.pack()

                trv2.heading(1, text="Average amount")
                trv2.heading(2, text="Mode CategoryID")
                trv2.pack()
                update(queryResult1, trv2)
            except:
                messagebox.showinfo(message="Not enough of information")





          



    window = Tk()
    obj = viewProducts(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()