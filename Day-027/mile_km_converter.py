from tkinter import *


#Create window screen , title, screen size, and background color.
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 300, height= 100)
window['bg'] = 'light blue'


#Setting up text label into specific grid
label = Label(text= "is equal to ")
label.grid(row = 1, column= 0)

Miles_label = Label(text = 'Miles')
Miles_label.grid(row = 0, column=2)

km_label = Label(text = "Km ")
km_label.grid(row=1, column=2)

total_km_label = Label(text="0")
total_km_label.grid(row = 1, column=1)

#Function that helps to convert the input from user's miles into km
#then display the km into the screen as green
def Calculate():
    miles = float(input.get())
    Km = miles * 1.60934
    total_km_label['text'] = Km
    total_km_label['fg'] = 'green'

#Create click button "Calculate" for user to calculate the converter from miles to km.
calculate = Button(text="Calculate", command= Calculate)
calculate.grid(row=2 , column=1)

#Create input message for user to input
input = Entry(width= 10)
input.insert(END,string= "0")
input.grid(row= 0, column=1)
input.get()

#To keep the screen on
window.mainloop()
