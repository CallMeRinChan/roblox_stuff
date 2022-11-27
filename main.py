# This is made by CallMeRinChan

# All the stuff you need to install:
# pip install pyautogui
# pip install pillow
# pip install keyboard
# pip install opencv-pythons
# pip install numpy

# importing modules
import pyautogui # for writing stuff to the mouse etc. this does a lot of stuff
import keyboard # for detecting keyboard inputs || also writes stufF?
import time # for time based stuff
import cv2 # for aids color checking
import numpy as np # for even more color checking aids
from PIL import ImageGrab

pyautogui.FAILSAFE = True #the biggest mistake ill make

# variable declaration
digger = False

# functions i guess

def checkPixel():
    px = ImageGrab.grab().load() # update the screen after doing a rebirth
    if np.any(px[170,900] == (255,15,15)): # if the color matches
        keyboard.press_and_release("F")

# print("The resolution is: ",screenWidth, screenHeight); # to print the resolution, nice for debugging i guess
# print("The center is: ", center) # just to show the center, nice for debugging i guess

while True:

    if keyboard.is_pressed('='):
        if digger == True:
            digger = False
        else:
            digger = True


    if digger == True:
        checkPixel() # check for a specific red pixel and press the F key
