import turtle
import random
screen = turtle.Screen()
screen.setup(height=500, width=500)


target = turtle.Turtle(shape = "turtle")
target.penup()
target.goto(x= random.randint(-230 -5, 230+5), y=random.randint(-230-5, 230+5))

arrow = turtle.Turtle()
arrow.penup()

def forward():
    arrow.forward(10)
def backward():
    arrow.backward(10)
def right():
    arrow.right(10)
def left():
    arrow.left(10)
def checker():
    if int(arrow.xcor()) in range(target.xcor() - 10 , target.xcor() + 10)  or int(arrow.ycor()) in range(target.ycor() - 10 , target.ycor() + 10):
        print("Congrats you won! ")
    else:
        print("Sorry! you lost better luck next time. ")
    screen.bye()


screen.listen()

screen.onkeypress(fun= forward, key = "w")

screen.onkeypress(fun= backward, key = "s")

screen.onkeypress(fun= right, key = "d")

screen.onkeypress(fun= left, key = "a")

screen.onkeypress(fun= checker, key = "space")




screen.exitonclick()
