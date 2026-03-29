import random

from mapLayouts import map1, map2, map3

class MapLoader:
    def __init__(self):
        self.maps = [
            map1.generate,
            map2.generate,
            map3.generate
        ]

    # random map választás
    def load_random_map(self):
        chosen = random.choice(self.maps)

        return chosen()