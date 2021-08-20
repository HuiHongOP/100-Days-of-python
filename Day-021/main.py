from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard
screen = Screen()

#Setup the screen wdith and height
screen.setup(width=600, height=600)

#Setup background color to be light blue
screen.bgcolor("light blue")

#Setup title name of the screen
screen.title("My Snake Game")
screen.tracer(0)

#Set object
snake = Snake()
food = Food()
scoreboard = Scoreboard()


#uses listen() to detect the keyboard 
screen.listen()
screen.onkey(key = "Up" ,fun =snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)


#Start up the snake game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    #detect collision with food
    #Distance will check the distance between the two
    if snake.head.distance(food) < 15:

      #After the food is being eaten
      food.refresh()
      snake.extend()
      scoreboard.increase_score()
    
    #Detect collision with wall
    if snake.head.xcor() >280 or snake.head.xcor() < -290 or snake.head.ycor() > 285 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
      if snake.head.distance(segment) <5:
        game_is_on = False
        scoreboard.game_over()
    
#Exit screen on click
screen.exitonclick()
