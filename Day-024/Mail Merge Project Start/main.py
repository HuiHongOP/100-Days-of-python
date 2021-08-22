#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp




#@name_list: store every name in file as an item.
#Each item that is in the name_list will contain \n at end of the item string.
name_list= []
with open("Input/Names/invited_names.txt") as name:
    name_list = name.readlines()

#@letter_message: store the letter message in "starting_letter.txt".
letter_message=""
with open("Input/Letters/starting_letter.txt") as letter:
    letter_message = letter.read()


#The strip will clean out the "\n for each name in name_list"
#@name_with_message: A original message that is replace with the name instead of '[name]'
#Create new .txt file for each invited name
def send_mail():
    for name in name_list:
        name = name.strip("\n")
        name_with_message = letter_message.replace("[name]",name)
        with open(f"Output\ReadyToSend\{name}.txt",mode="w") as send_letter:
            send_letter.write(name_with_message)

#Call function
send_mail()