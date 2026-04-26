from pathlib import Path
import sys

import pygame

_src = Path(__file__).resolve().parent / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from environment.constants import CELL_SIZE
from LODZSIK.direction import Direction
from LODZSIK.game import Game
from render import draw

# Logikai tick külön ütem: a képernyő gyakrabban frissül, a lépés fix FPS.
LOGIC_FPS = 10
RENDER_FPS = 60
# Egy játékképkockán legfeljebb ennyi logikai lépés (lassú gépen ne egyezzen meg magát).
MAX_LOGIC_STEPS_PER_FRAME = 5


def _window_size(game: Game) -> tuple[int, int]:
    return (
        game.board.width * CELL_SIZE,
        game.board.height * CELL_SIZE,
    )


def _ensure_surface(game: Game) -> pygame.Surface:
    """Ablak méret = pálya × csempe; újraindításkor a pálya mérete változhat."""
    w, h = _window_size(game)
    surf = pygame.display.get_surface()
    if surf is None or surf.get_size() != (w, h):
        return pygame.display.set_mode((w, h))
    return surf


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
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    game = Game()
    running = True
    logic_accum = 0.0
    logic_step_s = 1.0 / LOGIC_FPS

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not _handle_keydown(game, event.key):
                    running = False

        dt = clock.tick(RENDER_FPS) / 1000.0
        logic_accum += dt
        steps = 0
        while (
            steps < MAX_LOGIC_STEPS_PER_FRAME
            and logic_accum >= logic_step_s
            and not game.game_over
            and not game.paused
        ):
            game.update()
            logic_accum -= logic_step_s
            steps += 1
        if logic_accum > 0.2:
            logic_accum = 0.2

        surface = _ensure_surface(game)
        draw(
            surface,
            game.board,
            [(p.x, p.y) for p in game.snake.body],
            game.food.position,
        )
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()