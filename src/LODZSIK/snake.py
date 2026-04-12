from game.point import Point
from game.direction import Direction


class Snake:
    def __init__(self, start_position: Point):
        self.body = [start_position]
        self.direction = Direction.RIGHT
        self._grow_pending = False

    @property
    def head(self):
        return self.body[0]

    def change_direction(self, new_direction):
        # később tiltani lehet a visszafordulást
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

    def collides_with_self(self):
        return self.head in self.body[1:]