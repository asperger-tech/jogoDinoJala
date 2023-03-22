from dino_runner.components.obstacles.obstacle import * 
import random

class Cactus(Obstacle):
    def __init__(self, images,y):
    
        self.type = random.randint(0,2)
        super().__init__(images, self.type)
        
        self.rect.y = y

        

  
