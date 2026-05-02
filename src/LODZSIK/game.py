from LODZSIK.point import Point
from LODZSIK.snake import Snake
from environment.board import Board
from environment.constants import MAX_ACTIVE_POWERUPS, POWERUP_SPAWN_INTERVAL_TICKS
from environment.food import Food
from environment.map_loader import MapLoader
from environment.powerup import Powerup


def _body_as_tuples(body):
    """Board and Food.spawn expect (x, y) tuples; LODZSIK snake uses Point."""
    return [(p.x, p.y) for p in body]


class Game:
    def __init__(self):
        self.loader = MapLoader()
        self.grid = self.loader.load_random_map()

        self.board = Board(self.grid)
        self.snake = Snake(start_position=Point(5, 5))
        self.food = Food()
        self.powerups: list[Powerup] = []
        self._powerup_spawn_timer = 0

        self.score = 0
        self.game_over = False
        self.paused = False

        self._setup_game()

    def _setup_game(self):
        """
        Kezdő állapot beállítása:
        - food spawn
        - snake elhelyezése
        """
        self.spawn_food()
        self.board.place_snake(_body_as_tuples(self.snake.body))

    def spawn_food(self):
        """
        Új étel generálása a board segítségével.
        """
        food_position = self.food.spawn(
            self.board,
            _body_as_tuples(self.snake.body),
        )

        self.board.place_food(food_position)

    def try_spawn_powerup(self):
        if len(self.powerups) >= MAX_ACTIVE_POWERUPS:
            return
        pup = Powerup()
        position = pup.spawn(self.board, _body_as_tuples(self.snake.body))
        self.board.place_powerup(position)
        self.powerups.append(pup)

    def _tick_powerup_spawner(self):
        self._powerup_spawn_timer += 1
        if self._powerup_spawn_timer < POWERUP_SPAWN_INTERVAL_TICKS:
            return
        self._powerup_spawn_timer = 0
        self.try_spawn_powerup()

    def toggle_pause(self) -> None:
        if not self.game_over:
            self.paused = not self.paused

    def update(self):
        """
        Egy game tick:
        - snake törlése
        - snake mozgás
        - collision check
        - food check
        - snake kirajzolás
        """
        if self.game_over or self.paused:
            return

        self.board.clear_snake(_body_as_tuples(self.snake.body))

        self.snake.move()

        self.check_collisions()

        if self.game_over:
            return

        self.check_food()

        self.check_powerups()

        self._tick_powerup_spawner()

        self.board.place_snake(_body_as_tuples(self.snake.body))

    def check_collisions(self):
        """
        Fal + önütközés vizsgálata.
        """
        head = self.snake.head

        if self.board.is_wall(head.x, head.y):
            self.game_over = True
            return

        if self.snake.collides_with_self():
            self.game_over = True

    def check_food(self):
        """
        Ha megeszi a kaját:
        - nő
        - pontszám nő
        - régi food törlés
        - új food spawn
        """
        if (self.snake.head.x, self.snake.head.y) == self.food.position:
            self.snake.grow()
            self.score += 1

            self.board.clear_food(self.food.position)
            self.spawn_food()

    def check_powerups(self):
        """Fej rálépés: eltüntetjük a powerupot; effekt egyelőre nincs."""
        head = (self.snake.head.x, self.snake.head.y)
        remaining: list[Powerup] = []
        for pup in self.powerups:
            if pup.position == head:
                self.board.clear_powerup(pup.position)
                continue
            remaining.append(pup)
        self.powerups = remaining

    def restart(self):
        """
        Új játék.
        """
        self.__init__()
