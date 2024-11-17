from tkinter import *



from tkinter import messagebox

from addClient import open3

from editClient import open4

from viewclient import open5
def open2():
    class clients:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            #Initalizing Front End. Combining function calls with uttons 
            self.title = Label(window, text="Clients", font = "Verdana 32 bold").pack(pady=20)

            self.CreateClientButton = Button(window, text="Create Client", command=self.openClientPage, font = "Verdana 20 bold").pack(pady=20)

            self.editClientTable = Button(window, text="Edit Client Table", command=self.openEditClient, font = "Verdana 20 bold").pack(pady=20)


            self.viewClientTable = Button(window, text="View Client Table", command=self.openviewclient, font = "Verdana 20 bold").pack(pady=20)
        #Opens corresponding pages according to user click. 
        def openClientPage(self):
            open3()
        def openEditClient(self):
            open4()
        def openviewclient(self):
            open5()


    window = Tk()
    obj = clients(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()