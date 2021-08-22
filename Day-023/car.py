from turtle import Turtle, position
import random
colors = ['red', 'blue', 'orange', 'purple', 'pink','green','yellow']
Roadway_position = [(200,260),(90,140),(-30,40),(-260,-200),(-150,-90)]


#A class that randomly generate cars across the roadways
class Car(Turtle):
    def __init__(self):
        self.all_car= []

    #Randomly generate cars to the roadways from 1 in 6 chance.
    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            position = random.choice(Roadway_position)
            random_y = random.randint(*position)
            new_car.goto(300,random_y)
            self.all_car.append(new_car)
    
    #Move the cars from right to left side because it started from 300 as x-coordinate
    def move_cars(self):
        for car in self.all_car:
            car.backward(10)

