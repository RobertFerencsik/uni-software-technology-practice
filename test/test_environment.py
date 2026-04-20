from pathlib import Path
import sys

from board import Board
from food import Food
from mapLoader import MapLoader
from point import Point
from tile import Tile


def test_tile_values():
    assert Tile.EMPTY.value == 0
    assert Tile.SNAKE.value == 1
    assert Tile.FOOD.value == 2
    assert Tile.WALL.value == 3


def test_point_to_tuple():
    p = Point(3, 7)
    assert p.to_tuple() == (3, 7)


def test_point_is_equal():
    a = Point(1, 2)
    b = Point(1, 2)
    c = Point(2, 1)
    assert a.is_equal(b) is True
    assert a.is_equal(c) is False


def test_board_dimensions_and_walls():
    grid = [
        [Tile.EMPTY.value, Tile.WALL.value, Tile.EMPTY.value],
        [Tile.EMPTY.value, Tile.EMPTY.value, Tile.EMPTY.value],
        [Tile.WALL.value, Tile.EMPTY.value, Tile.EMPTY.value],
    ]
    board = Board(grid)

    assert board.width == 3
    assert board.height == 3
    assert board.is_wall(1, 0) is True
    assert board.is_wall(0, 0) is False
    assert board.is_wall(-1, 0) is True
    assert board.is_wall(0, -1) is True
    assert board.is_wall(3, 0) is True
    assert board.is_wall(0, 3) is True


def test_board_empty_food_snake_ops():
    grid = [
        [Tile.EMPTY.value, Tile.EMPTY.value, Tile.EMPTY.value],
        [Tile.EMPTY.value, Tile.EMPTY.value, Tile.EMPTY.value],
        [Tile.EMPTY.value, Tile.EMPTY.value, Tile.EMPTY.value],
    ]
    board = Board(grid)

    assert board.is_empty(0, 0) is True

    board.place_food((2, 1))
    assert board.grid[1][2] == Tile.FOOD.value

    board.clear_food((2, 1))
    assert board.grid[1][2] == Tile.EMPTY.value

    snake_body = [(0, 1), (1, 1), (2, 1)]
    board.place_snake(snake_body)
    assert board.grid[1][0] == Tile.SNAKE.value
    assert board.grid[1][1] == Tile.SNAKE.value
    assert board.grid[1][2] == Tile.SNAKE.value

    board.clear_snake(snake_body)
    assert board.grid[1][0] == Tile.EMPTY.value
    assert board.grid[1][1] == Tile.EMPTY.value
    assert board.grid[1][2] == Tile.EMPTY.value


def test_food_init():
    f = Food()
    assert f.position is None


def test_food_spawn_sets_position(monkeypatch):
    class DummyBoard:
        def __init__(self, grid):
            self.grid = grid
            self.height = len(grid)
            self.width = len(grid[0])

    board = DummyBoard([
        [Tile.EMPTY.value, Tile.WALL.value],
        [Tile.EMPTY.value, Tile.EMPTY.value],
    ])

    # First: (0,0) blocked by snake, second: (1,0) wall, third: (1,1) valid
    values = iter([0, 0, 1, 0, 1, 1])
    monkeypatch.setattr("food.random.randint", lambda a, b: next(values))

    f = Food()
    f.spawn(board, snake_body=[(0, 0)])
    assert f.position == (1, 1)


def test_maploader_has_three_maps():
    loader = MapLoader()
    assert len(loader.maps) == 3
    assert all(callable(m) for m in loader.maps)


def test_maploader_load_random_map(monkeypatch):
    loader = MapLoader()

    expected = [[9, 9], [9, 9]]

    def fake_generate():
        return expected

    monkeypatch.setattr("mapLoader.random.choice", lambda seq: fake_generate)

    result = loader.load_random_map()
    assert result == expected


def test_maploader_generated_map_shape_and_values():
    loader = MapLoader()
    grid = loader.load_random_map()

    assert isinstance(grid, list)
    assert len(grid) > 0
    assert all(isinstance(row, list) for row in grid)
    assert all(len(row) == len(grid[0]) for row in grid)
    assert all(cell in (0, 3) for row in grid for cell in row)