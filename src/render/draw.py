from __future__ import annotations

import pygame
from typing import List, Optional, Sequence, Tuple

from environment.board import Board
from environment.constants import (
    BACKGROUND_COLOR,
    CELL_SIZE,
)
from environment.powerup import Powerup, PowerupKind
from environment.tile import Tile

# Képek betöltése
SNAKE_HEAD_IMG = pygame.transform.scale(pygame.image.load("assets/snake_head.png"), (CELL_SIZE, CELL_SIZE))
SNAKE_BODY_IMG = pygame.transform.scale(pygame.image.load("assets/snake_body.png"), (CELL_SIZE, CELL_SIZE))
FOOD_IMG = pygame.transform.scale(pygame.image.load("assets/apple.png"), (CELL_SIZE, CELL_SIZE))
WALL_IMG = pygame.transform.scale(pygame.image.load("assets/wall.png"), (CELL_SIZE, CELL_SIZE))

POWERUP_IMAGES = {
    PowerupKind.SHORTEN: pygame.transform.scale(pygame.image.load("assets/shrink.png"), (CELL_SIZE, CELL_SIZE)),
    PowerupKind.SLOW: pygame.transform.scale(pygame.image.load("assets/slow.png"), (CELL_SIZE, CELL_SIZE)),
}

def draw(surface: pygame.Surface, board: Board, snake_body: List[Tuple[int, int]], food_pos: Optional[Tuple[int, int]], powerups: List[Powerup]):
    # 1. Háttér és Falak
    for y, row in enumerate(board.grid):
        for x, cell in enumerate(row):
            pos = (x * CELL_SIZE, y * CELL_SIZE)
            if cell == 3:
                surface.blit(WALL_IMG, pos)
            else:
                pygame.draw.rect(surface, (30, 30, 30), (*pos, CELL_SIZE, CELL_SIZE))

    # 2. Étel
    if food_pos:
        surface.blit(FOOD_IMG, (food_pos[0] * CELL_SIZE, food_pos[1] * CELL_SIZE))

    # 3. Power-upok
    for pup in powerups:
        img = POWERUP_IMAGES.get(pup.kind)
        if img:
            surface.blit(img, (pup.position[0] * CELL_SIZE, pup.position[1] * CELL_SIZE))

    # 4. Kígyó rajzolása (Forgatott fej és test)
    for i, (x, y) in enumerate(snake_body):
        pos = (x * CELL_SIZE, y * CELL_SIZE)
        angle = 0
        
        if i == 0:  # FEJ
            if len(snake_body) > 1:
                prev_node = snake_body[1]
                dx = x - prev_node[0]
                dy = y - prev_node[1]
                angle = get_angle(dx, dy)
            
            img_to_draw = pygame.transform.rotate(SNAKE_HEAD_IMG, angle)
            
        else:
            prev_node = snake_body[i-1]
            dx = prev_node[0] - x
            dy = prev_node[1] - y
            angle = get_angle(dx, dy)
            
            img_to_draw = pygame.transform.rotate(SNAKE_BODY_IMG, angle)

        rect = img_to_draw.get_rect(center=(pos[0] + CELL_SIZE // 2, pos[1] + CELL_SIZE // 2))
        surface.blit(img_to_draw, rect)

def get_angle(dx: int, dy: int) -> int:
    """Segédfüggvény a szög meghatározásához, ha az alap kép BALRA néz."""
    if dx == -1: return 0    # Balra
    if dx == 1:  return 180  # Jobbra
    if dy == -1: return 270   # Fel
    if dy == 1:  return 90  # Le
    return 0