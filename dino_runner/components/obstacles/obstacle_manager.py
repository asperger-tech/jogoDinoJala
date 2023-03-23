import pygame
import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.meteor import Meteor
from dino_runner.components.obstacles.minotaur import Minotaur
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
            random_bird = random.randint(0, 2)

            if random_obstacle == 0:            
                self.obstacles.append(Minotaur(MINOTAUR))
                self.item = 1
            elif random_obstacle == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS,400))
                self.item = 1
            elif random_obstacle == 2:
                self.obstacles.append(Bird(GHOST))
                self.item = 2
            elif random_obstacle == 3:
                self.obstacles.append(Meteor(METEOR))
                self.item = 2
            elif random_obstacle == 4:
                self.obstacles.append(Slime(SKELETON))
                self.item = 1
        
        if len(self.clouds) == 0:
            self.clouds.append(Cloud(CLOUD))


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles) 

            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.lifes -=1
                    self.reset_obstacles()
                    if game.lifes == 0:
                        game.playing = False
                        DEATHSOUND = pygame.mixer.music.load('dino_runner/assets/Sounds/death.wav')
                        pygame.mixer.music.play()
                        game.death_count += 1
                        break
                elif game.player.has_power_up:
                    if game.player.type == HAMMER_TYPE and self.item == 1: 
                        self.obstacles.remove(obstacle)
                    elif game.player.type == SHIELD_TYPE:
                        self.obstacles.remove(obstacle)
                    elif game.player.type == HAMMER_TYPE and self.item == 2:
                        pygame.time.delay(500)
                        game.lifes -=1
                        self.reset_obstacles()
                        if game.lifes == 0:
                            game.playing = False
                            DEATHSOUND = pygame.mixer.music.load('dino_runner/assets/Sounds/death.wav')
                            pygame.mixer.music.play()
                            game.death_count += 1
                            break

        for cloud in self.clouds:
            cloud.update(game.game_speed, self.clouds)
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        
        for cloud in self.clouds:
            cloud.draw(screen)

    def reset_obstacles(self):
        self.obstacles.clear()