from turtle import Turtle


#has height : 20
#width = 20

#This class helps to keep in track of ball movement.
#Allows user to see the ball moving and target the ball.
#The ball will rebounce if it hits the end of the screen for y-coordinate. 
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *=-1
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
