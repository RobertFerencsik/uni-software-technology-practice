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
from ui.overlays import GameState, draw_overlay

LOGIC_FPS = 10
RENDER_FPS = 60
MAX_LOGIC_STEPS_PER_FRAME = 5
FONT_PATH = "assets/NokjaOriginalSmallBold.ttf"

def _logic_step_multiplier(game: Game) -> float:
    fn = getattr(game, "logic_step_multiplier", None)
    return float(fn()) if callable(fn) else 1.0

def _window_size(game: Game) -> tuple[int, int]:
    return (game.board.width * CELL_SIZE, game.board.height * CELL_SIZE)

def _ensure_surface(game: Game) -> pygame.Surface:
    w, h = _window_size(game)
    surf = pygame.display.get_surface()
    if surf is None or surf.get_size() != (w, h):
        return pygame.display.set_mode((w, h))
    return surf

def _handle_keydown(game: Game, key: int):
    if key in (pygame.K_UP, pygame.K_w):
        game.snake.change_direction(Direction.UP)
    elif key in (pygame.K_DOWN, pygame.K_s):
        game.snake.change_direction(Direction.DOWN)
    elif key in (pygame.K_LEFT, pygame.K_a):
        game.snake.change_direction(Direction.LEFT)
    elif key in (pygame.K_RIGHT, pygame.K_d):
        game.snake.change_direction(Direction.RIGHT)

def main():
    pygame.init()
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    font_score = pygame.font.Font(FONT_PATH, 26)
    
    game = Game()
    state = GameState.MENU
    
    running = True
    logic_accum = 0.0
    base_logic_step_s = 1.0 / LOGIC_FPS

    while running:
        dt = clock.tick(RENDER_FPS) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    running = False
                
                if state == GameState.MENU:
                    if event.key == pygame.K_SPACE:
                        game.restart()
                        state = GameState.RUNNING
                elif state == GameState.RUNNING:
                    if event.key == pygame.K_p:
                        state = GameState.PAUSED
                    else:
                        _handle_keydown(game, event.key)
                elif state == GameState.PAUSED:
                    if event.key == pygame.K_p:
                        state = GameState.RUNNING
                elif state == GameState.GAME_OVER:
                    if event.key == pygame.K_r:
                        game.restart()
                        state = GameState.RUNNING
                    elif event.key == pygame.K_m:
                        state = GameState.MENU

        if state == GameState.RUNNING:
            logic_accum += dt
            logic_step_s = base_logic_step_s * _logic_step_multiplier(game)
            steps = 0
            while steps < MAX_LOGIC_STEPS_PER_FRAME and logic_accum >= logic_step_s:
                game.update()
                logic_accum -= logic_step_s
                steps += 1
                if game.game_over:
                    state = GameState.GAME_OVER
                    break

        surface = _ensure_surface(game)
        
        draw(surface, game.board, [(p.x, p.y) for p in game.snake.body], 
             game.food.position, getattr(game, "powerups", ()))

        score_text = font_score.render(f"Score: {game.score}", True, (255, 255, 255))
        surface.blit(score_text, (33, 30))

        if state == GameState.MENU:
            draw_overlay(surface, "SNAKE", "Press SPACE to Start or Q to exit")
        elif state == GameState.PAUSED:
            draw_overlay(surface, "PAUSED", "Press P to Resume or Q to exit")
        elif state == GameState.GAME_OVER:
            draw_overlay(surface, "GAME OVER", f"Final Score: {game.score} | Press R to Restart or Q to exit")

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()