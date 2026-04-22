from LODZSIK.point import Point
from LODZSIK.snake import Snake
from environment.board import Board
from environment.food import Food
from environment.map_loader import MapLoader


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

        self.score = 0
        self.game_over = False

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

    def update(self):
        """
        Egy game tick:
        - snake törlése
        - snake mozgás
        - collision check
        - food check
        - snake kirajzolás
        """
        if self.game_over:
            return

        self.board.clear_snake(_body_as_tuples(self.snake.body))

        self.snake.move()

        self.check_collisions()

        if self.game_over:
            return

        self.check_food()

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

    def restart(self):
        """
        Új játék.
        """
        self.__init__()
