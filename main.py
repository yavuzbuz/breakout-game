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

            layer1.destroyed_bricks.append(brick)
            if len(layer1.destroyed_bricks) == 12:
                layer1.layer1_complete = True

    for brick in layer2.layer_2:
        if ball.distance(brick) < 60 and 150 < ball.ycor() < 170:
            ball.bounce_y()
            brick.reset()
            ball.move_speed *= 0.9

            layer2.destroyed_bricks.append(brick)
            if len(layer2.destroyed_bricks) == 12:
                layer2.layer2_complete = True

    for brick in layer3.layer_3:
        if ball.distance(brick) < 60 and 180 < ball.ycor() < 200:
            ball.bounce_y()
            brick.reset()
            ball.move_speed *= 0.9

            layer3.destroyed_bricks.append(brick)
            if len(layer3.destroyed_bricks) == 12:
                layer3.layer3_complete = True

    for brick in layer4.layer_4:
        if ball.distance(brick) < 60 and 230 < ball.ycor() < 250:
            ball.bounce_y()
            brick.reset()
            ball.move_speed *= 0.9

            layer4.destroyed_bricks.append(brick)
            if len(layer4.destroyed_bricks) == 12:
                layer4.layer4_complete = True

    for brick in layer5.layer_5:
        if ball.distance(brick) < 60 and 260 < ball.ycor() < 280:
            ball.bounce_y()
            brick.reset()
            ball.move_speed *= 0.9

            layer5.destroyed_bricks.append(brick)
            if len(layer5.destroyed_bricks) == 12:
                layer5.layer5_complete = True

    for brick in layer6.layer_6:
        if ball.distance(brick) < 60 and 290 < ball.ycor() < 310:
            ball.bounce_y()
            brick.reset()
            ball.move_speed *= 0.9

            layer6.destroyed_bricks.append(brick)
            if len(layer6.destroyed_bricks) == 12:
                layer6.layer6_complete = True

    for brick in layer7.layer_7:
        if ball.distance(brick) < 60 and 320 < ball.ycor() < 340:
            ball.bounce_y()
            brick.reset()
            ball.move_speed *= 0.9

            layer7.destroyed_bricks.append(brick)
            if len(layer7.destroyed_bricks) == 12:
                layer7.layer7_complete = True

    if ball.ycor() < -450:
        ball.reset()
        paddle.reset()
        game_is_on = False
        pen = Lost()

    if layer1.layer1_complete and layer2.layer2_complete and layer3.layer3_complete and layer4.layer4_complete and\
            layer5.layer5_complete and layer6.layer6_complete and layer7.layer7_complete:
        ball.reset()
        paddle.reset()
        game_is_on = False
        pen = Won()


screen.exitonclick()
