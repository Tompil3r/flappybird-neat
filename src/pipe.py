

class Pipe:
    '''
    Pipe is a combination of bottom and top pipes
    '''

    def __init__(self, top_rect, bottom_rect):
        assert top_rect.point.x == bottom_rect.point.x

        self.top_rect = top_rect
        self.bottom_rect = bottom_rect

    
    def hits(self, rect, circle):
        if rect.contains(circle.point):
            return True

        dist = (rect.center() - circle.point).abs()

        return (dist.x <= rect.dim.width + circle.radius) and (dist.y <= rect.dim.height + circle.radius) and \
        ((dist.x - rect.dim.width//2)**2 + (dist.y - rect.dim.height//2)**2 <= circle.radius**2)
        

    def hits_pipe(self, circle):
        return self.hits(self.top_rect, circle) or self.hits(self.bottom_rect, circle)


    def move(self, delta):
        self.top_rect.point.x += delta
        self.bottom_rect.point.x += delta
        
    
    def get_x(self):
        return self.top_rect.point.x
    

    def __str__(self):
        return f'Pipe[top_rect={self.top_rect}, bottom_rect={self.bottom_rect}]'