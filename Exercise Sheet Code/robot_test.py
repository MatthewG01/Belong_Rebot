# Import necessary Python libraries
from gpiozero import CamJamKitRobot, LineSensor, DistanceSensor
import time

# Motor constants (must be in the range 0 < x <= 1)
FORWARD_SPEED = 0.25
BACKWARD_SPEED = 0.25
TURN_SPEED = 0.21

# Component constants
# These could change depending on where you plug your components onto the GPIO pins of your Pi
LINE_SENSOR_PIN = 25
DISTANCE_SENSOR_TRIGGER_PIN = 17 # Triggers transmission of sound waves
DISTANCE_SENSOR_ECHO_PIN = 18 # Listens for sound wave echo. 

# Setting objects so their associated functions can be called
robot = CamJamKitRobot()
lineSensor = LineSensor(pin = LINE_SENSOR_PIN)
distanceSensor = DistanceSensor(echo = DISTANCE_SENSOR_ECHO_PIN, trigger = DISTANCE_SENSOR_TRIGGER_PIN)

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

# Returns distance in cm up to the maximum distance. The default maximum distance is 100cm
def testDistance():
    print(distanceSensor.distance * 100)

# Test the line following sensor
# is_active will return true if the value exceeds the threshold (defaults to 0.5).
def testLine():
    if lineSensor.is_active:
        print("no line found")
    else:
        print("line found")
        
while True:
    # Get user input from the shell
    command = input("Enter a command: ")
    
    # Using "try" with "except" helps handle any errors that occur
    try:
        if command == "forward":
            print("forward")
            forward()
            time.sleep(3)
            stop()
                 
        elif command == "left":
            print("left")
            left()
            time.sleep(3)
            stop()    
        
        elif command == "right":
            print("right")
            right()
            time.sleep(3)
            stop()
            
        elif command == "backward":
            print("backward")
            backward()
            time.sleep(3)
            stop()
            
        elif command == "test distance":
            testDistance()
        
        elif command == "test line":
            testLine()
        
        # Catches all unrecognised commands
        else:
            print("Command not recognised")
    
    # Press ctrl + c to stop the motors and terminate the program
    except KeyboardInterrupt:
        stop()
        quit()