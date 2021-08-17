from turtle import Turtle, Screen
import random
import turtle

#Set screen to Screen() class
screen = Screen()


#Set up the screen width of 500 and height of 400
screen.setup(width = 500,height =400)

#Have user make bet which turtle color wins
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")


#Make different turtle color and set them into the race
#Make sure all turtle start from the same coordinate
colors = ['purple', 'red', 'SkyBlue', 'yellow', 'wheat','SpringGreen','tomato']
turtle_list = []

y_coordinate = -100
for i in range (0,len(colors)):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[i])
    new_turtle.shapesize(2)
    new_turtle.penup()
    new_turtle.goto(x= -230, y = y_coordinate)
    y_coordinate += 40
    turtle_list.append(new_turtle)


#check to see if there is a user input, then the game will start up
if user_bet:
    race_start = True


#If a turtle reached the end of the screen, then display the turtle as winner with it's color

while race_start:
    for turtle in turtle_list:
        #When the turtle reached the end of the screen
        if turtle.xcor()> 230:
            race_start = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle win the winner!")
            else:
                print(f"You've won! The {winning_color} turtle is the winner!")
        #turtle speed is being randomlize 
        rand_distance = random.randint(0,5)
        turtle.forward(rand_distance)

screen.exitonclick()
