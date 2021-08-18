from turtle import Screen, Turtle
import time
screen = Screen()
#Setting up the screen width and height

screen.setup(width= 600, height = 600)

#Set up the background screen color
screen.bgcolor("light blue")

#Title of the screen
screen.title("The Snake Game")

#Starting coordinate postion using tuples inside a list
start_coordinate = { (0, 0) , (-20, 0), (-40, 0),  }
segments = []

#Creating 3 segment into the screen
for coordinate in start_coordinate:
    new_segment = Turtle(shape = "square")
    new_segment.penup()
    new_segment.color("White")
    new_segment.goto(coordinate)
    segments.append(new_segment)

#time.sleep
#Will make the screen delay by second ( as integer)

#Making the snake moving forward
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        print(seg_num)
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)
    segments[0].forward(20)

#Exit screen on click
screen.exitonclick()
