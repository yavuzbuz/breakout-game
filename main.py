from turtle import Screen
from ball import Ball
from paddle import Paddle
from bricks import *
import time

screen = Screen()

screen.setup(width=1350, height=900)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

ball = Ball()
paddle = Paddle(screen=screen)
layer1 = Layer1()
layer2 = Layer2()
layer3 = Layer3()
layer4 = Layer4()
layer5 = Layer5()
layer6 = Layer6()
layer7 = Layer7()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 655 or ball.xcor() < -655:
        ball.bounce_x()

    if ball.distance(paddle) < 100 and ball.ycor() < -360:
        ball.bounce_y()

screen.exitonclick()
