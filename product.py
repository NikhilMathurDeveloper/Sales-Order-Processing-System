from tkinter import *

import mysql.connector as mysql

from tkinter import messagebox

from viewProducts import open8

from addProducts import open9

from addNewProduct import open10

from contactSupplier import open20

def open7():
    class products:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):

            #Front end established 
            self.title = Label(window, text="Products", font = "Verdana 32 bold").pack(pady=20)

            self.viewProductsButton = Button(window, text="View Products", command=self.openViewProducts, font = "Verdana 14 bold").pack(pady=20)

            self.updateProductStockButton = Button(window, text="Update product database", command=self.openAddProduct, font = "Verdana 14 bold").pack(pady=20)

            self.addProductButton = Button(window, text="Add product", command=self.openAddNewProduct, font = "Verdana 14 bold").pack(pady=20)


            self.button2 = Button(window, text="Contact Supplier", font = "Verdana 14 bold", command=self.openSupplierContact).pack(pady=20)
        #Functions activated according to user input.
        def openViewProducts(self):
            open8()
        def openAddProduct(self):
            open9()
        def openAddNewProduct(self):
            open10()
        def openSupplierContact(self):
            open20()




    window = Tk()
    obj = products(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()