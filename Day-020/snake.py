from turtle import Screen, Turtle

#Create class name Snake that would start from the coordinate (x = 0 , y = 0)
#There would be three segments for start up for the Snake game
#There would be movement for the snake to move up, down, right , and left
start_coordinate = { (0, 0) , (-20, 0), (-40, 0)}
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments =[]
        self.create_snake()
        self.head = self.segments[0]

    #Creating 3 segments in the window for the snake
    #It would be green and the shape of circle
    def create_snake(self):
        for position in start_coordinate:
            new_segment = Turtle()
            new_segment.shape("circle")
            new_segment.color("green")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    #Starting from the last segment
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(20)
    
    #Setting the direction of snake
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

