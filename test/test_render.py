import pygame

from environment.board import Board
from environment.constants import CELL_SIZE
from environment.tile import Tile
from render.draw import draw


def test_draw_smoke():
    pygame.init()
    try:
        grid = [[Tile.EMPTY.value for _ in range(4)] for _ in range(4)]
        grid[0][0] = Tile.WALL.value
        board = Board(grid)
        surface = pygame.Surface((board.width * CELL_SIZE, board.height * CELL_SIZE))
        draw(surface, board, [(1, 1)], (2, 2))
    finally:
        pygame.quit()
