from tkinter import *

import sqlite3
import smtplib
from tkinter import messagebox
from datetime import date
from editDoc import open13
from viewinvoice import open25



def open12():
    class invoices:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            self.title = Label(window, text="Invoices", font = "Verdana 32 bold").pack(pady=20)
            #Connects to database
            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()
            def openView():
                open25()
            def insertIntoFormat(list1, result):
                for i in result:
                    list1.append(i[0])
                return list1
            

            try:
                queryResultStorage = []
                #Select SQL Statement from Order table
                cursor.execute("SELECT OrderID FROM Order1")
                queryResult = cursor.fetchall()

                insertIntoFormat(queryResultStorage, queryResult)
                
                #Establishes front end
                self.label = Label(window, text="Select Order: ", font = "Verdana 14 bold").pack(pady=20)
                self.dropDown1 = StringVar(window)
                self.dropDown1.set(queryResultStorage[0])
                drop1 = OptionMenu(window, self.dropDown1, *queryResultStorage)
                drop1.pack(pady=20)
                drop1.configure(width=20)
            except:
                messagebox.showinfo(message="Not enough of info")
            
            #Create function creates invoice (OrderID taken as paramater). Making the code modular.
            def create(OrderID):
          
                
               

                
                with sqlite3.connect("SalesOrderProcessing.db") as db:
                    cursor=db.cursor()
                #SQL Statement selects ClientID From Order Table. and identifies the name in respect to ClientID from order table according to user input (Paramterized).
                #Uses Sub Query
                
                def queryCreation(OrderID):
                    try:
                        
                        #query = """SELECT Order1.ClientID, (SELECT name FROM Client WHERE ClientID = Order1.ClientID) 
                        #FROM Order1 WHERE OrderID = ? """

                        query = """SELECT name, postCode, specifiedAddress FROM Order1 INNER JOIN Client On Order1.ClientID = Client.ClientiD 
                        WHERE Order1.OrderID = ?"""
                    
                        cursor.execute(query, (OrderID, ))
                        queryResult = cursor.fetchall()
                        return queryResult
                    except:
                        messagebox.showinfo(message="There is not enough of info")


            
                
                #SQL statement selects productID from order accoridng to user input. This query is Paramterized.
                #Identifies ProductID, product Name in respect to the ProductID, and the Price in respect to the ProductID. 
                def queryCreation2(OrderID):
                    try:

                        #query2 = """SELECT Order1.ProductID, (SELECT productName FROM Product WHERE ProductID = Order1.ProductID), 
                        #(SELECT price FROM Product WHERE ProductID = Order1.ProductID) 
                        #FROM Order1 WHERE OrderID = ?"""
                        
                        #Product [0][0]
                        #Price [0][1]
                        query2 = """SELECT ProductName, Price, DateOfExpiration FROM Order1 INNER JOIN Product ON Order1.ProductID = Product.ProductID WHERE
                        Order1.OrderID = ?"""
                        cursor.execute(query2, (OrderID,)) 
                        queryResult3 = cursor.fetchall()
                        return queryResult3
                    except:
                        messagebox.showinfo(message="There is not enough of info.")
                
            
                


                #SQL statement selects quantity from order accoridng to user input. This query is Paramterized.
                def queryCreation3(OrderID):
                    try:
                        query3 = "SELECT Quantity FROM Order1 WHERE OrderID = ?"
                        cursor.execute(query3, (OrderID, ))
                        queryResult5 = cursor.fetchall()
                        return queryResult5[0]
                    except:
                        messagebox.showinfo(message="There is not enough of info")
            
                #Body for message in invoice
                #Takes query result and uses them appropriately.
                body = f"""
                
                    
                 

                    Subject: Pleasure doing business with you {queryCreation(OrderID)[0][0]}\n
                    Product: {queryCreation2(OrderID)[0][1]}\n
                    Amount: {queryCreation3(OrderID)}\n
                    Date Of Expiration: {queryCreation2(OrderID)[0][2]}\n
                    Post Code: {queryCreation(OrderID)[0][1]}\n,
                    Specified Address: {queryCreation(OrderID)[0][2]}\n
                    Date: {date.today()}\n
                """
                
                #Dyanmic usage of text files.
                name = "invoice"+str(queryCreation(OrderID)[0][0])+".txt"
                #Text files operations
                text_file = open(name, "w")
                text_file.write(body)
                text_file.close()
                #cursor.execute("INSERT INTO Product(ProductName, CategoryID, Amount,DateOfExpiration, Price ) VALUES (?,?,?,?,?)", ("Chicken Drumsticks",1,500,"8/1/23", "5",))
                #def insertIntoInvoiceTable(OrderID):

                    #cursor.execute("INSERT INTO Invoice(OrderID) VALUES (?)", (OrderID,))
                    #db.commit()
                #insertIntoInvoiceTable(OrderID)
            
                  
         


                #Function for sending details via email. 
                
                def send():

                    try:
                
                        body = f"""

                        Subject: Pleasure doing business with you {queryResult[0][1]}\n
                        Product: {queryCreation2(OrderID)[0][1]}\n
                        Amount: {queryCreation3(OrderID)}\n
                        Date Of Expiration: {queryCreation2(OrderID)[0][2]}\n
                        Post Code: {queryCreation(OrderID)[0][2]}\n,
                        Specified Address: {queryCreation(OrderID)[0][3]}\n
                        Date: {date.today()}\n
                        

                        """


                        #Details for gmail connection
                        sender = "computersciencetest6@gmail.com"

                        reciever = "mathurnikhil2004@gmail.com"

                        password = "vmvpienhhrgtmatq"
                        

                

                    

                        server = smtplib.SMTP('smtp.gmail.com',587)

                        server.starttls()

                        server.login(sender, password)

                        server.sendmail(sender, reciever, body)

                    
                        print("Mail Sent")
                        messagebox.showinfo(message="Mail Sent")

                        server.close()
                    except:
                        messagebox.showinfo(message="An error occured")

                buttonSend = Button(window, text="Send", command=send, font = "Verdana 14 bold").pack(pady=5)





            

            self.buttondDownload = Button(window, text="Download", command=lambda:create(self.dropDown1.get()), font = "Verdana 14 bold").pack(pady=5)
            self.buttonViewInvoice = Button(window, text="View Invoices", font = "Verdana 14 bold",command=openView).pack(pady=5)
            #Function call to open document
            def editDoc():
                open13()

            self.buttonEdit = Button(window, text="Edit Document", command=editDoc, font = "Verdana 14 bold").pack(pady=5)



    window = Tk()
    obj = invoices(window)
    window.configure(bg="light blue")
    window.geometry("300x300")
    window.mainloop()