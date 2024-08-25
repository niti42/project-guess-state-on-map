from turtle import Turtle, Screen
import pandas as pd

# Screen
screen = Screen()
screen.setup(width=600, height=750)

# Map
turtle = Turtle()
screen.title("Guess The States")


country = screen.textinput(
    title=f"Choose Your Country", prompt="Do you want to guess states of India or USA?").lower()

if country == "india":
    image = "India-locator-map-resized.gif"
    data_path = "india_states_with_coords.csv"

else:
    image = "blank_states_img.gif"
    data_path = "50_states.csv"


screen.addshape(image)
turtle.shape(image)

# Write on screen
marker = Turtle()
marker.penup()
marker.hideturtle()
marker.color("black")

# get data
states_df = pd.read_csv(data_path)
all_states = states_df['state'].to_list()
correct_guess = []  # store all correct answers
while len(correct_guess) != len(all_states):
    # ask user
    answer_state = screen.textinput(
        title=f"{len(correct_guess)}/{len(all_states)} states correct", prompt="What's another state name?").title()
    if answer_state in all_states:
        state_data = states_df[states_df['state'] == answer_state]
        marker.goto(state_data.x.item(), state_data.y.item())
        state = state_data.state.item()
        marker.write(state)
        correct_guess.append(state)

    # Exit game
    elif answer_state == 'Exit':
        guessed_states = set(correct_guess)
        to_review = list(set(all_states)-guessed_states)
        to_review_df = pd.DataFrame(to_review, columns=['review'])
        to_review_df.to_csv('for_review.csv')
        break

if len(correct_guess) == len(all_states):
    marker.goto(0, 0)
    marker.color('purple')
    marker.write(f"Congrats! you got {len(correct_guess)}/{len(all_states)} correct",
                 align='center', font=("Arial", 16, "bold"))
screen.mainloop()
