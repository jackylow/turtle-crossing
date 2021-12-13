from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_time = random.randint(1, 6)
        if random_time == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            y_pos = random.randint(-250, 250)
            new_car.goto(300, y_pos)
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.back(self.car_speed)

    def level_car(self):
        self.car_speed += MOVE_INCREMENT


