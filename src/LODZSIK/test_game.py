from game.game import Game


def test_game_starts_not_over():
    game = Game()

    assert game.game_over is False


def test_score_starts_zero():
    game = Game()

    assert game.score == 0