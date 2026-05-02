from LODZSIK.point import Point
from LODZSIK.direction import Direction


class Snake:
    def __init__(self, start_position: Point):
        self.body = [start_position]
        self.direction = Direction.RIGHT
        self._grow_pending = False

    @property
    def head(self):
        return self.body[0]

    _OPPOSITE = {
        Direction.UP: Direction.DOWN,
        Direction.DOWN: Direction.UP,
        Direction.LEFT: Direction.RIGHT,
        Direction.RIGHT: Direction.LEFT,
    }

    def change_direction(self, new_direction: Direction) -> None:
        if new_direction == self._OPPOSITE.get(self.direction):
            return
        self.direction = new_direction

    def move(self):
        dx, dy = self.direction.value

        new_head = Point(
            self.head.x + dx,
            self.head.y + dy
        )

        self.body.insert(0, new_head)

        if not self._grow_pending:
            self.body.pop()
        else:
            self._grow_pending = False

    def grow(self):
        self._grow_pending = True

    def shorten_by_ratio(self, ratio: float) -> None:
        """A farok felől levágja a testet: a hossz ratio hányadával csökken (0..1)."""
        n = len(self.body)
        if n <= 1:
            return
        keep = max(1, int(n * (1.0 - ratio)))
        self.body = self.body[:keep]

    def collides_with_self(self):
        return self.head in self.body[1:]