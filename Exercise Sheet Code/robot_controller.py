# Import necessary Python libraries
from approxeng.input.selectbinder import ControllerResource
from gpiozero import CamJamKitRobot

# Controller stick deadzone
# Any values between the range -DEADZONE < 0 < DEADZONE will not register
# Adjust value according to your controller
# Value must be between 0 and 1
DEADZONE = 0.3

# Setting object so its associated functions can be called
robot = CamJamKitRobot()

# Functions to control the motors of the robot
# Based on the x-axis and y-axis values from left stick of controller
def forward(y):
    robot.forward(speed = y)

def backward(y):
    robot.backward(speed = -y)

def forwardWithRight(x, y):
    robot.forward(speed = y, curve_right = x)

def forwardWithLeft(x, y):
    robot.forward(speed = y, curve_left = -x)

def backwardWithRight(x, y):
    robot.backward(speed = -y, curve_right = x)
    
def backwardWithLeft(x, y):
    robot.backward(speed = -y, curve_left = -x)
    
def left(x):
    robot.left()
    
def right(x):
    robot.right()
    
def stop():
    robot.stop()

with ControllerResource() as controller:
    while controller.connected:
        # Using "try" with "except" helps handle any errors that occur
        try:
            # Get the x-axis and y-axis values from the left stick of connected controller
            leftStickX = controller["lx"]
            leftStickY = controller["ly"]
            
            # Determine where stick is moved to
            
            if leftStickY > DEADZONE and (0 <= leftStickX < DEADZONE or -DEADZONE < leftStickX <= 0):
                forward(leftStickY)
            
            elif leftStickY < -DEADZONE and (0 <= leftStickX < DEADZONE or -DEADZONE < leftStickX <= 0):
                backward(leftStickY)
                
            elif leftStickX >= 0 and leftStickY > DEADZONE:
                forwardWithRight(leftStickX, leftStickY)
                
            elif leftStickX <= 0 and leftStickY > DEADZONE:
                forwardWithLeft(leftStickX, leftStickY)
                
            elif leftStickX >= 0 and leftStickY < -DEADZONE:
                backwardWithRight(leftStickX, leftStickY)
            
            elif leftStickX <= 0 and leftStickY < -DEADZONE:
                backwardWithLeft(leftStickX, leftStickY)
                
            elif leftStickX < -DEADZONE and (0 <= leftStickY < DEADZONE or -DEADZONE < leftStickY <= 0):
                left(leftStickX)
            
            elif leftStickX > DEADZONE and (0 <= leftStickY < DEADZONE or -DEADZONE < leftStickY <= 0):
                right(leftStickX)
            
            # If no stick movement is detected, stop the motors
            else:
                stop()
        
        # Press ctrl + c to stop the motors and terminate the program
        except KeyboardInterrupt:
            stop()
            quit()
        
        # Output the x-axis and y-axis values
        # str() converts the values into a string so that print() can output them.
        print("y: " + str(leftStickY))
        print("x: " + str(leftStickX))

