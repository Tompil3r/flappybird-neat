


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def copy(self):
        return Point(self.x, self.y)
    

    def distance(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5


class Dim:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    
    def copy(self):
        return Dim(self.width, self.height)
    

class Rect:
    def __init__(self, point, dim):
        self.point = point.copy()
        self.dim = dim.copy()

    
    def copy(self):
        return Rect(self.point, self.dim)

    
    def max_x(self):
        return (self.point.x + self.dim.width)


    def max_y(self):
        return (self.point.y + self.dim.height)


    def inside(self, point):
        return (self.point.x <= point.x <= self.max_x() and self.point.y <= point.y <= self.max_y())


    def corners(self):
        return [self.point.copy(), Point(self.max_x(), self.point.y), Point(self.max_x(), self.max_y()), Point(self.point.x, self.max_y())]


class Circle:
    def __init__(self, point, radius):
        self.point = point.copy()
        self.radius = radius

    
    def copy(self):
        return Circle(self.point, self.radius)


    def min_x(self):
        return (self.point.x - self.radius)
    

    def max_x(self):
        return (self.point.x + self.radius)
    

    def min_y(self):
        return (self.point.y - self.radius)
    

    def max_y(self):
        return (self.point.y + self.radius)
    

    def inside(self, point):
        return (self.point.x - point.x)**2 + (self.point.y - point.y)**2 <= self.radius**2
    
