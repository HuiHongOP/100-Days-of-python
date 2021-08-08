#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(letters[1] + letters[2] )
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


password_not_randomised =""
for i in range(0,nr_letters,1):
  #Instead of letters[random.randint(0,len(letters)-1)] 
  #Can be random.choice(list)
  password_not_randomised += letters[random.randint(0,len(letters)-1)]

for i in range (0,nr_symbols,1):
  password_not_randomised += symbols[random.randint(0,len(symbols)-1)]

for i in range (0,nr_numbers,1):
  password_not_randomised += numbers[random.randint(0,len(numbers)-1)]
print(f"Here is the password 'Not' being randomised order: {password_not_randomised}\n")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_randomised_order =[]

for i in range(0,nr_letters,1):
  password_randomised_order += letters[random.randint(0,len(letters)-1)]

for i in range (0,nr_symbols,1):
  password_randomised_order += symbols[random.randint(0,len(symbols)-1)]

for i in range (0,nr_numbers,1):
  password_randomised_order += numbers[random.randint(0,len(numbers)-1)]

#Would not work for string variable shuffle
random.shuffle(password_randomised_order)

#Convert list to string holder variable
result_str=""
for char in password_randomised_order:
  result_str += char

print(f"Here is the password being randomised order: {result_str}")

