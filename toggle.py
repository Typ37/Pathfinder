# Import tkinter in the notebook
from tkinter import *

# Create an instance of window of frame
win = Tk()

# set Title
win.title('Toggle Button Demonstration')

# Set the Geometry
win.geometry("700x400")
win.resizable(0, 0)

# Create a variable to turn on the button initially
is_on = True

# Create Label to display the message
label = Label(win, text="On", bg="white", fg="black", font=("Poppins bold", 22))
label.pack(pady=20)

# Define our switch function
def button_mode():
   global is_on

   # Determine it is on or off
   if is_on:
      on_.config(image=off)
      label.config(text="Off", bg="white", fg="black")
      is_on = False
   else:
      on_.config(image=on)
      label.config(text="On", fg="black")
      is_on = True

# Define Our Images
on = PhotoImage(file="on.png")
off = PhotoImage(file="off.png")

# Create A Button
on_ = Button(win, image=on, bd=0, command=button_mode)
on_.pack(pady=25)

# Keep Running the window
win.mainloop()