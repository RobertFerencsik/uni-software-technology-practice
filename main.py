from pathlib import Path
import sys

_src = Path(__file__).resolve().parent / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from LODZSIK.game import Game

def main():
    game = Game()
    while not game.game_over:
        game.update()
if __name__ == "__main__":
    main()