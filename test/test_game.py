"""Pytest picks up pythonpath from pytest.ini; running this file directly does not."""
import sys
from pathlib import Path

_src = Path(__file__).resolve().parent / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from LODZSIK.direction import Direction
from LODZSIK.game import Game
from LODZSIK.point import Point
from LODZSIK.snake import Snake


def test_game_starts_not_over():
    game = Game()

    assert game.game_over is False


def test_score_starts_zero():
    game = Game()

    assert game.score == 0


def test_snake_change_direction_rejects_180_reversal():
    s = Snake(Point(5, 5))
    assert s.direction is Direction.RIGHT
    s.change_direction(Direction.LEFT)
    assert s.direction is Direction.RIGHT
    s.change_direction(Direction.UP)
    s.change_direction(Direction.DOWN)
    assert s.direction is Direction.UP


def test_toggle_pause():
    game = Game()
    assert game.paused is False
    game.toggle_pause()
    assert game.paused is True
    game.toggle_pause()
    assert game.paused is False


def test_game_update_noop_while_paused():
    game = Game()
    game.toggle_pause()
    before = [Point(p.x, p.y) for p in game.snake.body]
    game.update()
    after = [Point(p.x, p.y) for p in game.snake.body]
    assert after == before