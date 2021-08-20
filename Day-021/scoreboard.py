from turtle import Turtle
ALIGN = 'center'
FONT = ("Arial",14,"normal")

#created a class Scoreboard inherit from Turtle class
class Scoreboard(Turtle):
  #Disply the score on the bottom center of the screen
  def __init__(self):
    #Able to access turtle methods 
    super().__init__()
    self.score = 0
    self.color("DeepPink2")
    self.penup()
    self.goto(0,-270)
    self.write(f"Score: {self.score}", align=ALIGN, font = FONT)
  def update_scorebard(self):
    self.write(f"Score: {self.score}", align=ALIGN, font = FONT)
  
  #Display the game over string in the middle of the screen
  def game_over(self):
    self.goto(0,0)
    self.write(f"GAME OVER", align=ALIGN, font = FONT)
  
  #Increase each time being called and update the score
  def increase_score(self):
    self.score +=1
    self.clear()
    self.update_scorebard()
