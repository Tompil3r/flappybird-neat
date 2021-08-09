from utils import Point


class Bird:
    def __init__(self, circle, alive=True, velocity=0):
        self.circle = circle
        self.velocity = velocity
        self.alive = alive
        self.score = 0
        self.nn = None
    

    def move(self):
        self.circle.point.y += self.velocity
