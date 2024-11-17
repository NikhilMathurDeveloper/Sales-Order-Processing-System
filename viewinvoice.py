from tkinter import *

import sqlite3

from tkinter import messagebox

from tkinter import filedialog
from tkinter import ttk



def open25():
    class invoices:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            #Establishes front end requirements
            def update(rows, tree):
                for i in rows:
                    tree.insert('', 'end', values=i)
            self.title = Label(window, text="View Invoice Details", font = "Verdana 32 bold").pack(pady=20)
            trv = ttk.Treeview(window, columns=(1,2,3,4,5), show = "headings")
            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()
            trv.pack()
            #Function used to vislauze details within table.
        
            trv.heading(1, text="OrderID")
            trv.heading(2, text="InvoiceID")
            trv.heading(3, text="ProductID")
            trv.heading(4, text="ClientID")
            trv.heading(5, text="DateOfRequirement")
            try:
            #Select Query identifies OrderID, ProductID, ClientID, DateOfRequirement. Uses left join 
                cursor.execute("""SELECT Order1.OrderID, Invoice.InvoiceID, Order1.ProductID, Order1.ClientID, Order1.DateOfRequirement 
                FROM Order1 LEFT JOIN Invoice ON Invoice.OrderID = Order1.OrderID ORDER BY Order1.OrderID ASC""")
                queryResult = cursor.fetchall()
            except:
                messagebox.showinfo(message="An error occured")
           
            trv.pack()
            update(queryResult, trv)

            


    window = Tk()
    obj = invoices(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()