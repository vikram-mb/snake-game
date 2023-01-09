from turtle import Turtle, pos


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []    # Keep track of all segments of turtles
        self.create_snake()
        self.head = self.segments[0]    # First segment is the head


    def create_snake(self):
        # Starting position
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("Skyblue")
        new_segment.penup()
        new_segment.goto(position)

        self.segments.append(new_segment)
    

    def move(self):
    # Move the snake      
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Get position of the 2nd segment, 3rd segment goes to where 2nd segment is, 2nd segment goes to where 1st segment is. 1st segment controls turning.
            # Get x and y coordinates of the 2nd last segment
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(new_x, new_y)    # Update last segment's coordinates with 2nd last coordinates
        
        self.head.forward(MOVE_DISTANCE)


    def extend(self):
        self.add_segment(self.segments[-1].position())  # Add segment at last segment's position
    

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)