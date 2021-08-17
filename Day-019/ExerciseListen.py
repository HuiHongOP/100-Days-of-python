from turtle import Turtle,Screen


#set tim to Turtle class
tim = Turtle()
screen = Screen()


#turtle move forwards
def move_forwards():
    tim.forward(18)
#turtle move backwards
def move_backwards():
    tim.backward(18)

#turtle move counter clockwise
def Counter_clockwise():
    tim.setheading(tim.heading() + 10)
    tim.forward(18)

#turtle move clockwise
def Clockwise():
    tim.setheading(tim.heading() - 10)
    tim.forward(18)

#clear the previous drawing of the turtle
def Clear_draw():
    tim.clear()


screen.listen()
# screen.onkey(key="space", fun = move_forwards)

#drawing for the screen 
#Keyword: press w to move forwards
#Keyword: press s to move backwards
#Keyword: press a to move counter-clockwise
#Keyword: press d to move clockwise
#Keyword: press c to clear previous drawing

screen.onkey(key="w", fun = move_forwards)
screen.onkey(key="s", fun = move_backwards)
screen.onkey(key="a", fun = Counter_clockwise)
screen.onkey(key="d", fun = Clockwise)
screen.onkey(key="c", fun = Clear_draw)

#click on screen to exit
screen.exitonclick()
