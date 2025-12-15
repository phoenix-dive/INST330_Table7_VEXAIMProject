#region VEXcode Generated Robot Configuration
from vex import *
from vex.vex_globals import *
import math
import random

# Robot initialization for AIM platform
robot = Robot()

# Timer initialization
timer = Timer()

# Controller initialization

# AI Vision configuration code
robot.vision.model_detection(True)
robot.vision.tag_detection(True)

 # AI Vision colors
COLOR1 = Colordesc(1, 41, 157, 213, 10, 0.2)
robot.vision.color_description(COLOR1)
COLOR2 = Colordesc(2, 193, 48, 62, 10, 0.2)
robot.vision.color_description(COLOR2)
COLOR3 = Colordesc(3, 42, 185, 104, 10, 0.2)
robot.vision.color_description(COLOR3)

# Console Colors
def set_console_text_color(COLOR):
    if (COLOR == Color.RED):
        print("\033[31m", end="")
    elif (COLOR == Color.GREEN):
        print("\033[32m", end="")
    elif (COLOR == Color.BLUE):
        print("\033[34m", end="")
    elif (COLOR == Color.BLACK):
        print("\033[30m", end="")
    elif (COLOR == Color.WHITE):
        print("\033[37m", end="")
    elif (COLOR == Color.YELLOW):
        print("\033[33m", end="")
    elif (COLOR == Color.ORANGE):
        print("\033[91m", end="")
    elif (COLOR == Color.PURPLE):
        print("\033[35m", end="")
    elif (COLOR == Color.CYAN):
        print("\033[36m", end="")
    elif (COLOR == Color.TRANSPARENT):
        print("\033[97m", end="")
    else:
        print("\033[30m", end="")

# Clear Console
def clear_console():
    print("\033[2J", end="")

# User Uploaded Images
IMAGE1 = "image1.png"
IMAGE2 = "image2.png"
IMAGE3 = "image3.png"
IMAGE4 = "image4.png"
IMAGE5 = "image5.png"
IMAGE6 = "image6.png"
IMAGE7 = "image7.png"
IMAGE8 = "image8.png"
IMAGE9 = "image9.png"
IMAGE10 = "image10.png"


# User Uploaded Sounds
SOUND1 = "sound1.mp3"
SOUND2 = "sound2.mp3"
SOUND3 = "sound3.mp3"
SOUND4 = "sound4.mp3"
SOUND5 = "sound5.mp3"
SOUND6 = "sound6.mp3"
SOUND7 = "sound7.mp3"
SOUND8 = "sound8.mp3"
SOUND9 = "sound9.mp3"
SOUND10 = "sound10.mp3"


# reset console text color
set_console_text_color(BLUE)
# Reset the Inertial Sensor heading and rotation
robot.inertial.reset_heading()
robot.inertial.reset_rotation()

#endregion VEXcode Generated Robot Configuration

doing_things = True
vision_data = []
screen_precision = 0
console_precision = 0

robot.stop_all_movement()
robot.screen.show_aivision()
robot.move_at(0)

vision_data = robot.vision.get_data(TAG1)

# getting vision data
while doing_things == True:
    vision_data = robot.vision.get_data(TAG1)
    print(vision_data)
    if vision_data:
        if vision_data[0].width >= 60:
            robot.stop_all_movement()
            doing_things = False
            break
        else:
            robot.move_at(vision_data[0].bearing)

    else:
        robot.move_at(0)
    wait(20, MSEC)
    # does not work, lol, lmao een

robot.stop_all_movement()
print("Going to DNS ")
print("Server")
wait(2, SECONDS)
robot.set_turn_velocity(15, PERCENT)
robot.turn(LEFT)

# Turn left until AprilTag ID 2 is detected
while True:
    vision_data = robot.vision.get_data(BLUE_BARREL)

    if vision_data:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.get_heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)

# Get blue barrel
while True:
    vision_data = robot.vision.get_data(BLUE_BARREL)

    if vision_data:
        if robot.has_blue_barrel():
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)

robot.stop_all_movement()
print("Packet received,")
print("heading back ")
print("to Router")
wait(2, SECONDS)
robot.set_turn_velocity(100, PERCENT)
robot.move_for(3 * 25.4, 90)
vision_data = robot.vision.get_data(COLOR3)
robot.set_turn_velocity(15, PERCENT)

# Turn left until AprilTag ID 1 is detected
robot.turn(LEFT)
while True:
    vision_data = robot.vision.get_data(TAG1)

    if vision_data:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.get_heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)

vision_data = robot.vision.get_data(TAG1)

# Move to AprilTag ID 1
while True:
    vision_data = robot.vision.get_data(TAG1)

    if vision_data:
        if vision_data[0].width >= 60:
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)

print("Going back")
print(" to end device")
wait(2, SECONDS)
robot.move_for(35, 90)

# Turn right until AprilTag ID 0 is detected
robot.turn(RIGHT)
while True:
    vision_data = robot.vision.get_data(TAG0)

    if vision_data:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.get_heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)

# Move to AprilTag ID 0
while True:
    vision_data = robot.vision.get_data(TAG0)

    if vision_data:
        if vision_data[0].width >= 60:
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)

robot.stop_all_movement()
print("End device ")
print("acquired DNS packet")
print("heading towards")
print(" HTTP server ")
wait(2, SECONDS)

# Turn right until AprilTag ID 1 is detected
robot.turn(RIGHT)
while True:
    vision_data = robot.vision.get_data(TAG1)

    if vision_data:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.get_heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)

# Move to AprilTag ID 1
while True:
    vision_data = robot.vision.get_data(TAG1)

    if vision_data:
        if vision_data[0].width >= 60:
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)

robot.move_for(35, 90)

# Turn right until AprilTag ID 3 is detected
robot.turn(RIGHT)
while True:
    vision_data = robot.vision.get_data(TAG3)

    if vision_data:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.get_heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)

# Move to AprilTag ID 3
while True:
    vision_data = robot.vision.get_data(TAG3)

    if vision_data:
        if vision_data[0].width >= 60:
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)

print("DNS accepted")
print("receiving HTTP")
print("request")
wait(2, SECONDS)
robot.kicker.place()

# Turn left until orange barrel is detected
robot.turn(LEFT)
while True:
    vision_data = robot.vision.get_data(ORANGE_BARREL)

    if vision_data:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.get_heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)

vision_data = robot.vision.get_data(ORANGE_BARREL)

# Get orange barrel
while True:
    vision_data = robot.vision.get_data(ORANGE_BARREL)

    if vision_data:
        if robot.has_orange_barrel():
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)

# Turn left until AprilTag ID 1 is detected
robot.turn(LEFT)
while True:
    vision_data = robot.vision.get_data(TAG1)

    if vision_data:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.get_heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)

# Move to AprilTag ID 1
while True:
    vision_data = robot.vision.get_data(TAG1)

    if vision_data:
        if vision_data[0].width >= 60:
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)

robot.move_for(40, 270)

# Turn left until AprilTag ID 0 is detected
robot.turn(LEFT)
while True:
    vision_data = robot.vision.get_data(TAG0)

    if vision_data:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.get_heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)

# Move to AprilTag ID 0
while True:
    vision_data = robot.vision.get_data(TAG0)

    if vision_data:
        if vision_data[0].width >= 60:
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)

robot.kicker.place()
robot.stop_all_movement()
print("Begin")
print("Teardown")
wait(2, SECONDS)

# Turn right until AprilTag ID 1 is detected
robot.turn(RIGHT)
while True:
    vision_data = robot.vision.get_data(TAG1)

    if vision_data:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.get_heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)

# Move to AprilTag ID 1
while True:
    vision_data = robot.vision.get_data(TAG1)

    if vision_data:
        if vision_data[0].width >= 60:
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)

robot.stop_all_movement()
robot.move_for(30, 90)

# Turn right until AprilTag ID 3 is detected
robot.turn(RIGHT)
while True:
    vision_data = robot.vision.get_data(TAG3)

    if vision_data:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.get_heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)

# Get blue barrel
while True:
    vision_data = robot.vision.get_data(BLUE_BARREL)

    if vision_data:
        if robot.has_blue_barrel():
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)

robot.move_for(30, 270)

# Turn left until AprilTag ID 1 is detected
robot.turn(LEFT)
while True:
    vision_data = robot.vision.get_data(TAG1)

    if vision_data:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.get_heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)

# Move to AprilTag ID 1
while True:
    vision_data = robot.vision.get_data(TAG1)

    if vision_data:
        if vision_data[0].width >= 60:
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)

robot.move_for(30, 270)

# Turn left until AprilTag ID 0 is detected
robot.turn(LEFT)
while True:
    vision_data = robot.vision.get_data(TAG0)

    if vision_data:
        # Turn to the object by adding your current heading and the vision bearing offset
        robot.turn_to(robot.inertial.get_heading() + vision_data[0].bearing)
        break
    wait(20, MSEC)

# Move to AprilTag ID 0
while True:
    vision_data = robot.vision.get_data(TAG0)

    if vision_data:
        if vision_data[0].width >= 60:
            robot.stop_all_movement()
            break
        else:
            robot.move_at(vision_data[0].bearing)
    else:
        robot.move_at(0)
    wait(20, MSEC)

robot.kicker.place()
robot.sound.play_file(SOUND1)
while robot.sound.is_active():
    wait(50, MSEC)
