from utils import Point


class Bird:
    def __init__(self, circle, alive=True, y_velocity=0):
        self.circle = circle
        self.y_velocity = y_velocity
        self.alive = alive
        self.nn = None
    

    def move(self):
        self.circle.point.y += self.y_velocity
