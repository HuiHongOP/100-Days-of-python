from tkinter import *
from tkinter import messagebox
import random
import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password_randomised_order =[]

    #Add 8 letters into the password
    password_randomised_order= [letters[random.randint(0,len(letters)-1)] for i in range(0,8,1)]

    #Add 3 symbols into the password
    password_randomised_order += [symbols[random.randint(0,len(symbols)-1)]  for i in range (0,3,1)]

    #Add 4 numbers into the password
    password_randomised_order += [numbers[random.randint(0,len(numbers)-1)]  for i in range (0,4,1)]

    #Would not work for string variable shuffle
    random.shuffle(password_randomised_order)

    #Join the list of letters,numbers and symbols into a string
    password_generate="".join(password_randomised_order)
    Password.insert(0,password_generate)
    print(password_generate)
    pyperclip.copy(password_generate)

# ---------------------------- SAVE PASSWORD ------------------------------- #

#Check if the string is empty.
#If empty string return false, else true.
def check_input(input_by_user):
    if len(input_by_user) == 0:
        return False
    else:
        return True

#Store the website, email, and password into a text file called "Account_Management.txt"
def password_store():
    website_bool = check_input(website.get())
    email_bool = check_input(email_username.get())
    password_bool = check_input(Password.get())

    save_info = False
    if website_bool and email_bool and password_bool:
        save_info = messagebox.askokcancel(title=website.get(), message=f"click 'Ok' if the informations are correct: \nEmail: {email_username.get()} \nPassword: {Password.get()}")
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave blank on any field!")


    if save_info:
        with open("Accout_Management.txt", mode = "a") as data:
            data.write(f"Website: {website.get()}")
            data.write(f"\nEmail/Username: {email_username.get()}")
            data.write(f"\nPassword: {Password.get()}")
            data.write("\n-----------------------------------------------------\n")
            #Deleting entry input by user
            website.delete(0,END)
            email_username.delete(0,END)
            Password.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width = 200, height = 200)
the_image = PhotoImage(file ='logo.png')
canvas.create_image(102,112, image = the_image)
canvas.grid(row=0,column =1)


website_label = Label(text="Website: ")
website_label.grid(row = 1, column=0)

email_username_label = Label(text = "Email/Username: ")
email_username_label.grid(row=2,column=0)

password_label = Label(text = "Password: ")
password_label.grid(row=3,column=0)


website = Entry(width= 38)
website.insert(END, string ="ex: www.google.com")
website.grid(row=1,column=1, columnspan=2)
website.get()

email_username = Entry(width= 38)
email_username.insert(END, string ="ex: Myemail52@gmail.com")
email_username.grid(row=2,column=1, columnspan =2)
email_username.get()

Password = Entry(width= 20)
Password.insert(END, string ="ex: ")
Password.grid(row=3,column=1)
Password.get()

add_button = Button(text = "Add", width =33, command =password_store)
add_button.grid(row = 5, column=1,columnspan=2)

generate_button = Button(text = "Generate Password", command=password_generator)
generate_button.grid(row = 3, column = 2)


window.mainloop()
