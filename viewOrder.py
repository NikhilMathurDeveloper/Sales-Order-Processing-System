from tkinter import *

import sqlite3

from tkinter import messagebox

from tkinter import filedialog
from tkinter import ttk



def open24():
    class viewOrder:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            def update(rows, tree):
                for i in rows:
                    tree.insert('', 'end', values=i)
            #Establishes front end requirements
            self.title = Label(window, text="View Order Details", font = "Verdana 32 bold").pack(pady=20)
            trv = ttk.Treeview(window, columns=(1,2,3,4,5), show = "headings")
            trv.pack()
            #Function used to vislauze details within table.
           
            trv.heading(1, text="OrderID")
            trv.heading(2, text="ClientID")
            trv.heading(3, text="ProductID")
            trv.heading(4, text="DateOfRequirement")
            trv.heading(5, text="Quantity")
            trv.pack()
            try:
                with sqlite3.connect("SalesOrderProcessing.db") as db:
                    cursor=db.cursor()
                #Selects everything from Order table
                cursor.execute("SELECT * FROM Order1")
                queryResult = cursor.fetchall()
                #Update Function called to insert data into visualization.
                update(queryResult, trv)
                #Aggregate SQL functions which calculates average quantity, the most frequent Clients, Most Frequent Products
                try:
                    cursor.execute("SELECT AVG(Quantity), (SELECT COUNT(ClientID) FROM Order1 GROUP BY ClientID ORDER BY COUNT(ClientID) DESC), (SELECT COUNT(ProductID) FROM Order1 GROUP BY ProductID ORDER BY COUNT(ProductID) DESC) FROM Order1")
                    queryResult2 = cursor.fetchall()
                except:
                    messagebox.showinfo(message="There is not enough of info ")


                trv1 = ttk.Treeview(window, columns=(1,2,3), show = "headings")
                trv1.pack()
                #Function used to vislauze details within table.
                
                trv1.heading(1, text="Average Quantity")
                trv1.heading(2, text="Most Frequent Client")
                trv1.heading(3, text="Most Frequent Product")
                trv1.pack()
                update(queryResult2, trv1)

                #Selects orderID, ClientID, and selects the neccessary name through a sub query. 
                #Left join identifies which Clients have established an order.
                try:
                    cursor.execute("SELECT Order1.OrderID, Client.ClientID, (SELECT name FROM Client WHERE ClientID = Order1.ClientID) FROM Client LEFT JOIN Order1 ON Order1.ClientID = Client.ClientID ORDER BY Order1.OrderID ASC")
                    queryResultResult3 = cursor.fetchall()
                except:
                    messagebox.showinfo(message="There is not enough of info")


                trv2 = ttk.Treeview(window, columns=(1,2,3), show = "headings")
                trv2.pack()

                trv2.heading(1, text="OrderID")
                trv2.heading(2, text="ClientID")
                trv2.heading(3, text="Client Name")
                trv2.pack()
                update(queryResultResult3, trv2)
            except:
                messagebox.showinfo(message="Not enough of info")

            



            
   




    window = Tk()
    obj = viewOrder(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()