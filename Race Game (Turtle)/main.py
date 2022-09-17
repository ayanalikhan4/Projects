#Turtle Game
#
#
#


from turtle import Turtle, Screen
import random
is_race_on = False

screen = Screen()
screen.setup(height= 500, width = 500)
colors = ["red","black",  "orange", "goldenrod", "green", "blue", "purple", "light pink", "olive", "slate gray"]
y_positions = [-220, -170, -120, -70, -20, 30, 80, 130, 180, 230 ]
all_turtles = []


winner = screen.textinput(title="Choose your turtle: ", prompt="Which turtle will win? Enter a color")

for turtle_index in range(0,10):
    
    timmy = Turtle(shape = "turtle")
    timmy.color(colors[turtle_index])
    timmy.penup()
    #timmy.speed(0)
    timmy.goto(x= -230, y = y_positions[turtle_index])
    all_turtles.append(timmy)

if winner:
    is_race_on = True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 223:
            is_race_on = False
            winner_color = (turtle.pencolor())
            if winner == winner_color:
                print(f"You have won! The {winner_color} color is the winner. ")
            else:
                print(f"You lost! The {winner_color} color is the winner. ")

            
        else:
            fwd_distace = random.randint(0,10)
            turtle.forward(fwd_distace)

screen.exitonclick()
