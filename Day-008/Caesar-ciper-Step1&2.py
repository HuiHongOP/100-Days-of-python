alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt (cipher_message,shift_amount):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    store_index = []
    #plain_text = "hello"
    #shift = 5
    encoded = ""
    for i in range(0,len(cipher_message)):
      store_index.append(alphabet.index(cipher_message[i]))
      store_index[i] += shift_amount
      encoded += alphabet[store_index[i]]
    print(encoded) 
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-1.1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_message ,shift_amount):
  #TODO-2.1: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
    store_index = []
    #plain_text = "hello"
    #shift = 5
    decode = ""
    for i in range(0,len(cipher_message)):
      store_index.append(alphabet.index(cipher_message[i]))
      store_index[i] -= shift_amount
      decode += alphabet[store_index[i]]
    print(decode) 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

def Main_driver():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction == "encode":
    encrypt(cipher_message=text,shift_amount=shift)
  elif direction == "decode":
    decrypt(cipher_message=text,shift_amount=shift)
  else:
    print("You have entered invalid input")

Main_driver()
