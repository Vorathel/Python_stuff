#!/usr/bin/python3
import tkinter as tk
from tkinter import messagebox as tkMessageBox

tkMessageBox.askyesno("Choose")


top = tk.Tk()

w = tk.Label(top,text='Hello World')
w.pack()

f=open('test.txt','r')		#
for line in f:			#Schreibt ersten 
	print (line[0])		#Buchstaben aus test.txt 

f.close()			#in terminal


top.mainloop()
