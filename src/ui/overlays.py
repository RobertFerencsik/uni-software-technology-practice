import pygame
from enum import Enum, auto

class GameState(Enum):
    MENU = auto()
    RUNNING = auto()
    PAUSED = auto()
    GAME_OVER = auto()

FONT_PATH = "assets/NokjaOriginalSmallBold.ttf"

def draw_overlay(surface, title, subtitle):
    
    try:
        font_title = pygame.font.Font(FONT_PATH, 48)
        font_sub = pygame.font.Font(FONT_PATH, 24)
    except (FileNotFoundError, RuntimeError):
        font_title = pygame.font.Font(None, 64)
        font_sub = pygame.font.Font(None, 32)
    
    img_title = font_title.render(title, True, (255, 255, 255))
    img_sub = font_sub.render(subtitle, True, (200, 200, 200))
    
    rect_title = img_title.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2 - 30))
    rect_sub = img_sub.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2 + 40))
    
    surface.blit(img_title, rect_title)
    surface.blit(img_sub, rect_sub)