from gui import FlappyBirdGUI
from utils import Point, Dim, Rect, Circle
from bird import Bird
from pipe import Pipe
from collections import deque
import random




class FlappyBirdEnv:

    def __init__(self, population):
        self.population = population
        
        self.dim = Dim(800, 800)

        self.bird_radius = 20
        self.birds_start_point = Point(self.dim.width // 4, self.dim.height // 2)

        self.no_action = 0
        self.jump_action = 1

        self.nb_actions = 2

        self.gravity = 0.098
        self.jump_velocity = -4
        self.world_velocity = -2

        self.pipe_width = 80
        self.pipe_gap = 150
        self.gap_between_pipes = 200
        self.birds_pipe_gap = 400

        self.birds = None
        self.pipes = None
        self.next_pipe = None
        self.gui = FlappyBirdGUI(self)
    

    def step(self, actions):
        for idx, bird in enumerate(self.birds):
            if actions[idx] == self.no_action:
                bird.velocity += self.gravity
            elif actions[idx] == self.jump_action:
                bird.velocity = self.jump_velocity

            bird.move()

    
    def sample_action(self):
        return random.randint(0, self.nb_actions - 1)


    def populate_birds(self):
        return [Bird(Circle(self.birds_start_point, self.bird_radius)) for idx in range(self.population)]
    

    def generate_pipes(self):
        if self.pipes == None:
            self.pipes = deque()

        if len(self.pipes) == 0:
            pipe_x = self.birds_start_point.x + self.birds_pipe_gap
        
        else:
            pipe_x = self.pipes[-1].get_x() + self.gap_between_pipes
        
        while pipe_x < self.dim.width:
            top_rect_height = random.randint(0, self.dim.height - self.pipe_gap)
            top_rect = Rect(Point(pipe_x, 0), Dim(self.pipe_width, top_rect_height))
            bottom_rect = Rect(Point(pipe_x, top_rect_height + self.pipe_gap), Dim(self.pipe_width, self.dim.height - top_rect_height - self.pipe_gap))

            self.pipes.append(Pipe(top_rect, bottom_rect))

            pipe_x += self.pipe_width + self.gap_between_pipes

    
    def reset(self):
        self.gui.reset()
        self.birds = self.populate_birds()
        self.generate_pipes()
    

    def render(self):
        self.gui.render()
    

    def close(self):
        self.gui.close()


