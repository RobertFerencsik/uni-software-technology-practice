"""Pytest picks up pythonpath from pytest.ini; running this file directly does not."""
import sys
from pathlib import Path

_src = Path(__file__).resolve().parent / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from LODZSIK.game import Game


def test_game_starts_not_over():
    game = Game()

    assert game.game_over is False


def test_score_starts_zero():
    game = Game()

    assert game.score == 0