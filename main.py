import tkinter
from tkinter import *

master=tkinter.Tk()
master.title("grid() method")
master.geometry("350x275")

count = 1

for x in range (15):
    for y in range(15):
        button=tkinter.Button(master, text = "     ")
        button.grid(row = x,column = y)
        count = count + 1

master.mainloop()