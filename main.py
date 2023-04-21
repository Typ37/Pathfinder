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

        #button2=tkinter.Button(master, text="button2")
        #button2.grid(row= x,column= y)

        #button3=tkinter.Button(master, text="button3")
        #button3.grid(row= x,column= y)

        #button4=tkinter.Button(master, text="button4")
        #button4.grid(row= x,column= y)

        #button5=tkinter.Button(master, text="button5")
        #button5.grid(row= x,column= y)
        count = count + 1

master.mainloop()