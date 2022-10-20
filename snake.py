import turtle

MOVE_DISTANCE = 20
POSITIONS = [(0,0),(0,-20),(0,-40)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("white")

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)
    
    def resetc(self):
        for seg  in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("white")


    def add_segment(self,position):
        segment = turtle.Turtle("square")
        segment.color("green")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            prevpos = (self.segments[i-1].xcor(),self.segments[i-1].ycor())
            self.segments[i].goto(prevpos)
        self.head.forward(20)

    def up(self):
        if(self.head.heading()!=DOWN):
            self.head.setheading(90)
    def down(self):
        if(self.head.heading()!=UP):
            self.head.setheading(270)
    def left(self):
        if(self.head.heading()!=RIGHT):
            self.head.setheading(180)
    def right(self):
        if(self.head.heading()!=LEFT):
            self.head.setheading(0)