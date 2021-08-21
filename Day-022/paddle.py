from turtle import Turtle

#This class set up the paddles in the screen. 
#The paddle allows the user to move up and down.
#It has a width and height of 20
class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(*position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
