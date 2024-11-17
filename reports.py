from tkinter import *



from tkinter import messagebox


import sqlite3
def open23():
    class report:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            #Initalizing Front End. Combining function calls with buttons 
            self.title = Label(window, text="Reports", font = "Verdana 32 bold").pack(pady=20)

            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()

            #This document will contain the products which are frequenly ordered, 
            #the number of orders placed in a given time, the average quantity ordered
            #The most frequent clients which obtain orders.
      
            try:

                #Selects productID, and the frequency of an product from Order. The product name is also selected in resepect to the Order1 productID.
                #Case statement used and sub query.
                query1 = """SELECT Order1.ProductID, (SELECT ProductName FROM Product WHERE ProductID = Order1.ProductID), COUNT(ProductID), 
                
                CASE WHEN COUNT(ProductID) > 5 AND COUNT(ProductID) < 10 THEN "Small" 
                WHEN COUNT(ProductID) > 10 AND COUNT(ProductID) < 20 THEN "Medium" 
                WHEN COUNT(ProductID) > 20 THEN "Large"
                ELSE "Very Small"  
                END AS Frequent
                FROM Order1 GROUP BY ProductID ORDER BY COUNT(ProductID) DESC 
                
                """
                cursor.execute(query1)
                queryResult = cursor.fetchall()
                print(queryResult)
                #Identifies the number of orders in Order1 Table.
                cursor.execute("SELECT COUNT(OrderID) FROM Order1")
                queryResult2 = cursor.fetchall()
                print(queryResult2)
               

                #Uses case statement, and sub query
                #Fetches, quantity, Client Name and identifies the magnitude of the quantity.
                query2 = """SELECT Order1.Quantity, (SELECT Order1.ClientID FROM Order1 WHERE Quantity = Order1.Quantity),
                (SELECT name FROM Client WHERE ClientID = Order1.ClientID), 
                CASE WHEN Quantity >= 10 AND Quantity <=15 THEN "Small" 
                WHEN Quantity >= 20 AND Quantity <=30 THEN "Medium" 
                WHEN Quantity >= 30 THEN "Large" WHEN Quantity <=10 THEN "Very Low" 
                END AS QuantityIndicator FROM Order1 """
                cursor.execute(query2) 
                queryResult4 = cursor.fetchall()
                print(queryResult4)


                 #Calculates the average quantity in order table.
                cursor.execute("SELECT AVG(Quantity) FROM Order1 ")
                queryResult5 = cursor.fetchall()
                print(queryResult5)
                #Selects the max quantity from Order1
                cursor.execute("SELECT MAX(Quantity) FROM Order1 AS Max")
                queryResult6 = cursor.fetchall()
                print(queryResult6)
                #Uses sub query to identify information from within the client table, 
                # identifies mode average for sets of information

                cursor.execute("SELECT (SELECT name FROM Client WHERE ClientID = Order1.ClientID) ,COUNT(ClientID) FROM Order1 GROUP BY ClientID ORDER BY COUNT(ClientID) DESC")
                queryResult7 = cursor.fetchall()
                print(queryResult7)

                #Uses sub query to identify information from department table, 
                #Calculates frequency of categories accordingly.
                cursor.execute("SELECT (SELECT name FROM Department WHERE CategoryID = Product.CategoryID),  COUNT(CategoryID) FROM Product GROUP BY CategoryID ORDER BY COUNT(CategoryID) DESC")
                queryResult8 = cursor.fetchall()
                print(queryResult8)
            except:
                messagebox.showinfo(message="There is not enough info!")

            def com():
                def create_new():
                    labelInfo = Label(window, text="Add file name", font = "Verdana 14 bold").pack(pady=5)
                    entry = Entry(window)
                    entry.pack()

                    def get():
                        try:
                            body = f"""

                            Subject: Report: Info in regards to -Product Demand -Client Orders -Measure of averages \n
                            Frequent Orders: {queryResult}\n
                            Number of orders: {queryResult2}\n
                            Average Quantity: {queryResult5}\n
                            Department : {queryResult4}\n
                            Frequent Departments: {queryResult8}\n

                            

                            """
                            file_name = entry.get() + ".txt"
                            file = open(file_name, "w")
                            file.write(body)

                            messagebox.showinfo(message="File Downloaded")
                        except:
                            messagebox.showinfo(message="An Error occured")

                    get_button = Button(window, text="Create file", command=get, font = "Verdana 14 bold").pack(pady=5)
                    
                    
                    

                button1 = Button(window, text="Create New file", command=create_new, font = "Verdana 14 bold").pack(pady=5)

                button2 = Button(window, text="Using Existing file", font = "Verdana 14 bold").pack(pady=5)

            button = Button(window, text="Create Report", command=com, font = "Verdana 14 bold").pack(pady=5)

            


    window = Tk()
    obj = report(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()