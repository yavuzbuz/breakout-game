from turtle import Screen
from ball import Ball
from paddle import Paddle
import time

screen = Screen()

screen.setup(width=1400, height=900)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

ball = Ball()
paddle = Paddle(screen=screen)


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 680 or ball.xcor() < -680:
        ball.bounce_x()

    if ball.distance(paddle) < 100 and ball.ycor() < -360:
        ball.bounce_y()

screen.exitonclick()
