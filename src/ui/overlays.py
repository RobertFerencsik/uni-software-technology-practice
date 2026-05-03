import pygame
from enum import Enum, auto

class GameState(Enum):
    MENU = auto()
    RUNNING = auto()
    PAUSED = auto()
    GAME_OVER = auto()

def draw_overlay(surface, title, subtitle):
    """Félig átlátszó réteget és feliratokat rajzol a képernyőre."""
    # Sötétítő réteg (RGBA)
    overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160)) 
    surface.blit(overlay, (0, 0))
    
    # Betűtípusok betöltése
    try:
        font_title = pygame.font.SysFont("Arial", 48, bold=True)
        font_sub = pygame.font.SysFont("Arial", 24)
    except:
        font_title = pygame.font.Font(None, 64)
        font_sub = pygame.font.Font(None, 32)
    
    # Renderelés
    img_title = font_title.render(title, True, (255, 255, 255))
    img_sub = font_sub.render(subtitle, True, (200, 200, 200))
    
    # Középre pozicionálás
    rect_title = img_title.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2 - 30))
    rect_sub = img_sub.get_rect(center=(surface.get_width() // 2, surface.get_height() // 2 + 40))
    
    surface.blit(img_title, rect_title)
    surface.blit(img_sub, rect_sub)