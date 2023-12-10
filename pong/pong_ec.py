#Author: Chahak Goyal
#Date: October 1, 2020
#Purpose: To make paddles for pong game and move them vertically

from cs1lib import *
from random import choice
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
#random velocity of the ball
v_x = choice([-2, -1, 1, 2])
v_y = choice([-2, -1, 1, 2])

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

#to change color everytime ball hits the paddles
f = 0

#variables for obstacles
x1 = 70
y1 = 80
LX1 = 10
LY1 = 60
x2 = 340
y2 = 100
LX2 = 80
LY2 = 10
x3 = 290
y3 = 260
x4 = 100
y4 = 360
vy1 = 1
vy2 = 1
vx1 = 1
vx2 = 1

#defining a function to reset the game
def intializations():
    global x_ball, y_ball, v_x, v_y, X_LEFT, y_left, X_RIGHT, y_right, f, x1, y1, x2, y2, x3, y3, x4, y4
    
    x_ball = WINDOW_WIDTH/2
    y_ball = WINDOW_HEIGHT/2
    v_x = choice([-2, -1, 1, 2])
    v_y = choice([-2, -1, 1, 2])
    X_LEFT = 0
    y_left = 0
    X_RIGHT = WINDOW_WIDTH-PADDLE_WIDTH
    y_right = WINDOW_HEIGHT-PADDLE_HEIGHT
    f = 0
    x1 = 70
    y1 = 80
    x2 = 340
    y2 = 100
    x3 = 290
    y3 = 260
    x4 = 100
    y4 = 360

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
    #setting color of paddles to brown
    set_fill_color(0.5, 0.2, 0.1)
    disable_stroke()
    #left paddle
    draw_rectangle(X_LEFT, y_left, PADDLE_WIDTH, PADDLE_HEIGHT)
    #right paddle
    draw_rectangle(X_RIGHT, y_right, PADDLE_WIDTH, PADDLE_HEIGHT)
   
#making the obstacles
def make_obstacles():
    set_fill_color(1, 0, 1)
    draw_rectangle(x1, y1, LX1, LY1)
    set_fill_color(0, 1, 0)
    draw_rectangle(x2, y2, LX1, LY1)
    set_fill_color(0, 0, 1)
    draw_rectangle(x3, y3, LX2, LY2)
    set_fill_color(0, 1, 1)
    draw_rectangle(x4, y4, LX2, LY2)


def obstacle_movement():
    global y1, y2, x3, x4, vx1, vx2, vy1, vy2
    y1 += vy1
    y2 += vy2
    x3 += vx1
    x4 += vx2
    if y1 == 0 or (y1 == y3+LY2 and x3 <= x1 <= x3+LX2-LX1):
        vy1 = -vy1
    #change direction if two obstacles collide
    if y1+LY1 == WINDOW_HEIGHT or (y1+LY1 == y3 and x3 <= x1 <= x3+LX2-LX1) or (y1+LY1 == y4 and x4 <= x1 <= x4+LX2-LX1):
        vy1 = -vy1
    if y2 <= 0 or (y2 == y3+LY2 and x3 <= x2 <= x3+LX2-LX1):
        vy2 = -vy2
    #change direction if two obstacles collide
    if y2+LY1 == WINDOW_HEIGHT or (y2+LY1 == y3 and x3 <= x2 <= x3+LX2-LX1) or (y2+LY1 == y4 and x4 <= x2 <= x4+LX2-LX1):
        vy2 = -vy2
    if x3+LX2 == WINDOW_WIDTH - PADDLE_WIDTH or (x3+LX2 == x2 and y2 <= y3 <= y2+LY1-LY2):
        vx1 = -vx1
    if x3 == PADDLE_WIDTH or (x3 == x1+LX1 and y1 <= y3 <= y1+LY1-LY2):
        vx1 = -vx1
    if x4+LX2 == WINDOW_WIDTH - PADDLE_WIDTH or (x4+LX2 == x2 and y2 <= y4 <= y2+LY1-LY2):
        vx2 = -vx2
    if x4 == PADDLE_WIDTH or (x4 == x1+LX1 and y1 <= y4 <= y1+LY1-LY2):
        vx2 = -vx2
        
#moves the paddles
def paddle_movement():
    global y_left, y_right, PRESSED_A, PRESSED_K, PRESSED_M, PRESSED_Z
 
    #key pressed a then left paddle moves upward until it reaches the top
    if PRESSED_A and not y_left<=0:
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
    #intial color red and after ball hits the paddle, f will update and so will the color of the ball
    set_fill_color(1*(1-f), 1*f/2, 1*(1-f))
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
    if ballx == PADDLE_WIDTH+SIZE and y_left <= bally <= y_left+PADDLE_HEIGHT:
        return True
    #collision of ball with right paddle
    if ballx == WINDOW_WIDTH-PADDLE_WIDTH-SIZE and y_right <= bally <= y_right+PADDLE_HEIGHT:
        return True
    else:
        return False

#check collision with vertical obstacles
def ball_hits_verticalobstacles(ballx, bally):
    if ballx == x1 - SIZE and y1 <= bally <= y1+LY1:
        return True
    if ballx == x1+LX1+SIZE and y1 <= bally <= y1+LY1:
        return True
    if ballx == x2 - SIZE and y2 <= bally <= y2+LY1:
        return True
    if ballx == x2+LX1+SIZE and y2 <= bally <= y2+LY1:
        return True
    else:
        return False
        
#check collision with horizontal obstacles
def ball_hits_horizontalobstacles(ballx, bally):
    if bally == y3 - SIZE and x3 <= ballx <= x3+LX2:
        return True
    if bally == y3+LY2+SIZE and x3 <= ballx <= x3+LX2:
        return True
    if bally == y4 - SIZE and x4 <= ballx <= x4+LX2:
        return True
    if bally == y4+LY2+SIZE and x4 <= ballx <= x4+LX2:
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
    global x_ball, y_ball, v_x, v_y, PRESSED_SPACE, f
    #setting movement of the ball
    x_ball += v_x
    y_ball += v_y
    
    if ball_hits_horizontalobstacles(x_ball, y_ball):
        v_y = -v_y
    
    if ball_hits_verticalobstacles(x_ball, y_ball):
        v_x = -v_x
    
    if ball_hits_horizontalwall(y_ball):
        v_y = -v_y
        
    if ball_hits_paddles(x_ball, y_ball):
        v_x = -v_x
        #updating f everytime ball hits one of the paddles to change ball color
        if f < 1:
            f += 1/8
        else:
            f = 0
        
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
        
        make_obstacles()
        
        obstacle_movement()
    
        ball_movement()
        
    #to stop the game after the ball moves beyond vertical walls
    if not PRESSED_SPACE:
        v_x = 0
        v_y = 0
        enable_stroke()
        draw_text("GAME OVER", 160, 200)
        draw_text("PRESS SPACE TO PLAY", 130, 220)
        

start_graphics(pong_game, key_press=my_key_press, key_release=my_key_release)
