from turtle import Turtle, Screen
from scoreboard import Scoreboard
import time
from player import Player
from roadway import Roadway
from car import Car



#Setting up screen with 800widthx600height
#@bg: background color
#@title: title of the window 
screen = Screen()
screen.setup(width = 800, height =600)
screen.bgcolor("DarkGray")
screen.title("Turtle Game")
#To remove animation
screen.tracer(0)


#Instantiate objects from their classes
scoreboard = Scoreboard()
roadway = Roadway()
player = Player()
car = Car()

#Detect keyboard stroke for up and down
screen.listen()
screen.onkey(key = "Up", fun = player.up)
screen.onkey(key = "Down", fun = player.down)


#Generate cars randomly across the screen from the roadways
car.create_cars()
car.move_cars()

#Turn on the game 
game_on = True
while game_on:

    #Delay the screen by 0.1sec
    #Constantly update the screen animation
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    #Detect collision on Top of screen
    if player.ycor() > 280:
        scoreboard.increase_diffculty()
        player.reset_position()

    #Detect collision with car
    for cars in car.all_car:
        if cars.distance(player) <20:
            game_on = False
            scoreboard.game_over()

#Click screen for exit
screen.exitonclick()
