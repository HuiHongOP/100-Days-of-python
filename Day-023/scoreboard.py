from turtle import Turtle
style = ("Arial", 15, "italic")
score_position = [(-80,270)]


#This class will display the score on top of the screen for the user's score
class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("blue")
        self.penup()
        self.goto(*score_position)
        self.hideturtle()
        self.update_board()
        
    def update_board(self):
        self.write(f"Level of Diffculty:  {self.score}", align= "center", font=style)
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align= "center" , font = style)
    def increase_diffculty(self):
        self.score +=1
        self.clear()
        self.update_board()

