import turtle
import pandas as pd
score = 0
screen = turtle.Screen()
screen.title("U.S. States Game")

#Read the csv file
data = pd.read_csv("50_states.csv")
#Make a list of all the states
all_state = data.state.to_list()

#Path to the image
image = "blank_states_img.gif"

#Adding extra image .gif into the screen shape
screen.addshape(image)

#Add into turtle display shape
turtle.shape(image)
game_is_on = True

#Keep in track of the user's guessed states
guessed_state = []

#This game only exit if you guessed all the states or type "Exit" on the prompt
#Allow user to guess what state is in the USA Map
#If the user gussed correctly, the screen will display the location of the state into the map gif
#If the user chosen to exit the game. The states that are not guessed right/did not answer will be put into a new csv file name "states_to_learn.csv"
while game_is_on:
    answer_state = screen.textinput(title = f"{score}/50", prompt="What is another state name? ")
    answer_state = answer_state.title()
    if score == 50:
        game = False
    if answer_state in all_state:
        jimmy = turtle.Turtle()
        jimmy.hideturtle()
        jimmy.color("red")
        jimmy.penup()
        state = data[data.state == answer_state]
        state_x_coord = state.x
        state_y_coord = state.y
        jimmy.goto(int(state_x_coord),int(state_y_coord))
        jimmy.write(answer_state)
        guessed_state.append(answer_state)
        score +=1
    if answer_state == "Exit" or answer_state == "exit":
        missing_state= []
        for state in all_state:
            if state not in guessed_state:
                missing_state.append(state)
        new_csv_file = pd.DataFrame(missing_state)
        new_csv_file.to_csv("states_to_learn.csv")
        game_is_on = False
#Keep the gif running
turtle.mainloop()

