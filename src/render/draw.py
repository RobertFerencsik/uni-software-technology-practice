from __future__ import annotations

import pygame
from typing import List, Optional, Tuple

from environment.board import Board
from environment.constants import (
    BACKGROUND_COLOR,
    CELL_SIZE,
    FOOD_COLOR,
    SNAKE_COLOR,
    WALL_COLOR,
)
from environment.tile import Tile


def draw(
    surface: pygame.Surface,
    board: Board,
    snake_body: List[Tuple[int, int]],
    food_position: Optional[Tuple[int, int]],
) -> None:
    """
    Kirajzolja a falakat, üres mezőket, a kígyót (body) és az ételt.
    A logika a Game modulban marad; itt csak megjelenítés.
    """
    snake_set = set(snake_body)
    head: Optional[Tuple[int, int]] = snake_body[0] if snake_body else None

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
            elif board.grid[y][x] == Tile.WALL.value:
                color = WALL_COLOR
            else:
                color = BACKGROUND_COLOR
            pygame.draw.rect(surface, color, rect)
