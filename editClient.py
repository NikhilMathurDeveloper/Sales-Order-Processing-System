from tkinter import *

import sqlite3

from tkinter import messagebox

from tkinter import ttk


def open4():
    class editClient:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            self.title = Label(window, text="Clients", font = "Verdana 32 bold").pack(pady=20)

            trv = ttk.Treeview(window, columns=(1,2,3,4,5), show = "headings")
            trv.pack()
            def update(rows):
                for i in rows:
                    trv.insert('', 'end', values=i)
            trv.heading(1, text="ClientID")
            trv.heading(2, text="PostCode")
            trv.heading(3, text="Name")
            trv.heading(4, text="Contact Email Address")
            trv.heading(5, text="Specified address")
            trv.pack()

            


            def remove():
                with sqlite3.connect("SalesOrderProcessing.db") as db:
                        cursor=db.cursor()

                

                    
                x = trv.selection()[0]

                print(trv.item(x)['values'])
                uid = trv.item(x)['values'][0]

                

                
        
                query = "DELETE FROM Client WHERE ClientID = ?"
                cursor.execute(query, (uid, ))
                db.commit()

                trv.delete(x)
                messagebox.showinfo(message="Details have been removed")
            

            self.button = Button(window, text="Delete", command=remove, font = "Verdana 14 bold").pack(pady=20)
            with sqlite3.connect("SalesOrderProcessing.db") as db:
                cursor=db.cursor()
            cursor.execute("SELECT * FROM Client")
            result = cursor.fetchall()

            update(result)
            
                


        
    

        


    window = Tk()
    window.configure(bg="light blue")
    obj = editClient(window)

    window.geometry("300x300")
    window.mainloop()