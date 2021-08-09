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
    

    def inside(self, rect):
        return not (self.circle.point.x - self.circle.radius < rect.point.x
        or self.circle.point.x + self.circle.radius >= rect.point.x + rect.dim.width
        or self.circle.point.y - self.circle.radius < rect.point.y
        or self.circle.point.y + self.circle.radius >= rect.point.y + rect.dim.height)
    

    def __str__(self):
        return f'Bird[circle={self.circle}, velocity={self.velocity}, alive={self.alive}, score={self.score}]'
