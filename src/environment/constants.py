# konstansok

# színek:
SNAKE_COLOR = (0, 200, 0)
FOOD_COLOR = (220, 0, 0)
POWERUP_SHORTEN_COLOR = (255, 180, 50)
POWERUP_SLOW_COLOR = (100, 200, 255)
WALL_COLOR = (139, 69, 19)
BACKGROUND_COLOR = (0, 0, 0)

CELL_SIZE = 30

# ennyi lépésenként próbálunk spawnolni egy új poweruppot
POWERUP_SPAWN_INTERVAL_TICKS = 50

# max ennyi powerup
MAX_ACTIVE_POWERUPS = 2

# rövidítő powerup: ennyivel csökken a hossz (a test hosszához viszonyítva)
POWERUP_SHRINK_RATIO = 0.3

# lassító powerup: ennyi másodpercig fele olyan gyors a logika (hosszabb lépésidő)
POWERUP_SLOW_DURATION_S = 10.0