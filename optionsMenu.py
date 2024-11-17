#Neccessary modules, from local files and libraries. 
from tkinter import *


import sqlite3
from tkinter import messagebox
from clients import open2

from product import open7

from order import open11
from invoice import open12

from delivery import open14
from reports import open23
def open1():
    class optionsMenu:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            #Initializing front end. Combining function calls with buttons.
            self.title = Label(window, text="Options Menu", font = "Verdana 32 bold").pack(pady=20)

            self.clientButton = Button(window, text="Clients", command=self.openClientPage, font = "Verdana 20 bold").pack(pady=20)

            self.productStockButton = Button(window, text="Product Stock", command=self.openProductPage, font = "Verdana 20 bold").pack(pady=20)


            self.orderButton = Button(window, text="Order", command=self.openOrderPage, font = "Verdana 20 bold").pack(pady=20)


            self.invoicePaymentButton = Button(window, text="Invoice and payment", command=self.openInvoiceMenu, font = "Verdana 20 bold").pack(pady=20)


            self.deliveryButton = Button(window, text="Delivery", command=self.openDelivery, font = "Verdana 20 bold").pack(pady=20)
            self.ReportButton = Button(window, text="Generate Reports", command=self.openReport,font = "Verdana 20 bold" ).pack(pady=20)

        #Opens corresponding pages according to user click. 
        def openClientPage(self):
            open2()
        def openProductPage(self):
            open7()
        def openOrderPage(self):
            open11()
        def openInvoiceMenu(self):
            open12()
        def openDelivery(self):
            open14()
        def openReport(self):
            open23()


    window = Tk()
    obj = optionsMenu(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()