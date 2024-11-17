from re import A
from tkinter import *

import sqlite3

from tkinter import messagebox

from addClient import open3
from tkinter import ttk

from editClient import open4
def open5():
    class viewClients:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            #Establishes front end
            self.title = Label(window, text="Clients", font = "Verdana 32 bold").pack(pady=20)

            def update1(rows, tree):
                for i in rows:
                    tree.insert('', 'end', value=i)


            trv = ttk.Treeview(window, columns=(1,2,3,4,5), show = "headings")
            trv.pack()
            #Functions creates a visual platform
          
            trv.heading(1, text="ClientID")
            trv.heading(2, text="PostCode")
            trv.heading(3, text="Name")
            trv.heading(4, text="Contact Email Address")
            trv.heading(5, text="Specified address")
            trv.pack()

            #Connects to database
            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()
            #SQL query selcts everything from client table
            try:
                cursor.execute("SELECT * FROM Client")
                queryResult = cursor.fetchall()
                #Argument supplied to function in order to supply details
                update1(queryResult, trv)
            except:
                messagebox.showinfo(message="Not enough of info")

            #Identifies postcode structure and identifies whether it is located in the North , South or West. Takes a list of postcode initals as an argument.
            def check(list1):
                #SQL statement using LIKE clause
                sql_statementFunc = """SELECT postCode FROM Client WHERE postCode LIKE ?"""
                arr = []
                #The postcodes are checked against the values from the database.
                for i in range(0,len(list1)):
                    cursor.execute(sql_statementFunc, (list1[i],))
                    resultOfQuery = cursor.fetchall()
                    #Appends all result in list
                    try:
                        arr.append(resultOfQuery[0])
                    except IndexError:
                        print("Fine")
                    
                return len(arr)
            #Post codes

            postCodeNorth = ["LU%", "2121%", "WD%", "MK%", "CB%", "CV%"]
            postCodeWest = ["SL4%", "SL6%", "SL5%", "RG5%", "RG1%"]
            postCodeSouth = ["CR0%", "RH19%", "RH10%", "RH16%", "BN%"]

        

            #Left join used to display the corresponding clients and Orders from the client table.
            #Will identify which clients have orders placed, and which do not have orders placed. 
            #Uses Order By aggregate function.
            #Details displayed on table.
            query1 = """SELECT Client.ClientID, Order1.OrderID FROM Client 
            LEFT JOIN Order1 ON Client.ClientID = Order1.ClientID ORDER BY Client.ClientID"""
            cursor.execute(query1)
            queryResult1 = cursor.fetchall()
 

            trv1 = ttk.Treeview(window, columns=(1,2), show = "headings")
            trv1.pack()

          
            #Functions creates a visual platform
       
            trv1.heading(1, text="ClientID")
            trv1.heading(2, text="OrderID") 
            trv1.pack()
            update1(queryResult1, trv1)



            trv2 = ttk.Treeview(window, columns=(1,2,3), show = "headings")
            trv2.pack()
            #Functions creates a visual platform
            
            trv2.heading(1, text="North")
            trv2.heading(2, text="West") 
            trv2.heading(3, text="South") 
        
            trv2.pack()
            lengths = []
            lengths.append((check(postCodeNorth), check(postCodeWest), check(postCodeSouth), ))
            update1(lengths, trv2)
           




           
        

            





            


    window = Tk()
    obj = viewClients(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()