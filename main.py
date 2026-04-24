from pathlib import Path
import sys

import pygame

_src = Path(__file__).resolve().parent / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from LODZSIK.game import Game

# A logika (snake lépés, ütközés) ne fusson a CPU sebességéhez kötve.
LOGIC_FPS = 10


def main():
    pygame.init()
    clock = pygame.time.Clock()
    game = Game()
    while not game.game_over:
        game.update()
        clock.tick(LOGIC_FPS)
    pygame.quit()


if __name__ == "__main__":
    main()