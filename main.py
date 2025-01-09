from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.title("PONG GAME")
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.speed_time)
    screen.update()
    ball.move()

    # Detection collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detection collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # If player miss the ball
    if ball.xcor() > 380:
        score.update_lscore()
        ball.reset_pos()
    elif ball.xcor() < -380:
        score.update_rscore()
        ball.reset_pos()

    if score.l_score >= 10 or score.r_score >= 10:
        game_on = False
        score.game_over()



screen.exitonclick()