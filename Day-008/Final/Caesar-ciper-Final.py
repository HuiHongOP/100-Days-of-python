alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar (cipher_message,shift_amount,decode_or_encode):
    Final_message = ""
    if decode_or_encode == "decode":
      shift_amount *=- 1
    for i in range(0,len(cipher_message)):
      #TODO-3: What happens if the user enters a number/symbol/space?
      #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
      #e.g. start_text = "meet me at 3"
      #end_text = "•••• •• •• 3"
      if cipher_message[i] in alphabet:
          store_index = (alphabet.index(cipher_message[i]))
          new_position = store_index+ shift_amount
          Final_message += alphabet[new_position]
      else:
          Final_message += cipher_message[i]
    print(f"This is {decode_or_encode} : {Final_message} ") 

#TODO-1: Import and print the logo from art.py when the program starts.

from art import logo
print (logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 

should_end = False
while not should_end:
    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
    #Hint: Think about how you can use the modulus (%).
    shift = shift %  26
    caesar(cipher_message = text,shift_amount = shift, decode_or_encode =direction )

    restart = input("Type 'yes' if you want to play it again. Otherwise type 'no' \n")
    if restart == "no":
        should_end = True
        print("Goodbye")
