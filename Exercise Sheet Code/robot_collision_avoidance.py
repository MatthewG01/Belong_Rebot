# Import necessary Python libraries
from gpiozero import CamJamKitRobot, DistanceSensor

# Motor constants (must be in the range 0 < x <= 1)
FORWARD_SPEED = 0.25
BACKWARD_SPEED = 0.25
TURN_SPEED = 0.4

# Component constants
# These could change depending on where you plug your components onto the GPIO pins of your Pi
TRIGGER_PIN = 17 # Triggers transmission of sound waves
ECHO_PIN = 18 # Listens for sound wave echo. 
THRESHOLD = 0.3 # Sets the sensor threshold to trigger at 0.3m (30cm). Objects at and below 30cm treated as obstacles.

# Setting objects so their associated functions can be called
robot = CamJamKitRobot()
distanceSensor = DistanceSensor(echo = ECHO_PIN, trigger = TRIGGER_PIN, threshold_distance = THRESHOLD)

# Functions to control the motors of the robot
def forward():
    robot.forward(FORWARD_SPEED)

def backward():
    robot.backward(BACKWARD_SPEED)
    
def left():
    robot.left(TURN_SPEED)
    
def stop():
    robot.stop()

# Prints the distance calculated by the sensor in cm
def distance():
    distance = distanceSensor.distance * 100
    print(distance)

# Turn left to avoid obstacle and move in direction where no obstacle is within range
def avoid():
    distance()
    left()
    distanceSensor.wait_for_out_of_range()
    move()

def move():
    distance()
    forward()
    
while True:
    # Using "try" with "except" helps handle any errors that occur
    try:
        # Wait until robot is out of range of obstacle to begin 
        distanceSensor.wait_for_out_of_range()
        move()
        
        # If robot moves within range of obstacle, avoid obstacle
        distanceSensor.wait_for_in_range()
        avoid()
        
    # Press ctrl + c to stop the motors and terminate the program
    except KeyboardInterrupt:
        stop()
        quit()