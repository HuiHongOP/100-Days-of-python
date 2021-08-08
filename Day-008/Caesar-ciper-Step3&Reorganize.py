alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar (cipher_message,shift_amount,decode_or_encode):
    store_index = []
    Final_message = ""
    if decode_or_encode == "decode":
      shift_amount *=- 1
    for i in range(0,len(cipher_message)):
      store_index.append(alphabet.index(cipher_message[i]))
      store_index[i] += shift_amount
      Final_message += alphabet[store_index[i]]
    print(f"This is {decode_or_encode} : {Final_message} ") 

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(cipher_message = text,shift_amount = shift, decode_or_encode =direction )
