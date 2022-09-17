import turtle
turtle.bgcolor("black")
turtlee = turtle.Screen()
turtlee.title("Faing Circle ")
turtle=turtle.Turtle()
turtle.color("red")
turtle.speed(0)
turtle.hideturtle()
for i in range(100):

        turtle.circle(i*2)
        turtle._rotate(5)
turtlee.done()