from tkinter import *
import sqlite3


from tkinter import messagebox

def open3():
    class createClients:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            #Initalizes Front End
            
            #Function used to unpack components of program
            def initalize():
                name = StringVar(window)
                postCode = StringVar(window)
                email = StringVar(window)
                specifedAddress = StringVar(window)

                title = Label(window, text="Create Client", font = "Verdana 32 bold").place(x=690, y =50)

                name1 = Label(window, text="Name", font = "Verdana 14 bold").place(x=690, y = 120)
                enterName = Entry(window, textvariable=name).place(x=690, y = 180)

                #A list used to store details about coordinate plains
                coordinatePlain = ["North", "West", "South"]

                #Initalizes front end inputs
                self= Label(window, text="Contact Email Address", font = "Verdana 14 bold").place(x=690, y=240)
                self= Entry(window, textvariable=email).place(x=690, y=360)

                self = Label(window, text="Specified Address", font = "Verdana 14 bold").place(x=690, y =420)
                self= Entry(window, textvariable=specifedAddress).place(x=690, y = 540)

                #Drop down menu presenting options, in regards coordinate plain
                try:
                    dropDown = StringVar(window)
                    dropDown.set(coordinatePlain[0])
                    drop2 = OptionMenu(window, dropDown, *coordinatePlain)
                    drop2.place(x=690, y =600)
                    drop2.configure(width=20)
                except:
                    messagebox.showinfo("There is not enough of info 1")
                #Stores user selection 
                obtainDropDown = []
                #Function which identifies user input and acts accordingly.
                def check(dropDownValue):
                    #Appends selection 
                    def checkEmail(email):
                        x = email.endswith("@gmail.com")
                        print(x)
                        if x == False:
                            
                            messagebox.showinfo(message="Email is not valid")
                            open3()
                            return False
                        else:
                            return True
                    try:
                        obtainDropDown.append(dropDownValue)
                        checkEmail(email.get())

                        #Checks whether selection corresponds to a particular criterion
                        if obtainDropDown[0]== "North":
                            #Stores postcode initalials. 
                            initals = ["LU", "2121", "WD", "MK", "CB", "CV"]
                            #New Drop Down created, to present these initals. 
                            dropDown1 = StringVar(window)
                            dropDown1.set(initals[0])
                            drop3 = OptionMenu(window, dropDown1, *initals)
                            drop3.place(x=690, y = 600)
                            drop3.configure(width=20)
            
                        if obtainDropDown[0] == "West":
                            initals2= ["SL4", "SL6", "SL5", "RG5", "RG1"]
                            #New Drop Down created, to present these initals. 
                            dropDown1 = StringVar(window)
                            dropDown1.set(initals2[0])
                            drop3 = OptionMenu(window, dropDown1, *initals2)
                            drop3.place(x=690, y = 600)
                            drop3.configure(width=20)

                        if obtainDropDown[0] == "South":
                            initals3 = ["CR0", "RH19", "RH10", "RH16", "BN"]
                            #New Drop Down created, to present these initals. 
                            dropDown1 = StringVar(window)
                            dropDown1.set(initals3[0])
                            drop3 = OptionMenu(window, dropDown1, *initals3)
                            drop3.place(x=690, y = 600)
                            drop3.configure(width=20)
                    except:
                        messagebox.showinfo("The info is not enough 2")
                    
                    #Function to add details to Client table
                    def addClient(postCode, name, contactEmailAddress, SpecifiedAddress):
                

                        #Connecs to database
                        with sqlite3.connect("SalesOrderProcessing.db") as db:
                            cursor=db.cursor()
                                       
                        try:
                        #Parameterized SQL query which inserts into Clients table. Takes user input, and inserts accordingly.   
                            cursor.execute("INSERT INTO Client(postCode,name, contactEmailAddress,specifiedAddress) VALUES (?,?,?,?)", (postCode, name, contactEmailAddress, SpecifiedAddress))
                            db.commit()
                            messagebox.showinfo(message="The Client Details have been added")
                        except sqlite3.IntegrityError:
                            messagebox.showinfo(message="The Client detail already exists! ")

                  

                    #dropDown1.get().upper()+postCode.get().upper(), name.get(), email.get(), specifedAddress.get(),
                    addClient1 = Button(window, text="Enter", command=lambda:addClient(dropDown1.get().upper()+postCode.get().upper(), name.get(), email.get(), specifedAddress.get()), font = "Verdana 14 bold").place(x=840, y = 820)

                
                #Buttons initiating these functions.
                enterMoreinitals = Label(window, text="Enter any extra initials", font = "Verdana 14 bold").place(x=690, y = 720)
                enterPostCode = Entry(window, textvariable=postCode).place(x=690, y = 780)
                check1 = Button(window, text="Get postcodes", command=lambda:check(dropDown.get()), font = "Verdana 14 bold").place(x=690, y = 820)
                

                

            
                


                
                
                

            #Unpacks all the compoenents within the interface
            Open = Button(window, text="Open", command=initalize, font = "Verdana 14 bold").place(x=420, y = 420)

            




  

       


    window = Tk()
  

   
    
    obj = createClients(window)
    window.configure(bg="light blue")

    def destroy1():
        window.destroy()


    window.geometry("300x300")

    my_menu = Menu(window)

    window.config(menu=my_menu)

    file_menu = Menu(my_menu)
           
                


    my_menu.add_cascade(label="Options Menu", menu=file_menu)
    file_menu.add_command(label="Options Menu", command=destroy1)
    window.mainloop()