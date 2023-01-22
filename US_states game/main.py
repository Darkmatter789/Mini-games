import turtle
import pandas
from writer import Writer

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(width=700, height=500)
image = "US_states game/blank_states_img.gif"
file = "US_states game/50_states.csv"
screen.addshape(image)
turtle.shape(image)
w = Writer()
data = pandas.read_csv(file)


correct = list()

while len(correct) < 50:
    answer = screen.textinput(title=f"{len(correct)}/50 States Correct", prompt="What's another state name?").title()
    if answer == 'Exit':
        states_missed = [state for state in data.state if state not in correct]
        states_to_learn = pandas.DataFrame(states_missed)
        states_to_learn.to_csv("US_states game/states_to_learn.csv")
        print(states_missed)
        screen.bye()
        break
     
    if answer in data.state.to_list():
        state = data[data.state == answer]
        w.write_correct_state(answer, int(state.x), int(state.y))
        correct.append(answer)

turtle.mainloop()
