import random

from environment.tile import Tile

class Food:

    def __init__(self):

        # aktuális pozíció
        self.position = None

    def spawn(self, board, snake_body):
        while True:
            x = random.randint(0, board.width - 1)
            y = random.randint(0, board.height - 1)

            if board.grid[y][x] == Tile.EMPTY.value and (x, y) not in snake_body:
                self.position = (x, y)
                return self.position