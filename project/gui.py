# Import Module
from tkinter import *
from vex import *
from vex.vex_globals import *

# Robot initialization for AIM platform
robot=Robot()
# create root window
root = Tk()
robot_speed = 10 # percent
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
    robot.turn(LEFT)

def up():
    robot_speed += 10
    robot.move_at(0, robot_speed)

    
def slow_down():
    robot_speed -= 10
    robot.move_at(0, robot_speed)

def turn_left():
    robot.turn_for(LEFT, 5)

def turn_right():
    robot.turn(RIGHT, 10)

# button widget with red color text inside
btnUp = Button(root, text = "Speed Up" ,
             fg = "red", command=up)
btnDown = Button(root, text = "Slow Down",
                command = slow_down)
btnLeft = Button(root, text = "Turn Left",
                 command = turn_left)
btnRight = Button(root, text = "Turn Right",
                 command = turn_right)
btnUp.grid(column = 3, row = 1)
btnLeft.grid(column = 2, row = 2)
btnRight.grid(column = 4, row = 2)
btnDown.grid(column = 3, row = 3)

# all widgets will be here
# Execute Tkinter
root.mainloop()

