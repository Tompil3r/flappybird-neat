


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def copy(self):
        return Point(self.x, self.y)
    

    def distance(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
    

    def as_tuple(self):
        return (self.x, self.y)


    def abs(self):
        return Point(abs(self.x), abs(self.y))


    def __iadd__(self, point):
        self.x += point.x
        self.y += point.y


    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)
    

    def __isub__(self, point):
        self.x -= point.x
        self.y -= point.y
    

    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y)
    

    def __imul__(self, point):
        self.x *= point.x
        self.y *= point.y


    def __mul__(self, point):
        return Point(self.x * point.x, self.y * point.y)

    
    def __idiv__(self, point):
        self.x /= point.x
        self.y /= point.y

    
    def __div__(self, point):
        return Point(self.x / point.x, self.y / point.y)


class Dim:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    
    def copy(self):
        return Dim(self.width, self.height)
    

    def as_tuple(self):
        return (self.width, self.height)
    

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
    

    def center(self):
        return Point(self.point.x + self.dim.width // 2, self.point.y + self.dim.height // 2)


    def contains(self, point):
        return (self.point.x <= point.x <= self.max_x() and self.point.y <= point.y <= self.max_y())


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
    

    def contains(self, point):
        return (self.point.x - point.x)**2 + (self.point.y - point.y)**2 <= self.radius**2
    
