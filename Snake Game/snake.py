from turtle import Turtle

STARTING_SEGMENTS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_SEGMENTS:
            self.add_segment(position)
            
        
    
    def move(self):     
        for seg_num in range(len(self.segments)-1,0,-1 ):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.up()
        new_segment.speed(6)
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    
    def up(self):
        self.head.setheading(90)
    
    def left(self):
        self.head.setheading(180)

    def down(self):
        self.head.setheading(270)

    def right(self):
        self.head.setheading(0)
    
    def return_home(self):
        self.head.goto(0,0)
