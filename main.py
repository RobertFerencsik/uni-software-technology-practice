from pathlib import Path
import sys

import pygame

_src = Path(__file__).resolve().parent / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from LODZSIK.direction import Direction
from LODZSIK.game import Game

# A logika (snake lépés, ütközés) ne fusson a CPU sebességéhez kötve.
LOGIC_FPS = 10

# Billentyűeseményekhez kell (virtuális) ablak; méret tetszőleges.
WINDOW_SIZE = (640, 480)


def _handle_keydown(game: Game, key: int) -> bool:
    """
    Egy gomb kezelése. Visszatérés: False ha a programnak ki kell lépni.
    """
    if key in (pygame.K_ESCAPE, pygame.K_q):
        return False
    if key == pygame.K_p:
        game.toggle_pause()
        return True
    if key == pygame.K_r:
        game.restart()
        return True

    if key in (pygame.K_UP, pygame.K_w):
        game.snake.change_direction(Direction.UP)
    elif key in (pygame.K_DOWN, pygame.K_s):
        game.snake.change_direction(Direction.DOWN)
    elif key in (pygame.K_LEFT, pygame.K_a):
        game.snake.change_direction(Direction.LEFT)
    elif key in (pygame.K_RIGHT, pygame.K_d):
        game.snake.change_direction(Direction.RIGHT)
    return True


def main():
    pygame.init()
    pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    game = Game()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not _handle_keydown(game, event.key):
                    running = False

        if not game.game_over and not game.paused:
            game.update()

        pygame.display.flip()
        clock.tick(LOGIC_FPS)
    pygame.quit()


if __name__ == "__main__":
    main()