# Bare Minimum RC Car
Simple RC car made with minimal parts

Ingredients:

raspberry pi zero w with rasberry pi OS lite 

adafruit DC motor bonnet

portable phone charger (for pi)

a battery pack with two 18650 style batteries (for motors)

4 "TT" dc motors with wheels

plastic chasis and some mounting hardware

wireless PS3 style controller with a tiny OTG adapter for the dongle

Coded in Python3

Required installs:

Inputs library: https://pypi.org/project/inputs/

Adafruit libraries: https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software

I used a module called evdev to get the names of the controller codes.  Install it and run evtest.py, and it will output the controller code name to the terminal. https://python-evdev.readthedocs.io/en/latest/install.html

![alt text](https://i.imgur.com/kEbuN5A.jpg)
