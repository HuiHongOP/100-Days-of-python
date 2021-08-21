from turtle import Turtle
style = ("Arial", 15, "italic")

#This class helps to keep in track of the user score on top of the screen.
class Dashboard(Turtle):

    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.color("blue")
        self.penup()
        self.goto(*position)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align= "center", font=style)

    def game_over(self,player):
        self.goto(0, 0)
        self.write(f"GAME OVER: {player} player has won.", align="center", font=style)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

