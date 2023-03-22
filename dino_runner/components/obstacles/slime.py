from dino_runner.components.obstacles.obstacle import Obstacle 
import random

class Slime(Obstacle):
    def __init__(self, images):
    
        self.type = 0
        super().__init__(images, self.type)
        
        self.rect.y = 290
