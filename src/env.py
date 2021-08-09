from gui import FlappyBirdGUI
from utils import Point, Dim, Rect, Circle
from bird import Bird
from pipe import Pipe
from collections import deque
import random




class FlappyBirdEnv:

    def __init__(self, population):
        self.population = population
        
        self.rect = Rect(Point(0, 0), Dim(800, 800))

        self.bird_radius = 20
        self.birds_start_point = Point(self.rect.dim.width // 4, self.rect.dim.height // 2)

        self.no_action = 0
        self.jump_action = 1

        self.nb_actions = 2

        self.gravity = 0.098
        self.jump_velocity = -4
        self.world_velocity = -2

        self.pipe_width = 80
        self.pipe_gap = 150
        self.gap_between_pipes = 400
        self.birds_pipe_gap = 400

        self.birds_alive = None

        self.birds = None
        self.pipes = None
        self.gui = FlappyBirdGUI(self)
    

    def step(self, actions):
        if self.birds_alive:
            self.move_birds(actions)
            self.move_pipes()
            self.destroy_pipes()
            self.generate_pipes()
            self.kill_birds(self.find_next_pipe())

    
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
        
        while pipe_x < self.rect.dim.width:
            top_rect_height = random.randint(0, self.rect.dim.height - self.pipe_gap)
            top_rect = Rect(Point(pipe_x, 0), Dim(self.pipe_width, top_rect_height))
            bottom_rect = Rect(Point(pipe_x, top_rect_height + self.pipe_gap), Dim(self.pipe_width, self.rect.dim.height - top_rect_height - self.pipe_gap))

            self.pipes.append(Pipe(top_rect, bottom_rect))

            pipe_x += self.pipe_width + self.gap_between_pipes


    def destroy_pipes(self):
        self.pipes = [pipe for pipe in self.pipes if not (pipe.get_x() + self.pipe_width < self.rect.point.x)]


    def move_birds(self, actions):
        for action,bird in zip(actions, self.birds):
            if action == self.no_action:
                bird.velocity += self.gravity
            elif action == self.jump_action:
                bird.velocity = self.jump_velocity
            
            bird.move()


    def move_pipes(self):
        for pipe in self.pipes:
            pipe.move(self.world_velocity)


    def find_next_pipe(self):
        for pipe in self.pipes:
            if pipe.get_x() + self.pipe_width < self.birds_start_point.x:
                continue
            else:
                return pipe


    def kill_birds(self, next_pipe):
        self.birds_alive = False

        for bird in self.birds:
            if not bird.inside(self.rect) or next_pipe.hits_pipe(bird.circle):
                bird.alive = False
            else:
                self.birds_alive = True

    
    def reset(self):
        self.gui.reset()
        self.birds = self.populate_birds()
        self.generate_pipes()
        self.birds_alive = self.population > 0
    

    def render(self):
        self.gui.render()
    

    def close(self):
        self.gui.close()


