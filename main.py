import turtle
import pandas
from turtle import Turtle, Screen

# Set up screen
screen = Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")

# Display map
map_turtle = Turtle()
map_turtle.penup()
map_turtle.shape("blank_states_img.gif")

write_turtle = Turtle()
write_turtle.hideturtle()
write_turtle.penup()
write_turtle.color("black")
# Read data
states_data = pandas.read_csv("50_states.csv")
print(states_data)

all_states = states_data["state"].tolist()
print(all_states)
print(len(all_states))
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states) / 50} states correct",
        prompt="What's your next state guess?")
    answer_state = answer_state.title()

    if answer_state == "Exit":
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_row = states_data[states_data["state"] == answer_state]
        x = state_row["x"].values[0]
        y = state_row["y"].values[0]
        write_turtle.goto(x, y)
        write_turtle.write(answer_state, align="center", font=("Arial", 8, "normal"))

    if answer_state in all_states and answer_state in guessed_states:
        print("you have already guessed it")

missed_state = [state for state in all_states if state not in guessed_states]


new_data = pandas.DataFrame(missed_state)

new_data.to_csv("states_to_learn.csv")


screen.mainloop()