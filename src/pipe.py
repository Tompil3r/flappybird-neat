

class Pipe:
    '''
    Pipe is a combination of bottom and top pipes
    '''

    def __init__(self, top_rect, bottom_rect):
        self.top_rect = top_rect
        self.bottom_rect = bottom_rect

    
    def hits(self, rect, circle):
        if rect.contains(circle.point):
            return True

        dist = (rect.center() - circle.point).abs()

        return (dist.x <= rect.dim.width + circle.radius) and (dist.y <= rect.dim.height + circle.radius) and \
        ((dist.x - rect.dim.width)**2 + (dist.y - rect.dim.height)**2 <= circle.radius**2)
        

    def hits(self, circle):
        return self.hits(self.top_rect, circle) or self.hits(self.bottom_rect, circle)