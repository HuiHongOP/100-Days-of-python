from turtle import Screen
from snake import Snake
import time


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
#food = Food()

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

#Exit screen on click
screen.exitonclick()
