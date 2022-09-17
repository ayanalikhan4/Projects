import turtle


screen = turtle.Screen()

turtle.speed(0)
def mov_fd():
    turtle.forward(100)
def mov_bck():
    turtle.backward(100)
def circle():
    turtle.circle(50)
def turn_left():
    turtle.left(10)
def turn_right():
    turtle.right(10)
def clear_scn():
    turtle.home()
    turtle.clear()
    
    turtle.setheading(00)


screen.listen()
screen.onkeypress(fun=mov_fd, key="w")
screen.onkeypress(fun=mov_bck, key="s")
screen.onkeypress(fun=circle, key="space")
screen.onkeypress(fun=turn_left, key="a")
screen.onkeypress(fun=turn_right, key="d")
screen.onkeypress(fun=clear_scn, key="c")



screen.exitonclick()
