
#from ast import excepthandler
from tkinter import *

from forgotPassword import open28

from tkinter import messagebox



from optionsMenu import open1

import sqlite3

import pickle
from datetime import *
import re

from PIL import ImageTk, Image


#Creation of hash table data structure for register and login section.
class hashTable:
    #Constructor to initialize the objects attributes
    def __init__(self):
        self.capacity = 100
        self.numBuckets = [None] * self.capacity
    #Hash function which takes a key and produces a hashed value.
    def hash(self, key):
        sum = 0
        for i in range(0,len(key)):
            ascii_code = ord(key[i])
            sum = sum +ascii_code
        hash_value  = sum % self.capacity

        return hash_value
    #inserts the value into the hash table. Avoids collisions appropritately
    def insert(self, key, value):
        index = self.hash(key)
        pair = [key, value]

        if self.numBuckets[index-1] == None:
            self.numBuckets[index-1] = pair
            print("----")
            print(self.numBuckets)
        else: 
            while self.numBuckets[index-1] is not None:
                index+=1
            self.numBuckets[index-1] = pair
        
        return self.numBuckets
       
    #Searches for a particular item.
    def search(self, key):
        index = self.hash(key)
        
        if self.numBuckets[index-1] != None:
            print(self.numBuckets[index-1])
            return self.numBuckets[index-1]
        else:
            if self.numBuckets[index-1] == None:
                index +=1
      
#creation of hash object          
c = hashTable()







        

class register:
    def __init__(self, parent):
        self.widgets(parent)
    def widgets(self, window):
        capacity = 50

    

        #Initalizing Front End Components 
        self.title = Label(window, text="Register", font ="Verdana 32 bold").pack(pady=20)
        self.name = StringVar()

        self.logo = Image.open("logo1.png")
        self.resize = self.logo.resize((150, 100), Image.ANTIALIAS)
        self.new_pic = ImageTk.PhotoImage(self.resize)
        self.label = Label(image=self.new_pic)
        self.label.pack()

        #self.disclaimer = Label(window, text="Username: 8 Characters Long, Contains symbols, Numbers").pack(pady=20)
        #self.disclaimer2 = Label(window, text="Password: 8 Characters Long, Contains Numbers").pack(pady=20)
        
        self.password = StringVar()
        self.email = StringVar()
        self.pin = StringVar()

        self.username = Label(window, text="Username", font = "Verdana 20 bold").pack(pady=20)
        self.usernameEntry = Entry(window, textvariable=self.name).pack() #Username
        self.password1 = Label(window, text="Password", font = "Verdana 20 bold").pack(pady=20)
        self.passwordEntry = Entry(window, textvariable=self.password).pack(pady=20) #Password
        self.email1 = Label(window, text="Email", font = "Verdana 20 bold").pack(pady=20)
        self.emailEntry = Entry(window, textvariable=self.email).pack(pady=20) #Email

        self.pin1 = Label(window, text="Pin", font = "Verdana 20 bold").pack(pady=20)
        self.pinEntry = Entry(window, textvariable=self.pin).pack(pady=20) #Pin

        self.enter = Button(window, text="Enter", command=lambda: self.tableInsert(self.name.get(), register.hash1(self.password.get(),26),self.email.get()), font = "Verdana 20 bold").pack(pady=20)


        with sqlite3.connect("SalesOrderProcessing.db") as db:
            cursor=db.cursor()
        
        cursor.execute("DELETE FROM Product WHERE Amount < 0")
  
        db.commit()

        cursor.execute("PRAGMA foreign_keys = ON")

        #cursor.execute("DELETE FROM Product WHERE Amount <= 0")
        #query = '''CREATE TABLE IF NOT EXISTS Client (ClientID INTEGER PRIMARY KEY autoincrement, postCode Text unique, name Text unique, contactEmailAddress Text unique, specifiedAddress Text unique)'''

       

        #query = '''CREATE TABLE IF NOT EXISTS Order1 (OrderID INTEGER PRIMARY KEY autoincrement, ClientID INTEGER, ProductID INTEGER, DateOfRequirement Date, Quantity INTEGER, FOREIGN KEY(ClientID) REFERENCES Clients(ClientID), FOREIGN KEY(ProductID) REFERENCES Product(ProductID))'''

        #query = '''CREATE TABLE IF NOT EXISTS Department (CategoryID INTEGER PRIMARY KEY autoincrement, name Text unique)'''

        #query = '''CREATE TABLE IF NOT EXISTS Product (ProductID INTEGER PRIMARY KEY autoincrement, ProductName Text unique, CategoryID Integer, Amount Integer, DateOfExpiration Date, price Integer, FOREIGN KEY(CategoryID) REFERENCES Department(CategoryID))'''

        #query = '''CREATE TABLE IF NOT EXISTS Delivery (DeliveryID INTEGER PRIMARY KEY autoincrement, OrderID INTEGER unique, FOREIGN KEY(OrderID) REFERENCES Order1(OrderID))'''
       

        #query = '''CREATE TABLE IF NOT EXISTS Invoice (InvoiceID INTEGER PRIMARY KEY autoincrement, OrderID Integer unique, FOREIGN KEY(OrderID) REFERENCES Order1(OrderID))'''
  
        #cursor.execute("INSERT INTO Client VALUES (?,?,?,?)", ("BN12GR", "SouthMart", "South@gmail.com", "Brighton Avenue"))
        #db.commit()

        
        #cursor.execute("INSERT INTO Product(ProductName, CategoryID, Amount,DateOfExpiration, Price ) VALUES (?,?,?,?,?)", ("Chicken Drumsticks",1,500,"8/1/23", "5",))
        #db.commit()
        
        #cursor.execute("DROP TABLE Supplier")
        #query = '''CREATE TABLE IF NOT EXISTS Supplier (SupplierID INTEGER PRIMARY KEY autoincrement, name Text unique, contactEmailAddress Text, SpecifiedAddress Text unique, CategoryID integer,FOREIGN KEY(CategoryID) REFERENCES Department(CategoryID))'''
        #cursor.execute(query)
        #cursor.execute("INSERT INTO Supplier(name, contactEmailAddress, SpecifiedAddress, CategoryID ) VALUES (?,?,?,?)", ("Frozen Meat","mathurnikhil2004@gmail.com","Plymouth", 1))
        #cursor.execute("INSERT INTO Supplier(name, contactEmailAddress, SpecifiedAddress, CategoryID ) VALUES (?,?,?,?)", ("Fruits","mathurnikhil2004@gmail.com","London",2))
        #cursor.execute("INSERT INTO Supplier(name, contactEmailAddress, SpecifiedAddress, CategoryID ) VALUES (?,?,?,?)", ("Vegetables","mathurnikhil2004@gmail.com","Newcastle",3))
        #cursor.execute("INSERT INTO Supplier(name, contactEmailAddress, SpecifiedAddress, CategoryID ) VALUES (?,?,?,?)", ("Snacks","mathurnikhil2004@gmail.com","Nottingham",4))
        #cursor.execute("INSERT INTO Supplier(name, contactEmailAddress, SpecifiedAddress, CategoryID ) VALUES (?,?,?,?)", ("Beverages","mathurnikhil2004@gmail.com","Southampton",5))
        #cursor.execute("INSERT INTO Supplier(name, contactEmailAddress, SpecifiedAddress, CategoryID ) VALUES (?,?,?,?)", ("Ready Made Meals","mathurnikhil2004@gmail.com","Derby",6))
        #db.commit()
    
        
                

        

        #query = '''CREATE TABLE IF NOT EXISTS Shipment (ShipmentID INTEGER PRIMARY KEY autoincrement, SupplierID Integer, OrderID Integer , ShipmentDate Text, FOREIGN KEY(SupplierID) REFERENCES Supplier(SupplierID),FOREIGN KEY(OrderID) REFERENCES Order1(OrderID))'''


        #cursor.execute(query)
                    
        #db.commit()


        #query = '''CREATE TABLE IF NOT EXISTS "Order" (OrderID INTEGER PRIMARY KEY autoincrement, ClientID INTEGER, ProductID INTEGER, DateOfRequirement Date, Quantity INTEGER, FOREIGN KEY(ClientID) REFERENCES Clients(ClientID), FOREIGN KEY(ProductID) REFERENCES Product(ProductID))'''
        '''
        cursor.execute("SELECT DateOfExpiration FROM Product")
        queryResult = cursor.fetchall()

        queryResultStorage = []
        for item in queryResult:
            queryResultStorage.append(item)
        print(queryResultStorage)

        '''
        
        
        #date_time_obj = datetime.strptime(queryResultStorage[0][2], '%y/%m/%d')
        date2 = date.today()
        
        #if (date_time_obj.day == date1.day) and (date_time_obj.month == date1.month) and (date_time_obj.year == date1.year):
            #pass
        
        '''
        for j in queryResultStorage:
            date_time_obj = datetime.strptime(j[0], '%d/%m/%y')
    
            if date_time_obj.day == date2.day and date_time_obj.month == date2.month and date_time_obj.year == date2.year:
                query = "SELECT ProductID FROM Product WHERE DateOfExpiration =?"
                cursor.execute(query, (j[0],))
                queryResult = cursor.fetchall()
                print(queryResult)
                query2 = "DELETE FROM Product WHERE ProductID = ?"
                cursor.execute(query2, queryResult[0])
                db.commit()
                print("YEAAA")
        
        cursor.execute("SELECT DateOfRequirement FROM Order1")
        queryResult2 = cursor.fetchall()
        queryResultStorage2 = []
        for item1 in queryResult2:
            queryResultStorage2.append(item1)
        date1 = datetime.now()
        for i in queryResultStorage2:
            date_time_obj1 = datetime.strptime(i[0], '%y/%m/%d')
            calc = date_time_obj1 - date1
            print(calc.days)
            try:
                if date_time_obj1.day == date1.day and date_time_obj1.month == date1.month and date_time_obj1.year == date1.year:
                    query1 = "SELECT OrderID FROM Order1 WHERE DateOfRequirement =?"
                    cursor.execute(query1, (i[0],))
                    queryResult3 = cursor.fetchall()
                    print(queryResult3)
                    query3 = "DELETE FROM Order1 WHERE OrderID = ?"
                    cursor.execute(query3, (queryResult3[0], ))
                    db.commit()
                    print("Yes", str(queryResult3))

                if calc.days < 0:
                    query2 = "SELECT OrderID FROM Order1 WHERE DateOfRequirement =?"
                    cursor.execute(query2, (i[0], ))
                    queryResult4 = cursor.fetchall()
                    query4 = "DELETE FROM Order1 WHERE OrderID = ?"
                    cursor.execute(query4, queryResult4[0])
                    db.commit()
                    print("Yup", str(queryResult4))
            except IndexError:
                print("Its Allright")
        cursor.execute("SELECT DateOfExpiration FROM Product")
        queryResult6 = cursor.fetchall()
        queryResultStorage5 = []
        for items in queryResult6:
            queryResultStorage5.append(items[0])
        for result in queryResultStorage5:
            if result == date1:
                print("Yess")
        '''
        



        cursor.execute("SELECT EmployeeUsername, Password FROM REGISTER")
        queryResultRegister = cursor.fetchall()


        for j in queryResultRegister:
            print(j[0])
            print(j[1])
            c.insert(j[0], j[1])
 


        self.login = Button(window, text="Login", command=register.open, font ="Verdana 20 bold").pack(pady=20)
        #Connecting to Database

        
       

        
        '''
        
        try:
            if queryResult5[0][1] < 0:
                query5 = "DELETE FROM Product WHERE ProductID = ?"
                cursor.execute(query5,(queryResult5[0][0], ))
                db.commit()
            else:
                print("Alright :>")
        except IndexError:
            print("Its alright")
        '''
            

        
        
        

     

        #Self Produced DDL statements
        """
        query = ('''CREATE TABLE IF NOT EXISTS REGISTER(
        EmployeeUsername Text PRIMARY KEY,
        password Text,
        Email Text)
        ''')
        """

        

    def check(name, pin, password, email): #Checks details (If username is long enough, username consists of neccessary symbols. if the pin = 3245, and if email is valid)
        flagValue2 = False

        try:
            def checkName(name):
                #Flag Value used to validate username requirements, through initiating a checklist.
                try:
                    symbols = [".", ",", "-", "+", "!", "?"]
                    flagValue = 0
                    for character in name:
                        for symbol in symbols:
                            if character == symbol:
                                flagValue+=1
                    if flagValue == 1:
                        return True
                    else:
                        return False
                except:
                    messagebox.showinfo(message="An error occured")
         
            #Conditional statement checking whether username is valid through flag value.
            if checkName(name) == False:
                messagebox.showinfo(message="Your username does not have the valid symbols")
             
        
            #Pin constant established, and used to check whether employees bellong to business.

            def checkPin():
                pin1 = "3245"
                #Checks if inputed value is equal to the desired pin.
                if pin != pin1:
                    messagebox.showinfo(message="Company PIN is wrong")
                    return False
                else:
                    return True
           
            
            def checkPassword(password):
                if len(password) < 8:
                    messagebox.showinfo(message="Password is not long enough")
                    flagValue2 = True
                else:
                    flagValue2 = False
            

                checkIfContainNumber = bool(re.search(r'\d', password))
                
                if checkIfContainNumber == False:
                    flagValue2 = True
                    messagebox.showinfo(message="There are no numbers in the password")
                else:
                    flagValue2 = False

                if flagValue2:
                    return False
                else:
                    return True

            def checkEmail(email):
                x = email.endswith("@gmail.com")
                print(x)
                if x == False:
                    
                    messagebox.showinfo(message="Email is not valid")
                    return False
                else:
                    return True
                    

            if checkEmail(email) == True and checkPassword(password) == True and checkName(name) == True and checkPin() == True:
                flagValue2 = True
                print("ok")
            else:
                flagValue2 = False
                print('not ok')
            
                
      
                
            
            if flagValue2 == True:
                return True
            else:
                return False
  

            #Flag Value2 used to validate whether username is appropriate. 
            
        except:
            messagebox.showinfo(message="An error occured")

            
    #Hash function used to generate hashed values. This is used for addressing and for confidentiality in the Register Table when inserted.
    def hash1(hash_key, numberOFSlots):
        sum = 0
        for i in range(0,len(hash_key)-1):
            ascii_code = ord(hash_key[i])
            sum = sum + ascii_code
        hash_value = sum % numberOFSlots
        return hash_value
    
    #Table insert function which inserts the details into the Register Table.
    def tableInsert(self, name, password, email):
        
        if register.check(self.name.get(), self.pin.get(), self.password.get(), self.email.get()) == False:
            print("NOT VLAID")
            self.name.set("")
            self.password.set("")
            self.email.set("")
            self.pin.set("")     
        else:
            #Pickle used to save data structures, allowing updates to happen dynamically. 
            #Creates Pickle file storing all data from data structure. 
     
            #Hashes password ensuring confidentiality.
           
            
            hashed_password = register.hash1(self.password.get(), 26)

            c.insert(self.name.get(), hashed_password)

            
            


       
        
            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()
      
            #Parameterized INSERT SQL Statement. (?,?,?) denote user input, and prevent sql injection from occuring.
            cursor.execute("INSERT INTO REGISTER VALUES (?,?, ?)", (name, password, email))
            db.commit()
            register.open()
            messagebox.showinfo(message="Registered")


    def open():

      
        #Login page opened when user has registered. 
       
        top = Toplevel()
        top.title("Login")
        top.geometry("300x300")
        top.configure(bg="light blue")
        def forgot():

            open28()
        subheader = Label(top, text="Login",font = "Verdana 20 bold" ).pack()

        button1 = Button(top, text="Forgot Password", font = "Verdana 16 bold", command=forgot).pack(pady=5)


        username = Label(top, text="Username", font = "Verdana 20 bold")
        username.pack(pady=20)

        entryUsername = Entry(top)#Username
        entryUsername.pack(pady=20)


        password = Label(top,text="Password", font = "Verdana 20 bold")
        password.pack(pady=20)

        entryPassword = Entry(top)#Password
        entryPassword.pack(pady=20)


    
            

       

        #Check function takes two arguments, the employees username and password. 
        def check1(employeeUsername, password):
            #Flag value used to validate details.
            infoVariable = False
            flag1 = False
            #Function used to structure query in more understandable format.
            def insertIntoFormat(list1, result):
                for i in result:
                    list1.append(i[1])
                return list1
            #Connection to sqlite database
            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()
            #Function which checks employeeUsername. Takes the name as an argument. This function makes the code modular.
            def employeeUsername1(name):
                #Try and except used to handle errors. 
                try:
                    #Query using paramterized SQL CASE statement which checks if the username is present in the table. If yes - True If No - faLSE
                    query = """SELECT employeeUsername, CASE WHEN employeeUsername = ? THEN "True" ELSE "False" END AS FoundOrNot FROM REGISTER """
                    cursor.execute(query, (name, ))
                    #Query result storage list
                    queryResultStorage = []
                    #Executes query
                    resultFromExecution = cursor.fetchall()
                    #Calls formating function
                    insertIntoFormat(queryResultStorage, resultFromExecution)
                    #Returns the neccessary detail.
                    return queryResultStorage
                except:
                    messagebox.showinfo("Message there is not enough of information!")
            
            #Calls employeeUsername, taking check1 argument.
            for booleanValue in employeeUsername1(employeeUsername):
                #Updates flag1 value depending on condition.
                if booleanValue == "True":
                    flag1 = True
            print(flag1)
            
            try:
                #Checks against hash table
                if c.search(employeeUsername)[0] == "":
                    flag1 = False
                else:
                    flag1 = True
                print(flag1)
            except TypeError:
                messagebox.showinfo(message="The Username does not exist")

            
    
            #Function checks users password. Takes password as an argument. This function makes the code modular
            def employeePassword(name):
                # Try and Except used to hanldle exceptions.
                try:
                    #Uses Paramterized SELECT statement which takes employee username as a parameter.
                    query = """SELECT password FROM REGISTER WHERE EmployeeUsername = ? """
                    cursor.execute(query, (name, ))
                    resultFromExecution = cursor.fetchall()
                    return resultFromExecution
                except:
                    messagebox.showinfo("Message there is not enough of information!")
            #Checks if query equals to the inputed argument (password).  Checks against database
            try:
                if int(employeePassword(employeeUsername)[0][0]) == int(password):
                    flag1 = True
                
                print(int(password))
                print(int(c.search(employeeUsername)[1]))
                #Checks against hash table
                if int(c.search(employeeUsername)[1]) == int(password):
                    flag1 = True
     
                else:
                    flag1 = False
           
             
            
       
            except IndexError:
                messagebox.showinfo(message="Login Details are wrong")
                
            

           
   
            

            #Identifies the action according to a condition.
            if flag1 == True:
                messagebox.showinfo(message="You are allowed into the system")
                open1()
            else:
                messagebox.showinfo(message="Your are not allowed in the system")




        
            
        enter = Button(top, text="Enter", command=lambda: check1(entryUsername.get(), register.hash1(entryPassword.get(), 100)), font = "Verdana 20 bold")
        enter.pack(pady=20)


#Produced DDL statements.

#query = '''CREATE TABLE IF NOT EXISTS "Order" (OrderID INTEGER PRIMARY KEY autoincrement, ClientID INTEGER, ProductID INTEGER, DateOfRequirement Date, Quantity INTEGER, FOREIGN KEY(ClientID) REFERENCES Clients(ClientID), FOREIGN KEY(ProductID) REFERENCES Product(ProductID))'''
   
#query = '''CREATE TABLE IF NOT EXISTS Department (CategoryID INTEGER PRIMARY KEY autoincrement, name Text)'''

#query = '''CREATE TABLE IF NOT EXISTS Product (ProductID INTEGER PRIMARY KEY autoincrement, ProductName Text, CategoryID Integer, Amount Integer, DateOfRequirement Date, price Integer, FOREIGN KEY(CategoryID) REFERENCES Department(CategoryID))'''

#query = '''CREATE TABLE IF NOT EXISTS Delivery (DeliveryID INTEGER PRIMARY KEY autoincrement, OrderID INTEGER, FOREIGN KEY(OrderID) REFERENCES "Order"(OrderID))'''
            

#query = '''CREATE TABLE IF NOT EXISTS Invoice (InvoiceID INTEGER PRIMARY KEY autoincrement, OrderID Integer, FOREIGN KEY(OrderID) REFERENCES "Order"(OrderID))'''
            

#query = '''CREATE TABLE IF NOT EXISTS Order1 (OrderID INTEGER PRIMARY KEY autoincrement, ClientID INTEGER, ProductID INTEGER, DateOfRequirement Date, Quantity INTEGER, FOREIGN KEY(ClientID) REFERENCES Clients(ClientID), FOREIGN KEY(ProductID) REFERENCES Product(ProductID))'''
   
        
#cursor.execute(query)
            
#db.commit()
        

        




window = Tk()


window.configure(bg="light blue")

window.geometry("2000x1000")



obj = register(window)



window.mainloop()