from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.listen()


screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PONG GAME")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()


#Paddle control
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
x = 0.1
while game_is_on:
    time.sleep(x)
    screen.update()
    ball.ball_move()
    scoreboard.update_scoreboard()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
        x = x * 0.9


    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
        x = 0.1

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
        x = 0.1


screen.exitonclick()