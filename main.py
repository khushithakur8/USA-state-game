import turtle
import pandas

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

screen = turtle.Screen()

screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


guessed_states = []

while len(guessed_states) < 50:
    state_input = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state name:")
    state_input = state_input.title()
    if state_input == "Exit":
        break
    if state_input in states:
        guessed_states.append(state_input)
        print(state_input)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == state_input]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_input) # can use item() for getting the first element

missed_states=[]
for state in states:
    if state not in guessed_states:
        missed_states.append(state)
refer = pandas.DataFrame(missed_states)
refer.to_csv("states_you_missed.csv")

screen.exitonclick()



turtle.mainloop()