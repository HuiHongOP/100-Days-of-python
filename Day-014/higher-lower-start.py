import random
from art import logo,vs
from game_data import data
from replit import clear

#print out the logo 
print(logo)


total_score = 0

#function that will compare the follower_count of the two people to see which have higher
#if user answered right it will add one to user's total_score
def Versus (person1,person2):
  global total_score
  print(f"Compare A: {person1[0]}")
  print(vs)
  print(f"Compare B: {person2[0]}")
  Winner = input("Who has more followers: 'A' or 'B': ")
  if person1 > person2 and person1[2] == Winner:
    total_score +=1
    clear()
    print(f"That's a right answer. Current score: {total_score}")
    return True
  elif person2> person1 and person2[2] == Winner:
    total_score +=1
    clear()
    print(f"That's a right answer. Current score: {total_score}")
    return True
  else:
    clear()
    print(f"Sorry, that's wrong. Final score: {total_score}")
    return False



#will randomly the person from the listed dictionary and return it's information
#@random_generator : random select from index 0 to size of the list-1
#@person_name: take in the person's name
#@person_descrpition: take in the person's description
#@person_country: take in the person's country
#@person_information: will store all the person's name,description, and country as a string
#@info_list = store the person's information and follower_count into a list
#@return info_list = will return the list that stores the person's information
def person_information():
  random_generator = random.randint(0,len(data)-1)
  person_name = data[random_generator]['name']
  person_description = data[random_generator]['description']
  person_country = data[random_generator]['country']
  person_information = person_name + ", " + person_description + ", " + person_country +"."
  info_list = []
  info_list.append(person_information)
  info_list.append(data[random_generator]['follower_count'])
  return info_list




#@start_game: will start up the game 
start_game = True

#@print will display the two person name with it's description and country.
#@user will have to guess who have more follower (person A or person B)
#@if user answered the wrong answer. The game will exit.
while start_game:
  person_one = person_information()
  person_one.append('A')
  person_two = person_information()
  person_two.append('B')
  if person_one[0] != person_two[0]:
    start_game = Versus(person1= person_one,person2=person_two)
    print(start_game)
  
