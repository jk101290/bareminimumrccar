#Bare minimum RC car
#Using raspberry pi zero w and adafruit motor bonnet
#Wireless USB controller for input

#using inputs module from pypi.org for controller  
from inputs import get_gamepad

#using adafruit's motorkit module
from adafruit_motorkit import MotorKit

#set up motorkit instance
kit = MotorKit()

#set up controller codes for the 4 buttons we're using
#controller is PS3-like, X for forward, square for backward, left and right bumpers for turning
#i used a module called evdev to get the controller code names, a script called evtest.py
controller_input = {'ABS_RZ': 0, 'BTN_NORTH': 0, 'BTN_SOUTH': 0, 'ABS_Z': 0}

#set up a variable for speed so we can easily change it when needed
speed = 0.5

#this function returns the controller code for the button that is pressed, I googled for this 
def gamepad_update():
    # Code execution stops at the following line until gamepad event occurs.
    events = get_gamepad()
    return_code = 'No Match'
    for event in events:
        event_test = controller_input.get(event.code, 'No Match')
        if event_test != 'No Match':
            controller_input[event.code] = event.state
            return_code = event.code
        else:
            return_code = 'No Match'
 
    return return_code

#move forward function
def forward():
    if controller_input['BTN_SOUTH'] == 1:
        kit.motor1.throttle = -(speed)
        kit.motor2.throttle = -(speed)
        kit.motor3.throttle = speed
        kit.motor4.throttle = speed
    elif controller_input['BTN_SOUTH'] == 0:
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0
        kit.motor3.throttle = 0
        kit.motor4.throttle = 0

#move backward function
def backward():
    if controller_input['BTN_NORTH'] == 1:
        kit.motor1.throttle = speed
        kit.motor2.throttle = speed
        kit.motor3.throttle = -(speed)
        kit.motor4.throttle = -(speed)
    elif controller_input['BTN_NORTH'] == 0:
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0
        kit.motor3.throttle = 0
        kit.motor4.throttle = 0

#turn right function
def right():
    if controller_input['ABS_RZ'] == 255:
        kit.motor1.throttle = -(speed)
        kit.motor2.throttle = -(speed)
        kit.motor3.throttle = -(speed)
        kit.motor4.throttle = -(speed)
    elif controller_input['ABS_RZ'] == 0:
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0
        kit.motor3.throttle = 0
        kit.motor4.throttle = 0

#turn left function
def left():
    if controller_input['ABS_Z'] == 255:
        kit.motor1.throttle = speed
        kit.motor2.throttle = speed
        kit.motor3.throttle = speed
        kit.motor4.throttle = speed
    elif controller_input['ABS_Z'] == 0:
        kit.motor1.throttle = 0
        kit.motor2.throttle = 0
        kit.motor3.throttle = 0
        kit.motor4.throttle = 0
        
#This is where the main loop starts
while 1:
     # Get next controller Input, then call the corresponding movement function
    control_code = gamepad_update()        
     
    if control_code == 'BTN_SOUTH':
        forward()
    elif control_code == 'BTN_NORTH':
        backward()
    elif control_code == 'ABS_RZ':
        right()
    elif control_code == 'ABS_Z':
        left()

