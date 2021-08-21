from turtle import Turtle


#This class will draw a dashline in x-coordinate of 0
class Dashline(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.middleline()


    def middleline(self):
        self.penup()
        self.goto(0,310)
        self.hideturtle()
        self.right(90)
        for x in range(40):
            self.forward(10)
            self.penup()
            self.forward(5)
            self.pendown()      
