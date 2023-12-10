#Author: Chahak Goyal
#Date: October 1, 2020
#Purpose: To make paddles for pong game and move them vertically

from cs1lib import *

#defining variables
#window dimensions
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

#paddle dimensions
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 80

#left paddle position
X_LEFT = 0
y_left = 0

#right paddle position
X_RIGHT = 380
y_right = 320

#speed of paddles
MOVEMENT = 10

#key presses
PRESSED_A = False
PRESSED_Z = False
PRESSED_K = False
PRESSED_M = False

def my_key_press(key):
    global PRESSED_A, PRESSED_K, PRESSED_M, PRESSED_Z
    if key == "a":
        PRESSED_A = True
    if key == "k":
        PRESSED_K = True
    if key == "m":
        PRESSED_M = True
    if key == "z":
        PRESSED_Z = True

def my_key_release(key):
    global PRESSED_A, PRESSED_K, PRESSED_M, PRESSED_Z
    if key == "a":
        PRESSED_A = False
    if key == "k":
        PRESSED_K = False
    if key == "m":
        PRESSED_M = False
    if key == "z":
        PRESSED_Z = False

def paddle():
    global y_left, y_right, PRESSED_A, PRESSED_K, PRESSED_M, PRESSED_Z
    
    #yellow background
    set_clear_color(1, 1, 0)
    clear()
    
    #brown color of paddles
    set_fill_color(0.5, 0.2, 0.1)
    disable_stroke()
    #paddle on the left
    draw_rectangle(X_LEFT, y_left, PADDLE_WIDTH, PADDLE_HEIGHT)
    #paddle on the right
    draw_rectangle(X_RIGHT, y_right, PADDLE_WIDTH, PADDLE_HEIGHT)
    
    #to prevent paddles from leaving the screen
    if y_left <= 0:
        PRESSED_A = False
    if y_left >= 320:
        PRESSED_Z = False
    if y_right >= 320:
        PRESSED_M = False
    if y_right <= 0:
        PRESSED_K = False
    
    #key pressed a then left paddle moves upward
    if PRESSED_A:
        y_left = y_left - MOVEMENT
    #key pressed z then left paddle moves downward
    if PRESSED_Z:
         y_left = y_left + MOVEMENT
    #key pressed k then right paddle moves upward
    if PRESSED_K:
        y_right = y_right - MOVEMENT
    #key pressed m then right paddle moves upward
    if PRESSED_M:
        y_right = y_right + MOVEMENT
        

start_graphics(paddle, key_press=my_key_press, key_release=my_key_release)
