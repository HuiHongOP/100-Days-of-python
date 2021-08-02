import random
#These are variable names
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Welcome message
print("Welcome to the rock paper scissors game to vs computer!\n")

#Make them into a list form
game_choice = [rock,paper,scissors]

#Let user to pick their choice of rock(0), paper(1), or sicssor(2)
user_choice = int(input("Pick '0' --> rock   or  '1' --> paper  or  '2' --> scissor: "))


#random generator choice of rock(0), paper(1), or sicssor(2) 
computer_generator = random.randint(0,2)


#Out of the choice range
if user_choice >=3 or user_choice <0:
    print("You have entered invalid input")

#Output the result of the game
else:
    #print the computer generate choice and user's choice
    print(f"Computer generated: {game_choice[computer_generator]}\n" )
    print(f"Your choice was: {game_choice[user_choice]} \n")
    if user_choice == computer_generator:
     print("It's a draw!")
    elif user_choice == 0 and computer_generator ==2:
        print("You win!")
    elif user_choice == 1 and computer_generator == 0:
        print("You win!")
    elif user_choice == 2 and computer_generator == 1:
        print("You win")
    elif computer_generator == 0 and user_choice ==2:
        print("You lose!")
    elif computer_generator == 1 and user_choice == 0:
     print("You lose!")
    elif computer_generator == 2 and user_choice == 1:
        print("You lose!")   


