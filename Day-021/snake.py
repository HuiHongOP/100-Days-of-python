from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#Create class Snake that starts from 3 segments
class Snake:

    #Attributes
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    #Start the 3 segements according to the starting coordinate
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    #Add starts by adding color, shape and the position of the segment
    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    #Add more segments into the snake
    def extend(self):
        self.add_segment(self.segments[-1].position())

    #Starting from last segment following the second last and second last follows third last and goes on.
    #It will stop on the head
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    #Allow the snake to move up,down, left, and right
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
