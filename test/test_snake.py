import pytest
from snake import Snake

class TestSnake:
    def test_init(self):
        snake = Snake()
        assert list(snake.body) == [(5, 5)]
        assert snake.direction == (1, 0)
        assert not snake.grow_pending

    def test_move(self):
        snake = Snake()
        snake.move()
        assert list(snake.body) == [(6, 5)]

    def test_grow(self):
        snake = Snake()
        snake.grow()
        snake.move()
        assert list(snake.body) == [(5, 5), (6, 5)]

    def test_check_self_collision(self):
        snake = Snake()
        snake.body = [(5, 5), (6, 5), (6, 6), (5, 5)]
        assert snake.check_self_collision() is True

    def test_change_direction(self):
        snake = Snake()
        snake.change_direction((0, 1))
        assert snake.direction == (0, 1)