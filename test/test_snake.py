import pytest
from snake import Snake

@pytest.fixture
def snake():
    return Snake()

def test_init(snake):
    assert list(snake.body) == [(5, 5)]
    assert snake.direction == (1, 0)
    assert not snake.grow_pending

def test_move(snake):
    snake.move()
    assert list(snake.body) == [(6, 5)]

def test_grow(snake):
    snake.grow()
    snake.move()
    assert list(snake.body) == [(5, 5), (6, 5)]

def test_check_self_collision(snake):
    snake.body = [(5, 5), (6, 5), (6, 6), (5, 5)]
    assert snake.check_self_collision() is True

def test_change_direction(snake):
    snake.change_direction((0, 1))
    assert snake.direction == (0, 1)