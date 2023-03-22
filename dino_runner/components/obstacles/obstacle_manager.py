import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus, CactusLarge
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.meteor import Meteor
from dino_runner.components.obstacles.slime import Slime
from dino_runner.components.obstacles.cloud import *
from dino_runner.utils.constants import * 


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.clouds = []

    def update(self, game):

        if len(self.obstacles) == 0:
            random_obstacle = random.randint(0, 4) 

            if random_obstacle == 0:            
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random_obstacle == 1:
                self.obstacles.append(CactusLarge(LARGE_CACTUS))
            elif random_obstacle == 2:
                self.obstacles.append(Bird(BIRD))
            elif random_obstacle == 3:
                self.obstacles.append(Meteor(METEOR))
            elif random_obstacle == 4:
                self.obstacles.append(Slime(SLIME))
        
        if len(self.clouds) == 0:
            self.clouds.append(Cloud(CLOUD))


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles) 

            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    DEATHSOUND = pygame.mixer.music.load('dino_runner/assets/Sounds/death.wav')
                    pygame.mixer.music.play()
                    game.death_count += 1
                    break
                else:
                    self.obstacles.remove(obstacle)

        for cloud in self.clouds:
            cloud.update(game.game_speed, self.clouds)
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        
        for cloud in self.clouds:
            cloud.draw(screen)

    def reset_obstacles(self):
        self.obstacles.clear()