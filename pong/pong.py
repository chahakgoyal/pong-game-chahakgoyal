#Author: Chahak Goyal
#Date: October 1, 2020
#Purpose: To make pong game

from cs1lib import *

#defining variables
#window dimensions
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

#paddle dimensions
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 80

#ball position and size
x_ball = WINDOW_WIDTH/2
y_ball = WINDOW_HEIGHT/2
SIZE = 10
#ball velocities and timestep
v_x = 120
v_y = -100
TIMESTEP = 1/60

#left paddle position
X_LEFT = 0
y_left = 0
#right paddle position
X_RIGHT = WINDOW_WIDTH - PADDLE_WIDTH
y_right = WINDOW_HEIGHT - PADDLE_HEIGHT
#paddle speed
MOVEMENT = 10
#key presses
PRESSED_A = False
PRESSED_Z = False
PRESSED_K = False
PRESSED_M = False
#to start a new game
PRESSED_SPACE = True


#defining a function to reset the game
def intializations():
    global x_ball, y_ball, v_x, v_y, X_LEFT, y_left, X_RIGHT, y_right
    x_ball = WINDOW_WIDTH/2
    y_ball = WINDOW_HEIGHT/2
    v_x = 120
    v_y = -100
    X_LEFT = 0
    y_left = 0
    X_RIGHT = WINDOW_WIDTH-PADDLE_WIDTH
    y_right = WINDOW_HEIGHT-PADDLE_HEIGHT


def my_key_press(key):
    global PRESSED_A, PRESSED_K, PRESSED_M, PRESSED_Z, PRESSED_Q, PRESSED_SPACE
    if key == "a":
        PRESSED_A = True
    if key == "k":
        PRESSED_K = True
    if key == "m":
        PRESSED_M = True
    if key == "z":
        PRESSED_Z = True
    if key == " ":
        PRESSED_SPACE = True
        intializations()
    #quits the program/game
    if key == "q":
        cs1_quit()
        

def my_key_release(key):
    global PRESSED_A, PRESSED_K, PRESSED_M, PRESSED_Z, PRESSED_Q
    if key == "a":
        PRESSED_A = False
    if key == "k":
        PRESSED_K = False
    if key == "m":
        PRESSED_M = False
    if key == "z":
        PRESSED_Z = False
        
        
def set_background():
    #yellow background color
    set_clear_color(1, 1, 0)
    clear()


#makes the paddles
def make_paddles():
    #global y_left, y_right
    
    #setting color of paddles to brown
    set_fill_color(0.5, 0.2, 0.1)
    disable_stroke()
    #left paddle
    draw_rectangle(X_LEFT, y_left, PADDLE_WIDTH, PADDLE_HEIGHT)
    #right paddle
    draw_rectangle(X_RIGHT, y_right, PADDLE_WIDTH, PADDLE_HEIGHT)
   
   
#moves the paddles
def paddle_movement():
    global PRESSED_A, PRESSED_K, PRESSED_M, PRESSED_Z, y_right, y_left
 
    #key pressed a then left paddle moves upward until it reaches the top
    if PRESSED_A and not y_left <= 0:
        y_left = y_left - MOVEMENT
    #key pressed z then left paddle moves downward until it reaches the bottom
    if PRESSED_Z and not y_left >= WINDOW_HEIGHT-PADDLE_HEIGHT:
         y_left = y_left + MOVEMENT
    #key pressed k then right paddle moves upward until it reaches the top
    if PRESSED_K and not y_right <= 0:
        y_right = y_right - MOVEMENT
    #key pressed m then right paddle moves downward until it reaches the bottom
    if PRESSED_M and not y_right >= WINDOW_HEIGHT-PADDLE_HEIGHT:
        y_right = y_right + MOVEMENT
    
    
    
#making the ball
def make_ball():
    global x_ball, y_ball
    #color green
    set_fill_color(0, 1, 0)
    draw_circle(x_ball, y_ball, SIZE)

#function to check collision of ball with horizontal walls as prompt asks
def ball_hits_horizontalwall(bally):
    if bally >= WINDOW_HEIGHT-SIZE or bally <= SIZE:
        return True
    else:
        return False

#function to check collision of ball with paddles as prompt asks
def ball_hits_paddles(ballx, bally):
    #collision of ball with left paddle
    if ballx == PADDLE_WIDTH+SIZE and y_left < bally < y_left+PADDLE_HEIGHT:
        return True
    #collision of ball with right paddle
    if ballx == WINDOW_WIDTH-PADDLE_WIDTH-SIZE and y_right < bally < y_right+PADDLE_HEIGHT:
        return True
    else:
        return False

#function to check if ball moves beyond vertical walls as prompt asks
def ball_moves_beyond_wall(ballx):
    if ballx == WINDOW_WIDTH or ballx == 0:
        return True
    else:
        return False
        
#function to see if the ball is colliding and if the game is in progress
def ball_movement():
    global x_ball, y_ball, v_x, v_y, PRESSED_SPACE
    #setting movement of the ball
    x_ball += v_x*TIMESTEP
    y_ball += v_y*TIMESTEP
    
    
    if ball_hits_horizontalwall(y_ball):
        v_y = -v_y
        
    if ball_hits_paddles(x_ball, y_ball):
        v_x = -v_x
    
    #to stop the game
    if ball_moves_beyond_wall(x_ball):
        PRESSED_SPACE = False
    
    
#calling all the above functions to make the game
def pong_game():
    global PRESSED_SPACE, v_x, v_y

    if PRESSED_SPACE:
        set_background()
        
        make_paddles()
        
        paddle_movement()
    
        make_ball()
    
        ball_movement()
        
    #to stop the game after the ball moves beyond vertical walls
    if not PRESSED_SPACE:
        v_x = 0
        v_y = 0
        enable_stroke()
        draw_text("GAME OVER", 160, 200)
        draw_text("PRESS SPACE TO PLAY", 130, 220)
        

start_graphics(pong_game, key_press=my_key_press, key_release=my_key_release)
