from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps= 0 
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(Timer_text, text = "0:00")
    Timer_label.config(text = "Timer")
    check.config(text = "")
    global reps
    reps=0
    start['state'] = NORMAL
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps +=1
    #if it's 2/4/6
    start['state'] = DISABLED
    if reps % 2 !=0:
        count_down(WORK_MIN*60)
        Timer_label.config(text = "Work", fg = "purple1")

    #If it's 8 reps
    elif reps == 8:
        count_down(LONG_BREAK_MIN*60)
        Timer_label.config(text = "Break", fg = "sky blue")

    #If it's 2/4/6 reps
    else:
        count_down(5*60)
        Timer_label.config(text = "Break", fg = "sky blue")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(Timer_text, text=f"{count_min}:{count_sec}")
    if count >0 :
        global timer
        timer = window.after(1000,count_down, count -1)
    else:
        start_timer()
        marks =""
        for _ in range(math.floor(reps/2)):
            marks +="✓"
        check.config(text= f"{marks}")
# ---------------------------- UI SETUP ------------------------------- #

#Set up the screen and expand
window = Tk()
window.title("Tomato")
window.config(padx= 80, pady= 80,bg="yellow")


#Create structured graphic application
#Take in the image and display it 
canvas = Canvas(width = 200, height =224, highlightthickness=0)
canvas['bg'] = "yellow"
The_image= PhotoImage(file ="tomato.png")
canvas.create_image(102,112, image= The_image)
Timer_text = canvas.create_text(103,112,text="00:00", fill = "white", font = (FONT_NAME,25,"bold"))
canvas.grid(row=1, column =1)


#Have two buttons for user to click on "Start" and "Reset" the timer
start = Button(text = "Start", command = start_timer)
start.grid(row = 2, column = 0)

reset = Button(text = "Reset", command = reset_timer)
reset.grid(row = 2, column = 2)

#Label for a check each 2 reps
check = Label(text ="")
check.grid(row = 3, column = 1)
check.config(fg= "green",bg= "Yellow")

#Label that display "Work", "Break", or "Timer" on top of the tomato png
Timer_label = Label(text="Timer",font= (FONT_NAME, 35, "bold"))
Timer_label.config(fg= "green",bg= "Yellow")
Timer_label.grid(row = 0, column = 1)

#Keep screen on
window.mainloop()
