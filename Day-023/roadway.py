from turtle import Turtle

#This class will draw roadways so that the user know
#there is cars coming. There are also spot where the user can be safe 
#from being crushed by.
class Roadway(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.top_half()
        self.middle_part()
        self.bottom_half()

    #Draw dashlines and straight lines 
    def drawer(self,street_coordinate):
        self.penup()
        self.goto(*street_coordinate[0])
        self.pendown()
        self.forward(800)
        self.penup()
        self.goto(*street_coordinate[1])
        for x in range(54):
            self.forward(10)
            self.penup()
            self.forward(5)
            self.pendown()    
        self.penup()
        self.goto(*street_coordinate[2])
        self.pendown()
        self.forward(800)

    #Draw the top half roadways of the screen
    def top_half(self):
        self.street_coordinate1 = [(-400,270),(-400,230), (-400,190)]
        self.drawer(self.street_coordinate1)
        self.street_coordinate2 = [(-400,160) , (-400,120), (-400,80)]
        self.drawer(self.street_coordinate2)

    #Draw the middle half roadways of the screen
    def middle_part(self):
        self.street_coordinate1 = [(-400,50),(-400,10), (-400,-40)]     
        self.drawer(self.street_coordinate1)

    #Draw the bottom half roadways of the screen
    def bottom_half(self):
        self.street_coordinate1 = [(-400,-270),(-400,-230), (-400,-190)]
        self.drawer(self.street_coordinate1)
        self.street_coordinate2 = [(-400,-160) , (-400,-120), (-400,-80)]
        self.drawer(self.street_coordinate2)
