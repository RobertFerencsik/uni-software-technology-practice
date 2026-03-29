import collections

class Snake:
    def __init__(self, start_pos=(5, 5), start_direction=(1, 0)):
        self.body = collections.deque([start_pos])
        self.direction = start_direction
        self.grow_pending = False

    def move(self):
        head_x, head_y = self.body[-1]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        
        self.body.append(new_head)
        
        if not self.grow_pending:
            self.body.popleft()
        else:
            self.grow_pending = False

    def grow(self):
        self.grow_pending = True

    def check_self_collision(self):
        head = self.body[-1]
        # Itt fontos a pontos behúzás!
        for i in range(len(self.body) - 1):
            if head == self.body[i]:
                return True
        return False

    def change_direction(self, new_dir):
        # Megakadályozza a 180 fokos fordulatot
        if (new_dir[0] * -1, new_dir[1] * -1) != self.direction:
            self.direction = new_dir