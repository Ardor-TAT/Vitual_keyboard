import tkinter
from tkinter import *

#let us see if this finally edits the main file or creates a new one

keyboard = tkinter.Tk()
keyboard.title("on screen keyboard")
keyboard.iconbitmap("C:\\Users\\HP\\Pictures\\exper_png.png")
keyboard.geometry('1010x250')
keyboard.configure(bg='red')
keyboard.resizable(0,0)
def select(value):
    entry.insert(tkinter.END,value)

buttons = {
    'Q','W','E','R','T','Y','U','I','O','P',
    'A','S','D','F','G','H','J','K','L',
    'Z','X','C','V','B','N','M','2','3'
    }

entry=tkinter.Entry(keyboard,width=150)
entry.grid(row= 1, columnspan=20)
varRow = 2
varColumn = 0
for button in buttons:
    command = lambda x=button: select(x) 
    tkinter.Button(keyboard,text=button , width =5 , bg="#000000",fg="#ffffff",
    activebackground ="#ffffff",activeforeground="#000000",relief='raised',padx=4, pady = 4, bd=4,
    command=command).grid(row=varRow , column = varColumn)
    varColumn+=1
    if varColumn>14 and varRow==2:
        varColumn = 0
        varRow+=1
    if varColumn> 14 and varRow==3:
        varColumn= 0
        varRow+=1
    
keyboard.mainloop()
    
