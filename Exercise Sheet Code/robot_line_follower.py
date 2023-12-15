# Import necessary Python libraries
from gpiozero import CamJamKitRobot, LineSensor
import time

# Motor constants (must be in the range 0 < x <= 1)
FORWARD_SPEED = 0.25
BACKWARD_SPEED = 0.25
TURN_SPEED = 0.25

# Component constants
# These could change depending on where you plug your components onto the GPIO pins of your Pi
LINE_SENSOR_PIN = 25

# Setting objects so their associated functions can be called
robot = CamJamKitRobot()
lineSensor = LineSensor(pin = LINE_SENSOR_PIN)

# Functions to control the motors of the robot
def forward():
    robot.forward(FORWARD_SPEED)

def backward():
    robot.backward(BACKWARD_SPEED)
    
def left():
    robot.left(TURN_SPEED)
    
def right():
    robot.right(TURN_SPEED)
    
def stop():
    robot.stop()

# Turns the robot left and right to find line if sensor moves off of line
def detectLine():
    robot.left(TURN_SPEED)
    time.sleep(1)
    robot.right(TURN_SPEED)

    lineSensor.when_line = follow
    lineSensor.when_no_line = search

# Follows line when found
def follow():
    print("found")
    forward()

# Activates detectLine() when line is lost
def search():
    print("lost")
    detectLine()

while True:
    # Using "try" with "except" helps handle any errors that occur
    try:
        # Waits for a line to be found to begin the line following program
        lineSensor.wait_for_line()
        forward()
        
        # If robot goes off line, stop and detect line
        lineSensor.wait_for_no_line()
        stop()
        detectLine()
    
    # Press ctrl + c to stop the motors and terminate the program
    except KeyboardInterrupt:
        stop()
        quit()
        
    

        

