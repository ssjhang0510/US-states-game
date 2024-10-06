import turtle
import pandas


screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
state_list = data["state"].to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50Guess the State",
                                    prompt="What's another state's name?").title()

    # If answer_state is one of the states in all the states of the 50_states.csv
        # If they got it right:
            # Create a turtle to write the name of state at the state's x and y coordinate

    if answer_state == "Exit":
        break
    if answer_state in state_list:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        # also can use: t.write(state_data.state.item())

# state_to_learn.csv
missing_state = []
for i in state_list:
    if i not in guessed_state:
        missing_state.append(i)

missing_data = pandas.DataFrame(missing_state)
missing_data.to_csv("missing states.csv")


# to get the coordinate when click on window
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

