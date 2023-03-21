import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus, CactusLarge
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.meteor import Meteor
from dino_runner.utils.constants import * 


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):

        if len(self.obstacles) == 0:
            random_obstacle = random.randint(0, 3) 

            if random_obstacle == 0:            
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random_obstacle == 1:
                self.obstacles.append(CactusLarge(LARGE_CACTUS))
            elif random_obstacle == 2:
                self.obstacles.append(Bird(BIRD))
            elif random_obstacle == 3:
                self.obstacles.append(Meteor(METEOR))


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)    #mover para esquerda e deleta.
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles.clear()