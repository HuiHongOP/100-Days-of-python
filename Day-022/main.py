from turtle import Screen
from dashboard import Dashboard
import time
from dashline import Dashline
from paddle import Paddle
from ball import Ball
score_position = [ (-180,270) , (180,270) ]
paddle_coordinate = [ (430,0), (-430,0)]


#Ask user how much point to win the game.
game_win_point =  int(input("How many game points you guys want to play?: "))


#Set up screen color, size, title , and remove animation
screen = Screen()
screen.setup(width = 900, height =600)
screen.bgcolor("orange")
screen.title("Pong Game")
screen.tracer(0)

#Setting up two paddle for left and right user
r_paddle = Paddle(paddle_coordinate[0])
l_paddle = Paddle(paddle_coordinate[1])

#A ball start from the center of the screen
ball = Ball()
#Draw a dashline in the  x-coordinate of 0 of the screen
dashline = Dashline()

#Keep in track of player score on top of the screen
dashboard_player1_left = Dashboard(score_position[0])
dashboard_player2_right = Dashboard(score_position[1])

#Detecting user's key stroke for direction of the paddles
screen.listen()
screen.onkey(key = "Up", fun = r_paddle.go_up)
screen.onkey(key = "Down", fun = r_paddle.go_down)
screen.onkey(key = "a", fun = l_paddle.go_up)
screen.onkey(key = "s", fun = l_paddle.go_down)


#Start the game
start_game = True
while start_game:
    time.sleep(.1)
    screen.update()
    ball.move()

    #Detect collision with Wall for the ball5
    if ball.ycor() > 285 or ball.ycor() <-285:
        #needs to bounds back
        ball.bounce_y()

    #Detect collision with right paddle and left paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() <- 340:
        ball.bounce_x()

    #Detect when the ball enters either side
    #Right paddle missed the ball
    if ball.xcor() > 440:
        ball.reset_position()
        dashboard_player1_left.increase_score()
    #left paddle missed the ball
    if ball.xcor() <-440:
        ball.reset_position()
        dashboard_player2_right.increase_score()

    #Keep in track which player wins.
    if dashboard_player2_right.score == game_win_point:
        dashboard_player2_right.game_over("right")
        start_game = False
    if dashboard_player1_left.score == game_win_point:
        dashboard_player1_left.game_over("left")
        start_game = False

screen.exitonclick()
