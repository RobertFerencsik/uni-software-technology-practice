# egy koordinátát jelző osztály
# (x,y) pozíció a pályán

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # átalakítás tuple-ra
    def to_tuple(self):
        return (self.x, self.y)
    
    # két pont összehasonlítása, ütközéshez stb
    def is_equal(self, other):
        return self.x == other.x and self.y == other.y
