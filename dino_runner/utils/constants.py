import pygame
import os

TITLE = "Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
FONT_STYLE = "freesansbold.ttf"

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"

ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

SOUNDTRACK = 'dino_runner/assets/Sounds/soundtrack.mp3'

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]
SKELETON = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/esqueleto.png"))
]
MINOTAUR = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/0.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/1.png"))
]
SLIME = [
        pygame.image.load(os.path.join(IMG_DIR, "Other/slime.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]
BIRD_BLUE = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1blue.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2blue.png")),
]
BIRD_GREEN = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1green.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2green.png")),
]
GHOST = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/ghost2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/ghost.png"))
    ]

METEOR = [
    pygame.image.load(os.path.join(IMG_DIR, "Other/0.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Other/1.png")),
]
BIRD_LIST = [BIRD,BIRD_BLUE,BIRD_GREEN]

LOGODINORUN = pygame.image.load(os.path.join(IMG_DIR, 'Other/logo.png'))
half_screen_height = SCREEN_HEIGHT // 2
half_screen_width = SCREEN_WIDTH // 2
LOSE_TEXT = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))




CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/teste3.jpg'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/heart.png'))

DEFAULT_TYPE = "default"
