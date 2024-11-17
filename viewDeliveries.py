from tkinter import *

import sqlite3

from tkinter import messagebox

from addClient import open3
from tkinter import ttk

from editClient import open4
def open17():
    class viewClients:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            #Establishes front end
            self.title = Label(window, text="Deliveries", font = "Verdana 32 bold").pack(pady=20)




            trv = ttk.Treeview(window, columns=(1,2), show = "headings")
            trv.pack()
            #Functions creates a visual platform
            def update(rows, tree):
                for i in rows:
                    tree.insert('', 'end', values=i)
            trv.heading(1, text="DeliveryID")
            trv.heading(2, text="OrderID")
            trv.pack()

            #Connects to database
            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()
            #SQL query selcts everything from client table
            try:
                cursor.execute("SELECT * FROM Delivery")
                details = cursor.fetchall()
            except:
                messagebox.showinfo(message="Not enough of info")
            #Argument supplied to function in order to supply details
            update(details, trv)

            trv1 = ttk.Treeview(window, columns=(1,2), show = "headings")
            trv1.pack()
            # Used to identify which orders have an establoshed delivery, and which do not have an assigned delivery.
            try:
                cursor.execute("SELECT Order1.OrderID, Delivery.DeliveryID FROM Order1 LEFT JOIN Delivery ON Delivery.OrderID = Order1.OrderID ORDER BY Order1.OrderID ASC")
                results = cursor.fetchall()
            except:
                messagebox.showinfo(message="Not enough of info")

            #Functions creates a visual platform
           
            trv1.heading(1, text="DeliveryID")
            trv1.heading(2, text="OrderID")
            trv1.pack()
            update(results, trv1)

         




    window = Tk()
    obj = viewClients(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()