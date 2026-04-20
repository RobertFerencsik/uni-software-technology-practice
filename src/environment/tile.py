from enum import Enum

# tile típusok
class Tile(Enum):
    EMPTY = 0
    SNAKE = 1
    FOOD = 2
    WALL = 3