import random
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle 

class Minotaur(Obstacle):
    def __init__(self, images): 
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = 380
        self.last_walk = 0

    def draw(self, screen):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_walk > 100:  
            self.last_walk = current_time
            screen.blit(self.images[self.type], (self.rect.x, self.rect.y))
            self.type += 1
            if self.type == 2:
                self.type = 0
        else:
            screen.blit(self.images[self.type], (self.rect.x, self.rect.y))