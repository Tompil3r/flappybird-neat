from utils import Dim
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time


class FlappyBirdGUI:
    def __init__(self, env):
        self.dim = env.dim.copy()

        self.background_color = (135, 206, 235)
        self.bird_color = (212, 172, 87)
        self.pipe_color = (113, 191, 46)

        self.timer = None
        self.update_secs_delay = .01

        pygame.init()
        
        self.window = None
        self.env = env


    def render(self):
        if self.timer is not None:
            time_diff = time.perf_counter() - self.timer
        
            if time_diff < self.update_secs_delay:
                pygame.time.delay(int(self.update_secs_delay*1000 - time_diff*1000))
        
        if self.window is None:
            self.window = pygame.display.set_mode(self.dim.as_tuple())
        
        self.draw_background()
        self.draw_birds()
        self.draw_pipes()
        pygame.display.update()

        self.timer = time.perf_counter()


    def close(self):
        pygame.display.quit()
        pygame.quit()
        self.window = None
        self.timer = None


    def draw_background(self):
        pygame.draw.rect(self.window, self.background_color, [0, 0, self.dim.width, self.dim.height])
    

    def draw_birds(self):
        for bird in self.env.birds:
            pygame.draw.circle(self.window, self.bird_color, bird.circle.point.as_tuple(), bird.circle.radius)
        
    
    def draw_pipes(self):
        for pipe in self.env.pipes:
            pygame.draw.rect(self.window, self.pipe_color, pipe.top_rect.as_tuple())
            pygame.draw.rect(self.window, self.pipe_color, pipe.bottom_rect.as_tuple())



    def reset(self):
        self.timer = None
    


