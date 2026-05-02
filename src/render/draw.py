from __future__ import annotations

import pygame
from typing import List, Optional, Sequence, Tuple

from environment.board import Board
from environment.constants import (
    BACKGROUND_COLOR,
    CELL_SIZE,
    FOOD_COLOR,
    POWERUP_SHORTEN_COLOR,
    POWERUP_SLOW_COLOR,
    SNAKE_COLOR,
    WALL_COLOR,
)
from environment.powerup import Powerup, PowerupKind
from environment.tile import Tile


def draw(
    surface: pygame.Surface,
    board: Board,
    snake_body: List[Tuple[int, int]],
    food_position: Optional[Tuple[int, int]],
    powerups: Sequence[Powerup],
) -> None:
    """
    Kirajzolja a falakat, üres mezőket, a kígyót, az ételt és a powerupokat (típus szerinti szín).
    """
    snake_set = set(snake_body)
    head: Optional[Tuple[int, int]] = snake_body[0] if snake_body else None
    powerup_at = {p.position: p.kind for p in powerups if p.position is not None}

    for y in range(board.height):
        for x in range(board.width):
            rect = pygame.Rect(
                x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE
            )
            # Kígyó és étel a fal felett: ütközésnál is látszódjon a fej, ne tűnjön el a falban.
            if head is not None and (x, y) == head:
                color = SNAKE_COLOR
            elif (x, y) in snake_set:
                color = SNAKE_COLOR
            elif food_position is not None and (x, y) == food_position:
                color = FOOD_COLOR
            elif board.grid[y][x] == Tile.POWERUP.value:
                kind = powerup_at.get((x, y))
                if kind is PowerupKind.SLOW:
                    color = POWERUP_SLOW_COLOR
                else:
                    color = POWERUP_SHORTEN_COLOR
            elif board.grid[y][x] == Tile.WALL.value:
                color = WALL_COLOR
            else:
                color = BACKGROUND_COLOR
            pygame.draw.rect(surface, color, rect)
