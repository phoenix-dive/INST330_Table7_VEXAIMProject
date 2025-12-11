# Import Module
from tkinter import *
#from vex import *
#from vex.vex_globals import *

# Robot initialization for AIM platform
#robot=Robot()
# create root window
root = Tk()
#robot_speed = 10 # percent
# root window title and dimension
root.title("Packet Tracer Prototype")
# Set geometry (widthxheight)
root.geometry('800x600')

# adding a label to the root window
lbl = Button(root, text = "Searcb", activebackground="black")
lbl.grid(column = 1, row = 0)

# adding Entry Field
txt = Entry(root, width=50)
txt.grid(column =0, row =0)

root.mainloop()

