from game.game import Game


def main():
    game = Game()

    while not game.game_over:
        game.update()
        # ide jön később render + input


if __name__ == "__main__":
    main()