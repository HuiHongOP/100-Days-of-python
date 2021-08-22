#Reading Files
with open("Read.txt") as file:
    text = file.read()
    print(text)

#Writing to Files 
#It will delete previous text if there is any.
with open("write.txt", mode="w") as file:
    file.write("text.txt")
    
#Opening a File that doesn't exit in write mode will create it from scratch

with open("file_that_doesnt_exist.txt", mode="w") as file:
    file.write("New text.")


#Adding text into existed file without change the text.
with open("append.txt", mode = "a") as file:
    file.write("\n adding new append line.")
