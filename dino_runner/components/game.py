import pygame
import time
from dino_runner.utils.constants import *
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE
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
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.executing = False
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.death_count = 0
        # Criar uma fonte para exibir a pontuação
        self.score_font = pygame.font.Font(None, 40)
        self.lose_font = pygame.font.Font(None, 70)
        self.score = 0
        self.font = pygame.font.Font(FONT_STYLE, 25)

    def execute(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        SOUNDTRACK = pygame.mixer.music.load('dino_runner/assets/Sounds/soundtrack.mp3')
        pygame.mixer.music.play(-1)
        # Game loop: events - update - draw
        self.playing = True
        if self.death_count == 0:
            self.reset_game()
        else:
            self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset_game(self):
        self.obstacle_manager.reset_obstacles()
        self.game_speed = 20
        self.score = 0
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score(1)
        

    def update_score(self, points):
        self.score += points
        if self.score %100 == 0:
            self.game_speed += 2


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()

        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)

        # Desenhar a pontuação na tela
        self.draw_score()
        self.draw_level()
        self.draw_deaths()
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
        self.draw_score_deaths(f"Score: {self.score}",1000,50)

    def draw_deaths(self):
        self.draw_score_deaths(f"Deaths: {self.death_count}",550,50)

    def draw_score_deaths(self,texto,x,y):
        text = self.font.render(texto, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text, text_rect)
    
    def draw_lose(self):
        lose_text = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))
        self.screen.blit(lose_text, (SCREEN_WIDTH - lose_text.get_width() - 290, 180))
    
    def draw_screen_level(self,texto,rgb):
        text = self.font.render(texto, True, (rgb))
        text_rect = text.get_rect()
        text_rect.center = (140, 50)
        self.screen.blit(text, text_rect)

    def draw_level(self):

        if self.score < 400:
            self.draw_screen_level("EASY MODE",(0,128,0))
        elif self.score < 1000:
            self.draw_screen_level("MEDIUM MODE",(238, 173, 45))
        else:
            self.draw_screen_level("HARD MODE",(255, 0, 0))

    def show_menu(self):
        self.screen.fill((255,255,255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:

            lose_text = pygame.image.load(os.path.join(IMG_DIR, 'Other/logo.png'))
            self.screen.blit(lose_text, (SCREEN_WIDTH - lose_text.get_width() - 290, 180))

            text = self.font.render("Press (s) to start playing.", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height + 130)
            self.screen.blit(text, text_rect)
        else:
            self.draw_lose()
            text = self.font.render("Press (c) to continue playing.", True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)

            text2 = self.font.render("Press (r) to restart game.", True, (0,0,0))
            text_rect.center = (half_screen_width + 30, half_screen_height + 50)
            self.screen.blit(text2, text_rect)

            text3 = self.font.render(f"Your Score: {self.score}", True, (0,0,0))
            text_rect.center = (half_screen_width + 80, half_screen_height + 140)
            self.screen.blit(text3, text_rect)
        
        pygame.display.update()
        self.handle_events_on_menu()
    
    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_s] and self.death_count == 0:
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_c]:
                    self.run()
                elif pygame.key.get_pressed()[pygame.K_r]:
                    self.death_count = 0
                    self.run()

   