# -*- coding: utf-8 -*-
import Tkinter as tk
import tkFont
from Tkinter import StringVar
from Tkinter import Label
from processor.processtext import ProcessText



'''
Method to change the label text
'''
def cambiarTexto(newText):
    var.set(newText)
    print newText


'''
Method to call the text processor when user press "enter" key
'''
def on_return_release(event):
    alerta = ProcessText()
    cambiarTexto(alerta.set_orden(text.get("1.0", "end -1 chars")))


'''
Basic Interface for the program
'''   
    
app = tk.Tk()

var = StringVar()
label = Label(app, textvariable=var) 
font = tkFont.Font(family='Helvetica', size=36, weight='bold')
label.pack()

text = tk.Text(app, width=50, font=font)
text.config(width=35, height=2)
text.pack()
text.bind("<KeyRelease-Return>", on_return_release)

app.mainloop()



