from src.gui import FlappyBirdGUI
from src.utils import Point, Dim, Rect, Circle
from src.bird import Bird
from src.pipe import Pipe
from collections import deque
import random
import numpy as np




class FlappyBirdEnv:

    def __init__(self, population, gui_secs_delay=0.01):
        self.population = population
        
        self.rect = Rect(Point(0, 0), Dim(800, 800))

        self.bird_radius = 20
        self.birds_start_point = Point(self.rect.dim.width // 4, self.rect.dim.height // 2)

        self.no_action = 0
        self.jump_action = 1
        self.action_prob = 0.5

        self.nb_actions = 2

        self.bird_states_shape = (population, 7)

        self.gravity = 0.098
        self.jump_velocity = -4
        self.world_velocity = -2

        self.pipe_width = 80
        self.pipe_gap = 150
        self.gap_between_pipes = 400
        self.birds_pipe_gap = 400

        self.done = None
        self.gui_secs_delay = gui_secs_delay

        self.birds = None
        self.pipes = None
        self.gui = FlappyBirdGUI(self, self.gui_secs_delay)
    

    def step(self, actions, probability_actions=True):
        if not self.done:
            self.move_birds(actions, probability_actions)
            self.move_pipes()
            self.destroy_pipes()
            self.generate_pipes()
            bird_states, birds_alive = self.update_birds(self.find_next_pipe())

            if self.done:
                return bird_states, self.get_birds_score(), birds_alive, True
            else:
                return bird_states, None, birds_alive, False

        return None, None, None, True


    def get_bird_states(self, next_pipe):
        bird_states = np.zeros(shape=self.bird_states_shape)

        for idx, bird in enumerate(self.birds):
            if bird.alive:
                bird_states[idx] = [bird.circle.point.x, bird.circle.point.y, bird.circle.radius, bird.velocity,
                next_pipe.get_x(), next_pipe.get_top_boundry(), next_pipe.get_bottom_boundry()]

        return bird_states

    
    def add_bird_scores(self):
        for bird in self.birds:
            if bird.alive:
                bird.score += 1
    

    def reset_birds_score(self):
        for bird in self.birds:
            bird.score = 0
    

    def get_birds_alive(self):
        return [bird.alive for bird in self.birds]


    def get_birds_score(self):
        return [bird.score for bird in self.birds]


    def update_birds(self, next_pipe):
        self.done = True
        bird_states = np.zeros(shape=self.bird_states_shape)
        birds_alive = np.zeros(shape=(self.population,), dtype=np.bool)

        for idx, bird in enumerate(self.birds):
            if not bird.inside(self.rect) or next_pipe.hits_pipe(bird.circle):
                bird.alive = False
            else:
                self.done = False
                birds_alive[idx] = True
                bird.score += 1

                bird_states[idx] = [bird.circle.point.x, bird.circle.point.y, bird.circle.radius, bird.velocity,
                next_pipe.get_x(), next_pipe.get_top_boundry(), next_pipe.get_bottom_boundry()]

        return bird_states, birds_alive
            
    
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


    def move_birds(self, actions, probability_actions):
        if probability_actions:        
            for action, bird in zip(actions, self.birds):
                if action < self.action_prob:
                    bird.velocity += self.gravity
                else:
                    bird.velocity = self.jump_velocity
                
                bird.move()

        else:        
            for action, bird in zip(actions, self.birds):
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
        self.done = True

        for bird in self.birds:
            if not bird.inside(self.rect) or next_pipe.hits_pipe(bird.circle):
                bird.alive = False
            else:
                self.done = False

    
    def reset(self):
        self.gui.reset()
        self.birds = self.populate_birds()
        self.pipes = None
        self.generate_pipes()
        self.done = self.population <= 0

        return self.get_bird_states(self.find_next_pipe())
    

    def render(self):
        self.gui.render()
    

    def close(self):
        self.gui.close()


