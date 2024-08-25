from turtle import Turtle, Screen
import pandas as pd

# Setup screen and turtle
screen = Screen()
screen.setup(width=600, height=750)
turtle = Turtle()
image = "India-locator-map-resized.gif"
screen.addshape(image)
turtle.shape(image)

# Load the existing CSV data
df = pd.read_csv('india_states.csv')

# Function to handle the mouse click and record coordinates


def get_mouse_click_coor(x, y):
    global current_state_index
    state = states[current_state_index]
    print(f"{state}: ({x}, {y})")
    # Append the state name and its coordinates to the DataFrame
    df.loc[current_state_index, 'x'] = x
    df.loc[current_state_index, 'y'] = y
    current_state_index += 1
    if current_state_index < len(states):
        print(f"Next: Click on the location for {states[current_state_index]}")
    else:
        # Save the updated DataFrame to CSV
        df.to_csv('india_states_with_coords.csv', index=False)
        print("All states updated and saved!")


# State management
states = df['Name'].to_list()
current_state_index = 0

# Initial prompt for the first state
print(f"Click on the location for {states[current_state_index]}")
screen.onscreenclick(get_mouse_click_coor)

# Keep the window open
screen.mainloop()
