from tkinter import *

import sqlite3

from tkinter import messagebox

from tkinter import filedialog



def open13():
    class editDoc:
        def __init__(self, parent):
            self.widgets(parent)
        def widgets(self, window):
            #Establishes front end requirements
            self.title = Label(window, text="Edit Document", font = "Verdana 32 bold").pack(pady=20)
            self.my_text = Text(window, width=40, height=40)
            self.my_text.pack(pady=20)


            #Function open text file and writes information.
            def openText():
                text_file = filedialog.askopenfilename(filetypes=(("Text Files", "*.txt"), ))
                text_file = open(text_file, "r")
                info = text_file.read()
                self.my_text.insert(END, info)
                text_file.close()
            #Function saves information.
            def save():
                text_file = filedialog.askopenfilename(filetypes=(("Text Files", "*.txt"), ))
                text_file = open(text_file, "w")

                text_file.write(self.my_text.get(1.0, END))

                text_file.close()
                messagebox.showinfo(message="Saved")



            self.openFile = Button(window, text="Open text file", command=openText, font = "Verdana 14 bold")
            self.openFile.pack(pady=20)

            self.save = Button(window, text="Save file", command=save, font = "Verdana 14 bold")
            self.save.pack(pady=5)

            
   




    window = Tk()
    obj = editDoc(window)
    window.configure(bg="light blue")

    window.geometry("300x300")
    window.mainloop()