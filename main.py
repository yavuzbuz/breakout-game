from turtle import Screen
from ball import Ball
from paddle import Paddle
from bricks import *
from game_over import Lost, Won
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

layers = [layer1, layer2, layer3, layer4, layer5, layer6, layer7]

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 655 or ball.xcor() < -655:
        ball.bounce_x()
    if ball.ycor() > 430:
        ball.bounce_y()

    if ball.distance(paddle) < 100 and ball.ycor() < -360:
        ball.bounce_y()

    for brick in layer1.layer_1:
        if ball.distance(brick) < 60 and 120 < ball.ycor() < 140:
            ball.bounce_y()
            brick.reset()
            ball.move_speed *= 0.9
            print(layer1.layer_1)

    for brick in layer2.layer_2:
        if ball.distance(brick) < 60 and 150 < ball.ycor() < 170:
            ball.bounce_y()
            brick.reset()
            ball.move_speed *= 0.9

    for brick in layer3.layer_3:
        if ball.distance(brick) < 60 and 180 < ball.ycor() < 200:
            ball.bounce_y()
            brick.reset()
            ball.move_speed *= 0.9

    for brick in layer4.layer_4:
        if ball.distance(brick) < 60 and 230 < ball.ycor() < 250:
            ball.bounce_y()
            brick.reset()
            ball.move_speed *= 0.9

    for brick in layer5.layer_5:
        if ball.distance(brick) < 60 and 260 < ball.ycor() < 280:
            ball.bounce_y()
            brick.reset()
            ball.move_speed *= 0.9

    for brick in layer6.layer_6:
        if ball.distance(brick) < 60 and 290 < ball.ycor() < 310:
            ball.bounce_y()
            brick.reset()
            ball.move_speed *= 0.9

    for brick in layer7.layer_7:
        if ball.distance(brick) < 60 and 320 < ball.ycor() < 340:
            ball.bounce_y()
            brick.reset()
            ball.move_speed *= 0.9

    if ball.ycor() < -450:
        ball.reset()
        paddle.reset()
        game_is_on = False
        pen = Lost()




screen.exitonclick()

