from dino_runner.utils.constants import SCREEN_WIDTH
class Obstacle:
    def __init__(self, images, type): #O modulo cactus.py traz para seu "pai" as imagens, num aleatorio, POS_Y
        self.images = images
        self.type = type
        self.image = self.images[self.type]
        
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def draw(self, screen):
            screen.blit(self.image, (self.rect.x, self.rect.y))
  
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed    

        if self.rect.x < -self.rect.width:
            obstacles.pop()