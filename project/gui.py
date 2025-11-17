# Import Module
from tkinter import *
from vex import *
from vex.vex_globals import *

# Robot initialization for AIM platform
robot=Robot()
# create root window
root = Tk()

# root window title and dimension
root.title("Packet Tracer Prototype")
# Set geometry (widthxheight)
root.geometry('800x600')

# adding a label to the root window
lbl = Label(root, text = "insert url here...")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =0)


# function to display user text when 
# button is clicked
def clicked():

    res = "You wrote" + txt.get()
    robot.turn(LEFT)

def clicked_two():
    res="among us?"
    robot.move_at(0)
# button widget with red color text inside
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked_two)
# Set Button Grid
btn.grid(column=3, row=1)

# all widgets will be here
# Execute Tkinter
root.mainloop()

