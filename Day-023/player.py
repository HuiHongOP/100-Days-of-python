from turtle import Turtle

turtle_position = [(0,-280)]


#This class is a turtle. It allows the user to move up and down in a straight line.
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("purple")
        self.penup()
        self.goto(*turtle_position)
        self.left(90)
    def up(self):
        new_y = self.ycor() + 10
        self.goto(0,new_y)
    def down(self):
        new_y = self.ycor() - 10
        self.goto(0,new_y)
    def reset_position(self):
        new_y = self.ycor() * -1
        self.goto(0,new_y)
