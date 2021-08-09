#Number Guessing Game Objectives:

# Include an ASCII art logo.
import random
from art import logo
print(logo)


# Allow the player to submit a guess for a number between 1 and 100.
game_in_process = True
print("Welcome to the guessing number game! \n")
print("You will be guessing between 1 to 100 ")
difficulty_level = input("Pick a level: 'easy' or 'hard': ")
if difficulty_level == 'easy':
  live = 10
elif difficulty_level == 'hard':
  live = 5
else:
  print('You have entered invalid input for difficulty_level')
  game_in_process = False
generator = random.randint(1,100)

#This display the computer's random number generator
#print(generator)

def decrease_live(live_num):
  return live_num -1

# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def start_game():
  live_count = live
  start = game_in_process
  while start and live_count > 0:
    print(f"you have {live_count} number of attempt")
    guess_num = int(input("Guess a number: "))
    if generator > guess_num :
      print("It's too low ")
      print("guess again")
      live_count = decrease_live(live_num = live_count)
    elif generator < guess_num:
      print("It's too high ")
      print("guess again")
      live_count = decrease_live(live_num = live_count)
    else:
      print(f"congratulation, you guessed right! The answer was {generator}") 
      start = False
  if live_count ==0:
    print("You loss")


start_game()
