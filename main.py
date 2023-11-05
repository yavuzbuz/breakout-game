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


screen.exitonclick()