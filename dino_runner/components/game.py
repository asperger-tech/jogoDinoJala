import pygame
import time
from dino_runner.utils.constants import *
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 25
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

        # Criar uma fonte para exibir a pontuação
        self.score_font = pygame.font.Font(None, 40)
        self.lose_font = pygame.font.Font(None, 70)
        self.score = 0

    def update_score(self, points):
        self.score += points

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        time.sleep(3)
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score(1)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()

        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)

        # Desenhar a pontuação na tela
        self.draw_score()
        if self.playing == False:
            self.draw_lose()

        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        # Renderizar a pontuação na fonte
        score_text = self.score_font.render(f'Score: {self.score}', True, (0, 0, 0))

        # Desenhar a pontuação na tela
        self.screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 20, 20))
    
    def draw_lose(self):
        # Renderizar a pontuação na fonte
        lose_text = self.lose_font.render('GAME OVER!', True, (0, 0, 0))

        # Desenhar a pontuação na tela
        self.screen.blit(lose_text, (SCREEN_WIDTH - lose_text.get_width() - 380, 250))
