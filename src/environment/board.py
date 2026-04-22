from environment.tile import Tile

class Board:
    def __init__(self, grid):

        # a pálya 2D listaként
        self.grid = grid

        # méretek
        self.height = len(grid)
        self.width = len(grid[0])

    def is_wall(self, x, y):

        # ha pályán kívül van akkor fal
        if x < 0 or y < 0:
            return True
        
        if x >= self.width or y >= self.height:
            return True
        
        return self.grid[y][x] == Tile.WALL.value
    
    def is_empty(self, x, y):
        return self.grid[y][x] == Tile.EMPTY.value
    
    def place_food(self, position):
        x, y = position
        self.grid[y][x] = Tile.FOOD.value

    def clear_food(self, position):
        x, y = position
        self.grid[y][x] = Tile.EMPTY.value

    def place_snake(self, snake_body):
        for x, y in snake_body:
            self.grid[y][x] = Tile.SNAKE.value

    def clear_snake(self, snake_body):
        for x, y in snake_body:
            self.grid[y][x] = Tile.EMPTY.value